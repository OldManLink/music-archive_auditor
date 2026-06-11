from music_audit.findings import Finding
from music_audit.grouping import Album


def check_apple_survivor_track(album: Album) -> list[Finding]:
    if album.audio_file_count != 1:
        return []

    file = album.files[0]

    if file.extension != ".m4a":
        return []

    if file.path.stem.lower() != album.path.name.lower():
        return []

    return [
        Finding(
            severity="CRITICAL",
            category="apple_survivor_track",
            album=album,
            message="Single surviving m4a title track",
            score=90,
        )
    ]
