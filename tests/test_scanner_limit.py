from pathlib import Path

from music_audit.scanner import scan_audio_files


def test_limit_restricts_number_of_results(tmp_path: Path):
    for i in range(5):
        (tmp_path / f"track{i}.mp3").touch()

    files = scan_audio_files(tmp_path, limit=3)

    assert len(files) == 3


def test_limit_none_returns_all_files(tmp_path: Path):
    for i in range(5):
        (tmp_path / f"track{i}.mp3").touch()

    files = scan_audio_files(tmp_path)

    assert len(files) == 5

def test_limit_of_one_returns_one_file(tmp_path: Path):
    (tmp_path / "a.mp3").touch()
    (tmp_path / "b.mp3").touch()

    files = scan_audio_files(tmp_path, limit=1)

    assert len(files) == 1
