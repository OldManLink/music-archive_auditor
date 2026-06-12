from music_audit.metadata import first_value
from music_audit.metadata import parse_track_number

def test_first_value_returns_first_item():
    assert first_value(["one", "two"]) == "one"


def test_first_value_returns_none_for_empty_list():
    assert first_value([]) is None


def test_first_value_returns_none_for_none():
    assert first_value(None) is None

def test_parse_track_number_with_total():
    assert parse_track_number(["04/15"]) == (4, 15)


def test_parse_track_number_without_total():
    assert parse_track_number(["04"]) == (4, None)


def test_parse_track_number_with_empty_value():
    assert parse_track_number([]) == (None, None)