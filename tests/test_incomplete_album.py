from pathlib import Path
from datetime import datetime

from music_audit.checks.incomplete_album import (
    check_incomplete_album_by_metadata,
)
from music_audit.grouping import Album
from music_audit.metadata import AudioMetadata
from music_audit.scanner import AudioFile


def test_reports_album_with_missing_tracks():
    file = AudioFile(
        path=Path("/music/album/track02.mp3"),
        extension=".mp3",
        size_bytes=1000,
        modified_time=datetime.now(),
    )

    album = Album(
        path=Path("/music/album"),
        files=[file],
    )

    metadata_by_path = {
        file.path: AudioMetadata(
            title="Fantasy",
            artist="Earth Wind & Fire",
            album="All 'n All",
            track_number=2,
            track_total=8,
            encoder=None,
            sample_rate=44100,
            bitrate=128000,
        )
    }

    findings = check_incomplete_album_by_metadata(
        album,
        metadata_by_path,
    )

    assert len(findings) == 1

    assert findings[0].category == "incomplete_album_by_metadata"
    assert findings[0].severity == "CRITICAL"
    assert findings[0].message == None
    assert findings[0].expected_tracks == 8
    assert findings[0].found_tracks == 1


def test_does_not_report_complete_album():
    files = []

    metadata_by_path = {}

    for track in range(1, 9):
        file = AudioFile(
            path=Path(f"/music/album/{track:02d}.mp3"),
            extension=".mp3",
            size_bytes=1000,
            modified_time=datetime.now(),
        )

        files.append(file)

        metadata_by_path[file.path] = AudioMetadata(
            title=f"Track {track}",
            artist="Artist",
            album="Album",
            track_number=track,
            track_total=8,
            encoder=None,
            sample_rate=44100,
            bitrate=128000,
        )

    album = Album(
        path=Path("/music/album"),
        files=files,
    )

    findings = check_incomplete_album_by_metadata(
        album,
        metadata_by_path,
    )

    assert findings == []
