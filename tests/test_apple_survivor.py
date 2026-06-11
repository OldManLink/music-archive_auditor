from datetime import datetime
from pathlib import Path

from music_audit.checks.apple_survivor import check_apple_survivor_track
from music_audit.grouping import Album
from music_audit.scanner import AudioFile


def audio_file(path: Path) -> AudioFile:
    return AudioFile(
        path=path,
        extension=path.suffix.lower(),
        size_bytes=123,
        modified_time=datetime(2024, 1, 1),
    )


def test_detects_apple_survivor_track(tmp_path: Path):
    album_path = tmp_path / "Highway to Hell"

    album = Album(
        path=album_path,
        files=[
            audio_file(album_path / "Highway to Hell.m4a")
        ],
    )

    findings = check_apple_survivor_track(album)

    assert len(findings) == 1
    assert findings[0].severity == "CRITICAL"
    assert findings[0].category == "apple_survivor_track"
    assert findings[0].score == 90


def test_mp3_file_is_not_apple_survivor(tmp_path: Path):
    album_path = tmp_path / "Highway to Hell"

    album = Album(
        path=album_path,
        files=[
            audio_file(album_path / "Highway to Hell.mp3")
        ],
    )

    findings = check_apple_survivor_track(album)

    assert findings == []


def test_multiple_files_are_not_apple_survivor(tmp_path: Path):
    album_path = tmp_path / "Highway to Hell"

    album = Album(
        path=album_path,
        files=[
            audio_file(album_path / "01.m4a"),
            audio_file(album_path / "02.m4a"),
        ],
    )

    findings = check_apple_survivor_track(album)

    assert findings == []


def test_title_must_match_album_name(tmp_path: Path):
    album_path = tmp_path / "Highway to Hell"

    album = Album(
        path=album_path,
        files=[
            audio_file(album_path / "Girls Got Rhythm.m4a")
        ],
    )

    findings = check_apple_survivor_track(album)

    assert findings == []
