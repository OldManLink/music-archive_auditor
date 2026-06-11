from music_audit.findings import Finding
from music_audit.grouping import Album


def check_single_track_album(album: Album) -> list[Finding]:
    if album.audio_file_count != 1:
        return []

    return [
        Finding(
            severity="CRITICAL",
            category="single_track_album",
            album=album,
            message="Album contains exactly one audio file",
            score=100,
        )
    ]
