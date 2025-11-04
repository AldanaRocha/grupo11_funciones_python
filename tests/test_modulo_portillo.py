from funciones.modulo_portillo import modulo_portillo

def test_modulo_portillo():
    assert modulo_portillo(10, 3) == 1
    assert modulo_portillo(7, 2) == 1
    assert modulo_portillo(9, 3) == 0
    assert modulo_portillo(7, 0) is None
