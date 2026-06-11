from music_audit.findings import Finding
from music_audit.grouping import Album


def check_apple_format_single_track_album(album: Album) -> list[Finding]:
    if album.audio_file_count != 1:
        return []

    file = album.files[0]

    if file.extension != ".m4a":
        return []

    return [
        Finding(
            severity="CRITICAL",
            category="apple_format_single_track_album",
            album=album,
            message="Single-track album with surviving Apple-format file",
            score=95,
        )
    ]
