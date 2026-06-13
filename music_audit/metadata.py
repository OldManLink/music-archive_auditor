from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from mutagen import File

@dataclass(frozen=True)
class AudioMetadata:
    title: Optional[str]
    artist: Optional[str]
    album: Optional[str]
    track_number: Optional[int]
    track_total: Optional[int]
    encoder: Optional[str]
    sample_rate: Optional[int]
    bitrate: Optional[int]

def read_metadata(path: Path) -> AudioMetadata:
    tags = File(path, easy=True)

    if tags is None:
        return AudioMetadata(
            title=None,
            artist=None,
            album=None,
            track_number=None,
            track_total=None,
            encoder=None,
            sample_rate=None,
            bitrate=None,
        )

    track_number, track_total = parse_track_number(tags.get("tracknumber"))

    return AudioMetadata(
        title=first_value(tags.get("title")),
        artist=first_value(tags.get("artist")),
        album=first_value(tags.get("album")),
        track_number=track_number,
        track_total=track_total,
        encoder=first_value(tags.get("encodedby")) or first_value(tags.get("encoder")),
        sample_rate=getattr(tags.info, "sample_rate", None),
        bitrate=getattr(tags.info, "bitrate", None),
    )

def first_value(values) -> Optional[str]:
    if not values:
        return None

    return values[0]

def parse_track_number(values) -> tuple[Optional[int], Optional[int]]:
    if not values:
        return None, None

    parts = str(values[0]).split("/")

    try:
        track_number = int(parts[0])
    except ValueError:
        track_number = None

    track_total = None

    if len(parts) > 1:
        try:
            track_total = int(parts[1])
        except ValueError:
            track_total = None

    return track_number, track_total
