from dataclasses import dataclass
from pathlib import Path

from music_audit.scanner import AudioFile


@dataclass(frozen=True)
class Album:
    path: Path
    files: list[AudioFile]

    @property
    def audio_file_count(self) -> int:
        return len(self.files)


def group_albums(audio_files: list[AudioFile]) -> list[Album]:
    albums_by_path: dict[Path, list[AudioFile]] = {}

    for audio_file in audio_files:
        album_path = audio_file.path.parent
        albums_by_path.setdefault(album_path, []).append(audio_file)

    albums = [
        Album(path=path, files=sorted(files, key=lambda file: file.path))
        for path, files in albums_by_path.items()
    ]

    return sorted(albums, key=lambda album: album.path)
