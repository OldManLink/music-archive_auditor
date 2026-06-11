from datetime import datetime
from pathlib import Path

from music_audit.checks.apple_format_single_track import (
    check_apple_format_single_track_album,
)
from music_audit.grouping import Album
from music_audit.scanner import AudioFile


def audio_file(path: Path) -> AudioFile:
    return AudioFile(
        path=path,
        extension=path.suffix.lower(),
        size_bytes=123,
        modified_time=datetime(2024, 1, 1),
    )


def test_detects_single_m4a_album(tmp_path: Path):
    album = Album(
        path=tmp_path / "Album",
        files=[
            audio_file(tmp_path / "Album" / "Track.m4a")
        ],
    )

    findings = check_apple_format_single_track_album(album)

    assert len(findings) == 1
    assert findings[0].severity == "CRITICAL"
    assert findings[0].category == "apple_format_single_track_album"
    assert findings[0].score == 95


def test_single_mp3_album_is_not_detected(tmp_path: Path):
    album = Album(
        path=tmp_path / "Album",
        files=[
            audio_file(tmp_path / "Album" / "Track.mp3")
        ],
    )

    findings = check_apple_format_single_track_album(album)

    assert findings == []


def test_multi_track_album_is_not_detected(tmp_path: Path):
    album = Album(
        path=tmp_path / "Album",
        files=[
            audio_file(tmp_path / "Album" / "01.m4a"),
            audio_file(tmp_path / "Album" / "02.m4a"),
        ],
    )

    findings = check_apple_format_single_track_album(album)

    assert findings == []
