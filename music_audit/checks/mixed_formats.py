from music_audit.findings import Finding
from music_audit.grouping import Album
from collections import Counter

def check_mixed_audio_formats(album: Album) -> list[Finding]:
    format_counts = Counter(
        file.extension for file in album.files
    )

    if len(format_counts) <= 1:
        return []

    return [
        Finding(
            severity="WARNING",
            category="mixed_audio_formats",
            album=album,
            message=f"Album contains multiple audio formats",
            score=40,
        )
    ]
