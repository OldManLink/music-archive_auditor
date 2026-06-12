from dataclasses import dataclass
from typing import Optional

from music_audit.grouping import Album


@dataclass(frozen=True)
class Finding:
    severity: str
    category: str
    album: Album
    score: int
    message: Optional[str] = None
    expected_tracks: Optional[int] = None
    found_tracks: Optional[int] = None
