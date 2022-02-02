from hello import more_goodbye, more_hello


def test_more_hello() -> None:
    assert "hi" == more_hello()


def test_more_goodbye() -> None:
    assert "bye" == more_goodbye()
