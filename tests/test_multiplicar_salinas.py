from funciones.multiplicar_salinas import multiplicar_salinas

def test_multiplicar_salinas():
    assert multiplicar_salinas(3, 5) == 15
    assert multiplicar_salinas(-2, 2) == -4