import io
from unittest.mock import patch
import ejercicio_2 as menu
def run_menu_with_inputs(inputs):
    fake_input = iter(inputs).__next__
    with patch("sys.stdout", new=io.StringIO()) as fake_out:
        with patch("time.sleep", return_value=None):
            menu.menu(input_func=fake_input)
        return fake_out.getvalue()


def test_opcion_guardar():
    salida = run_menu_with_inputs(["1", "3"])
    assert "Guardando archivo..." in salida
    assert "Guardado con éxito" in salida


def test_opcion_cargar():
    salida = run_menu_with_inputs(["2", "3"])
    assert "Cargando..." in salida
    assert "Cargado con éxito" in salida


def test_opcion_salir():
    salida = run_menu_with_inputs(["3"])
    assert "Saliendo del programa..." in salida
    assert "Gracias por utilizar el programa" in salida


def test_opcion_invalida():
    salida = run_menu_with_inputs(["a", "", "5", "3"])
    assert "Debe digitar solo números enteros" in salida
    assert "No puede dejar el campo vacío." in salida
    assert "Opción fuera de rango" in salida
