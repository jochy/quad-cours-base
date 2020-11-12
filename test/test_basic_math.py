
def test_sum():
    import basicmath.basic_math as m
    assert m.sum(1, 2) == 3
    assert m.sum(2, 3) == 5
    assert m.sum(-1, 1) == 0


def test_calculator(monkeypatch):
    import basicmath.basic_math as m
    monkeypatch.setattr(m, 'sum', mocked_sum_with_fake_return)
    assert m.calculator('+', 1 , 2) == "toto"
    assert m.calculator('+', 3 , 5) == "toto"


def mocked_sum_with_fake_return(a, b):
    return "toto"
