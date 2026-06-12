from music_audit.metadata import first_value


def test_first_value_returns_first_item():
    assert first_value(["one", "two"]) == "one"


def test_first_value_returns_none_for_empty_list():
    assert first_value([]) is None


def test_first_value_returns_none_for_none():
    assert first_value(None) is None
