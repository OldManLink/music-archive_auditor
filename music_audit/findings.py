from dataclasses import dataclass

from music_audit.grouping import Album


@dataclass(frozen=True)
class Finding:
    severity: str
    category: str
    album: Album
    message: str
    score: int
