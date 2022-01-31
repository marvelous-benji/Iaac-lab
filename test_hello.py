from hello import more_goodbye, more_hello


def test_more_hello():
    assert "hi" == more_hello()


def test_more_goodbye():
    assert "bye" == more_goodbye()
