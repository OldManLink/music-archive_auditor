from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from mutagen import File


@dataclass(frozen=True)
class AudioMetadata:
    title: Optional[str]
    artist: Optional[str]
    album: Optional[str]


def read_metadata(path: Path) -> AudioMetadata:
    tags = File(path, easy=True)

    if tags is None:
        return AudioMetadata(
            title=None,
            artist=None,
            album=None,
        )

    return AudioMetadata(
        title=first_value(tags.get("title")),
        artist=first_value(tags.get("artist")),
        album=first_value(tags.get("album")),
    )


def first_value(values) -> Optional[str]:
    if not values:
        return None

    return values[0]
