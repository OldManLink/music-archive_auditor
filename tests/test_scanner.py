from pathlib import Path

from music_audit.scanner import scan_audio_files


def test_finds_audio_files_recursively(tmp_path: Path):
    album = tmp_path / "ACDC" / "Highway to Hell"
    album.mkdir(parents=True)

    track = album / "01 Highway to Hell.mp3"
    track.write_bytes(b"fake mp3 content")

    result = scan_audio_files(tmp_path)

    assert len(result) == 1
    assert result[0].path == track
    assert result[0].extension == ".mp3"
    assert result[0].size_bytes == len(b"fake mp3 content")


def test_ignores_non_audio_files(tmp_path: Path):
    (tmp_path / "cover.jpg").write_bytes(b"fake image")
    (tmp_path / "notes.txt").write_text("hello")

    result = scan_audio_files(tmp_path)

    assert result == []


def test_extension_matching_is_case_insensitive(tmp_path: Path):
    track = tmp_path / "Track.M4A"
    track.write_bytes(b"fake m4a content")

    result = scan_audio_files(tmp_path)

    assert len(result) == 1
    assert result[0].extension == ".m4a"


def test_records_modified_time(tmp_path: Path):
    track = tmp_path / "Track.mp3"
    track.write_bytes(b"fake content")

    result = scan_audio_files(tmp_path)

    assert result[0].modified_time is not None
