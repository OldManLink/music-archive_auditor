from pathlib import Path
import re
import unicodedata


from music_audit.findings import Finding
from music_audit.grouping import Album
from music_audit.metadata import AudioMetadata


def check_metadata_album_mismatch(
        album: Album,
        metadata_by_path: dict[Path, AudioMetadata],
) -> list[Finding]:
    if not album.files:
        return []
    file = album.files[0]

    metadata = metadata_by_path.get(file.path)

    if metadata is None:
        return []

    if metadata.album is None:
        return []

    if normalize_album_name(metadata.album) == normalize_album_name(album.path.name):
        return []

    return [
        Finding(
        severity="WARNING",
        category="metadata_album_mismatch",
        album=album,
        score=20,
        )
    ]

def normalize_album_name(name: str) -> str:
    normalized = unicodedata.normalize("NFC", name).lower()

    normalized = normalized.replace("_", " ")
    normalized = normalized.replace("/", " ")
    normalized = normalized.replace("\\", " ")
    normalized = normalized.replace("?", " ")
    normalized = normalized.replace(":", " ")
    normalized = normalized.replace('"', " ")
    normalized = re.sub(r"\.+", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized)

    return normalized.strip()