from pathlib import Path
from typing import Optional
from music_audit.findings import Finding
from music_audit.grouping import Album
from music_audit.metadata import AudioMetadata


def check_album_track_count_by_metadata(
        album: Album,
        metadata_by_path: dict[Path, AudioMetadata],
) -> list[Finding]:
    track_totals = []

    for file in album.files:
        metadata = metadata_by_path.get(file.path)

        if (
                metadata is not None
                and metadata.track_total is not None
        ):
            track_totals.append(metadata.track_total)

    if not track_totals:
        return []

    expected_total = max(track_totals)
    actual_total = len(album.files)

    if actual_total == expected_total:
        return []

    return [
        Finding(
            severity="CRITICAL",
            category="album_track_count_by_metadata",
            album=album,
            expected_tracks=expected_total,
            found_tracks=actual_total,
            score=100,
        )
    ]
