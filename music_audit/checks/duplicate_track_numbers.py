# music_audit/checks/duplicate_track_numbers.py

from collections import defaultdict
from pathlib import Path

from music_audit.findings import Finding
from music_audit.formatting import pluralize
from music_audit.grouping import Album
from music_audit.metadata import AudioMetadata


def check_duplicate_track_numbers(
        album: Album,
        metadata_by_path: dict[Path, AudioMetadata],
) -> list[Finding]:
    files_by_track_number = defaultdict(list)

    for file in album.files:
        metadata = metadata_by_path.get(file.path)

        if metadata is None:
            continue

        if metadata.track_number is None:
            continue

        files_by_track_number[metadata.track_number].append(file)

    duplicate_track_numbers = [
        track_number
        for track_number, files in files_by_track_number.items()
        if len(files) > 1
    ]

    if not duplicate_track_numbers:
        return []

    track_count = len(duplicate_track_numbers)
    track_numbers = ", ".join(map(str, duplicate_track_numbers))

    duplicate_message = (
        f"duplicated "
        f"{pluralize(track_count, 'track')}: "
        f"{track_numbers}"
    )
    return [
        Finding(
            severity="WARNING",
            message=duplicate_message,
            category="duplicate_track_numbers",
            album=album,
            score=60,
        )
    ]
