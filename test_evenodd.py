from evenodd import evenandodd


def test_odd():
    assert evenandodd(2) == "even"
    assert evenandodd(3) == "odd"


def test_even():
    assert evenandodd(-1) == "odd"
    assert evenandodd(-2) == "even"
    assert evenandodd(-3) == "odd"