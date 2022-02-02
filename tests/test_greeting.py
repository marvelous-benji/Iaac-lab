from greeting import introduce


def test_intro1() -> None:
    assert "My name is khan" == introduce("khan")

def test_intro2() -> None:
    assert "My namen is shola" != introduce(("Annie"))