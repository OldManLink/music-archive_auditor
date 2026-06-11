from collections import Counter

from music_audit.grouping import Album


def count_single_track_modification_dates(albums: list[Album]) -> list[tuple[str, int]]:
    dates = Counter()

    for album in albums:
        if album.audio_file_count != 1:
            continue

        file = album.files[0]
        date = file.modified_time.date().isoformat()
        dates[date] += 1

    return sorted(
        dates.items(),
        key=lambda item: (-item[1], item[0]),
    )
