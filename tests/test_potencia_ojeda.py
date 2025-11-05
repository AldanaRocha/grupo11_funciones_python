from funciones.potencia_ojeda import potencia_ojeda

def test_potencia_ojeda():
    assert potencia_ojeda(2, 3) == 8
    assert potencia_ojeda(5, 0) == 1
    assert potencia_ojeda(10, 2) == 100
