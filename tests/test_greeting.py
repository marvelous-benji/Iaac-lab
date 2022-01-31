from greeting import introduce


def test_intro1():
    assert "My name is khan" == introduce("khan")

def test_intro2():
    assert "My namen is shola" != introduce(("Annie"))