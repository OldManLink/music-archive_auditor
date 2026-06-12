from datetime import datetime
from pathlib import Path

from music_audit.checks.mixed_formats import check_mixed_audio_formats
from music_audit.grouping import Album
from music_audit.scanner import AudioFile


def audio_file(path: Path) -> AudioFile:
    return AudioFile(
        path=path,
        extension=path.suffix.lower(),
        size_bytes=123,
        modified_time=datetime(2024, 1, 1),
    )


def test_detects_album_with_mixed_audio_formats(tmp_path: Path):
    album = Album(
        path=tmp_path / "Album",
        files=[
            audio_file(tmp_path / "Album" / "01.mp3"),
            audio_file(tmp_path / "Album" / "02.m4a"),
        ],
    )

    findings = check_mixed_audio_formats(album)

    assert len(findings) == 1
    assert findings[0].severity == "WARNING"
    assert findings[0].category == "mixed_audio_formats"
    assert findings[0].score == 40
    assert findings[0].message == "Album contains multiple audio formats"


def test_album_with_only_mp3_files_is_not_detected(tmp_path: Path):
    album = Album(
        path=tmp_path / "Album",
        files=[
            audio_file(tmp_path / "Album" / "01.mp3"),
            audio_file(tmp_path / "Album" / "02.mp3"),
        ],
    )

    findings = check_mixed_audio_formats(album)

    assert findings == []


def test_single_track_album_is_not_mixed_format(tmp_path: Path):
    album = Album(
        path=tmp_path / "Album",
        files=[
            audio_file(tmp_path / "Album" / "01.m4a"),
        ],
    )

    findings = check_mixed_audio_formats(album)

    assert findings == []
