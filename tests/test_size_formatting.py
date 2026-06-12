from music_audit.formatting import format_bytes


def test_formats_megabytes():
    assert format_bytes(1_048_576) == "1.0 MB"


def test_formats_gigabytes():
    assert format_bytes(10_737_418_240) == "10.0 GB"
