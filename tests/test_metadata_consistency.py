from datetime import datetime
from pathlib import Path

from music_audit.grouping import Album
from music_audit.metadata import AudioMetadata
from music_audit.scanner import AudioFile
from music_audit.checks.metadata_consistency import check_metadata_album_mismatch
from music_audit.checks.metadata_consistency import normalize_album_name



def test_reports_album_metadata_mismatch():
    file = AudioFile(
        path=Path(
            "/music/King Crimson/"
            "In The Court Of The Crimson King [Bonus Tracks]/track06.mp3"
        ),
        extension=".mp3",
        size_bytes=1000,
        modified_time=datetime.now(),
    )

    album = Album(
        path=Path(
            "/music/King Crimson/"
            "In The Court Of The Crimson King [Bonus Tracks]"
        ),
        files=[file],
    )

    metadata_by_path = {
        file.path: AudioMetadata(
            title="Track",
            artist="King Crimson",
            album="In The Court Of The Crimson King",
            track_number=6,
            track_total=10,
            encoder=None,
            sample_rate=44100,
            bitrate=320000,
        )
    }

    findings = check_metadata_album_mismatch(
        album,
        metadata_by_path,
    )

    assert len(findings) == 1

def test_ignores_matching_album_names():
    file = AudioFile(
        path=Path(
            "/music/King Crimson/"
            "In The Court Of The Crimson King/track01.mp3"
        ),
        extension=".mp3",
        size_bytes=1000,
        modified_time=datetime.now(),
    )

    album = Album(
        path=Path(
            "/music/King Crimson/"
            "In The Court Of The Crimson King"
        ),
        files=[file],
    )

    metadata_by_path = {
        file.path: AudioMetadata(
            title="Track",
            artist="King Crimson",
            album="In The Court Of The Crimson King",
            track_number=1,
            track_total=10,
            encoder=None,
            sample_rate=44100,
            bitrate=320000,
        )
    }

    findings = check_metadata_album_mismatch(
        album,
        metadata_by_path,
    )

    assert findings == []

def test_normalizes_filesystem_colon_replacement():
    assert (
        normalize_album_name("Respect_ The Very Best Of Aretha Franklin")
        == normalize_album_name("Respect: The Very Best Of Aretha Franklin")
    )

def test_normalizes_unicode_equivalence():
    assert normalize_album_name("Julsånger 2009") == normalize_album_name("Julsånger 2009")

def test_normalizes_question_mark_replacement():
    assert normalize_album_name("Whose Side Are You On_") == normalize_album_name(
        "Whose Side Are You On?"
    )


def test_normalizes_quotes_replacement():
    assert normalize_album_name("_Heroes_") == normalize_album_name('"Heroes"')


def test_normalizes_slash_replacement():
    assert normalize_album_name("The Quiet Zone_The Pleasure Dome") == normalize_album_name(
        "The Quiet Zone/The Pleasure Dome"
    )


def test_normalizes_backslash_and_slash_replacement():
    assert normalize_album_name(
        "Ulvaeus_Rice_C.C.Productions _ Chess"
    ) == normalize_album_name(
        "Ulvaeus/Rice\\C.C.Productions / Chess"
    )


def test_normalizes_ellipsis_variants():
    assert normalize_album_name("This is.._") == normalize_album_name("This is...")

def test_normalizes_different_ellipsis_lengths():
    assert normalize_album_name("The Wonderful Music Of..._") == normalize_album_name("The Wonderful Music Of....")