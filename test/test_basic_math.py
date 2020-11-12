
def test_calculator_ti():
    import basicmath.basic_math as m
    assert m.calculator('+', 1, 2) == 3
    f = open("logs.txt","r+")
    assert '1 + 2' in f.read()

