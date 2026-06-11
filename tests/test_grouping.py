from datetime import datetime
from pathlib import Path

from music_audit.grouping import group_albums
from music_audit.scanner import AudioFile


def audio_file(path: Path) -> AudioFile:
    return AudioFile(
        path=path,
        extension=path.suffix.lower(),
        size_bytes=123,
        modified_time=datetime(2024, 1, 1),
    )


def test_files_in_same_directory_become_one_album(tmp_path: Path):
    album_path = tmp_path / "ACDC" / "Highway to Hell"
    album_path.mkdir(parents=True)

    files = [
        audio_file(album_path / "01 Highway to Hell.mp3"),
        audio_file(album_path / "02 Girls Got Rhythm.mp3"),
    ]

    albums = group_albums(files)

    assert len(albums) == 1
    assert albums[0].path == album_path
    assert albums[0].audio_file_count == 2


def test_files_in_different_directories_become_different_albums(tmp_path: Path):
    album_1 = tmp_path / "ACDC" / "Highway to Hell"
    album_2 = tmp_path / "ACDC" / "Back in Black"
    album_1.mkdir(parents=True)
    album_2.mkdir(parents=True)

    albums = group_albums([
        audio_file(album_1 / "01 Highway to Hell.mp3"),
        audio_file(album_2 / "01 Hells Bells.mp3"),
    ])

    assert len(albums) == 2
    assert [album.path for album in albums] == [album_2, album_1]


def test_files_inside_album_are_sorted(tmp_path: Path):
    album_path = tmp_path / "Album"
    album_path.mkdir()

    albums = group_albums([
        audio_file(album_path / "02 Track.mp3"),
        audio_file(album_path / "01 Track.mp3"),
    ])

    assert [file.path.name for file in albums[0].files] == [
        "01 Track.mp3",
        "02 Track.mp3",
    ]


def test_returns_empty_list_when_no_audio_files():
    assert group_albums([]) == []
