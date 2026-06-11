from datetime import datetime
from pathlib import Path

from music_audit.checks.single_track import check_single_track_album
from music_audit.grouping import Album
from music_audit.scanner import AudioFile


def audio_file(path: Path) -> AudioFile:
    return AudioFile(
        path=path,
        extension=path.suffix.lower(),
        size_bytes=123,
        modified_time=datetime(2024, 1, 1),
    )


def test_single_track_album_generates_finding(tmp_path: Path):
    album = Album(
        path=tmp_path / "Highway to Hell",
        files=[
            audio_file(tmp_path / "Highway to Hell" / "Highway to Hell.m4a")
        ],
    )

    findings = check_single_track_album(album)

    assert len(findings) == 1
    assert findings[0].severity == "CRITICAL"
    assert findings[0].category == "single_track_album"
    assert findings[0].score == 100


def test_multi_track_album_generates_no_finding(tmp_path: Path):
    album = Album(
        path=tmp_path / "Back in Black",
        files=[
            audio_file(tmp_path / "Back in Black" / "01.mp3"),
            audio_file(tmp_path / "Back in Black" / "02.mp3"),
        ],
    )

    findings = check_single_track_album(album)

    assert findings == []
