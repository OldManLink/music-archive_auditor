from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

AUDIO_EXTENSIONS = {".mp3", ".m4a", ".m4p", ".aac", ".flac", ".wav"}


@dataclass(frozen=True)
class AudioFile:
    path: Path
    extension: str
    size_bytes: int
    modified_time: datetime
    @property
    def size_mb(self) -> float:
        return self.size_bytes / (1024 * 1024)

def scan_audio_files(root: Path, limit: Optional[int] = None) -> list[AudioFile]:
    audio_files: list[AudioFile] = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue

        extension = path.suffix.lower()
        if extension not in AUDIO_EXTENSIONS:
            continue

        stat = path.stat()
        audio_files.append(
            AudioFile(
                path=path,
                extension=extension,
                size_bytes=stat.st_size,
                modified_time=datetime.fromtimestamp(stat.st_mtime),
            )
        )
        if limit is not None and len(audio_files) >= limit:
            return audio_files

    return sorted(audio_files, key=lambda audio_file: audio_file.path)
