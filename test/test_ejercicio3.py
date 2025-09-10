import io
from unittest.mock import patch
import ejercicio_3


def run_with_inputs(inputs, minimo=None, maximo=None):
    """Simula inputs y captura salidas del validador"""
    it = iter(inputs)
    fake_input = lambda _: next(it)   # acepta un argumento pero no lo usa
    fake_output = io.StringIO()
    with patch("sys.stdout", new=fake_output):
        try:
            resultado = ejercicio_3.pedir_numero(
                input_func=fake_input,
                output_func=print,
                minimo=minimo,
                maximo=maximo
            )
        except StopIteration:
            resultado = None
    return fake_output.getvalue(), resultado


def test_vacio():
    salida, resultado = run_with_inputs(["", "5"])
    assert "No puede dejar el campo vacío" in salida
    assert resultado == 5


def test_texto():
    salida, resultado = run_with_inputs(["abc", "7"])
    assert "Debe digitar solo números enteros" in salida
    assert resultado == 7


def test_numero_mas_letras():
    salida, resultado = run_with_inputs(["12a3", "9"])
    assert "Debe digitar solo números enteros" in salida
    assert resultado == 9


def test_decimal():
    salida, resultado = run_with_inputs(["3.14", "4"])
    assert "Debe digitar solo números enteros" in salida
    assert resultado == 4


def test_negativo():
    salida, resultado = run_with_inputs(["-5", "2"])
    assert "No se permiten números negativos" in salida
    assert resultado == 2


def test_fuera_de_rango_menor():
    salida, resultado = run_with_inputs(["0", "3"], minimo=1, maximo=10)
    assert "El número debe ser mayor o igual a 1" in salida
    assert resultado == 3


def test_fuera_de_rango_mayor():
    salida, resultado = run_with_inputs(["20", "8"], minimo=1, maximo=10)
    assert "El número debe ser menor o igual a 10" in salida
    assert resultado == 8


def test_valido():
    salida, resultado = run_with_inputs(["5"], minimo=1, maximo=10)
    assert "✖️" not in salida  # no debe haber errores
    assert resultado == 5
