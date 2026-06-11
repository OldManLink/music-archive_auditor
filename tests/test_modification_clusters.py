from datetime import datetime
from pathlib import Path

from music_audit.analysis.modification_clusters import (
    count_single_track_modification_dates,
)
from music_audit.grouping import Album
from music_audit.scanner import AudioFile


def audio_file(path: Path, modified_time: datetime) -> AudioFile:
    return AudioFile(
        path=path,
        extension=path.suffix.lower(),
        size_bytes=123,
        modified_time=modified_time,
    )


def test_counts_modification_dates_for_single_track_albums(tmp_path: Path):
    albums = [
        Album(
            path=tmp_path / "Album 1",
            files=[
                audio_file(
                    tmp_path / "Album 1" / "01.m4a",
                    datetime(2009, 9, 13, 22, 35, 0),
                    )
            ],
        ),
        Album(
            path=tmp_path / "Album 2",
            files=[
                audio_file(
                    tmp_path / "Album 2" / "02.m4a",
                    datetime(2009, 9, 13, 22, 40, 0),
                    )
            ],
        ),
        Album(
            path=tmp_path / "Album 3",
            files=[
                audio_file(
                    tmp_path / "Album 3" / "01.mp3",
                    datetime(2011, 2, 18, 15, 25, 0),
                    )
            ],
        ),
    ]

    result = count_single_track_modification_dates(albums)

    assert result == [
        ("2009-09-13", 2),
        ("2011-02-18", 1),
    ]


def test_ignores_multi_track_albums(tmp_path: Path):
    albums = [
        Album(
            path=tmp_path / "Album",
            files=[
                audio_file(
                    tmp_path / "Album" / "01.m4a",
                    datetime(2009, 9, 13, 22, 35, 0),
                    ),
                audio_file(
                    tmp_path / "Album" / "02.m4a",
                    datetime(2009, 9, 13, 22, 36, 0),
                    ),
            ],
        )
    ]

    result = count_single_track_modification_dates(albums)

    assert result == []
