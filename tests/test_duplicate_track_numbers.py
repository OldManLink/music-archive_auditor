from datetime import datetime
from pathlib import Path

from music_audit.checks.duplicate_track_numbers import check_duplicate_track_numbers
from music_audit.grouping import Album
from music_audit.metadata import AudioMetadata
from music_audit.scanner import AudioFile


def audio_file(album_path: Path, filename: str) -> AudioFile:
    return AudioFile(
        path=album_path / filename,
        extension=Path(filename).suffix,
        size_bytes=1000,
        modified_time=datetime(2026, 6, 13, 18, 0, 0),
    )


def metadata(track_number: int) -> AudioMetadata:
    return AudioMetadata(
        title=f"Track {track_number}",
        artist="George Benson",
        album="Give Me The Night",
        track_number=track_number,
        track_total=10,
        encoder="iTunes 10.1.2",
        sample_rate=44100,
        bitrate=160000,
    )


def test_reports_duplicate_track_numbers():
    album_path = Path("/music/George Benson/Give Me The Night")

    track_1 = audio_file(album_path, "01 Love X Love.mp3")
    track_2 = audio_file(album_path, "02 - Off Broadway.mp3")
    track_6_mp3 = audio_file(album_path, "06 - Dinorah, Dinorah.mp3")
    track_6_m4a = audio_file(album_path, "06 Dinorah, Dinorah.m4a")

    album = Album(
        path=album_path,
        files=[
            track_1,
            track_2,
            track_6_mp3,
            track_6_m4a,
        ],
    )

    metadata_by_path = {
        track_1.path: metadata(1),
        track_2.path: metadata(2),
        track_6_mp3.path: metadata(6),
        track_6_m4a.path: metadata(6),
    }

    findings = check_duplicate_track_numbers(
        album,
        metadata_by_path,
    )

    assert len(findings) == 1
    assert findings[0].category == "duplicate_track_numbers"
    assert findings[0].album == album
    assert findings[0].score == 60


def test_ignores_unique_track_numbers():
    album_path = Path("/music/George Benson/Give Me The Night")

    track_1 = audio_file(album_path, "01 Love X Love.mp3")
    track_2 = audio_file(album_path, "02 - Off Broadway.mp3")
    track_3 = audio_file(album_path, "03 - Moody's Mood.mp3")

    album = Album(
        path=album_path,
        files=[
            track_1,
            track_2,
            track_3,
        ],
    )

    metadata_by_path = {
        track_1.path: metadata(1),
        track_2.path: metadata(2),
        track_3.path: metadata(3),
    }

    findings = check_duplicate_track_numbers(
        album,
        metadata_by_path,
    )

    assert findings == []
