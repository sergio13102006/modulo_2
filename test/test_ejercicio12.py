import pytest
from ejercicio_12 import lanzar_dados


def test_lanzamientos_basico():
    num_lanzamientos = 1000
    caras_dado = 6
    frecuencias = lanzar_dados(num_lanzamientos=num_lanzamientos, caras_dado=caras_dado)

    # Verifica que la suma de todas las frecuencias sea igual al número de lanzamientos
    assert sum(frecuencias.values()) == num_lanzamientos

    # Verifica que las claves estén en el rango correcto
    assert set(frecuencias.keys()) == set(range(2, 2 * caras_dado + 1))


def test_lanzamientos_diferente_caras():
    num_lanzamientos = 500
    caras_dado = 8
    frecuencias = lanzar_dados(num_lanzamientos=num_lanzamientos, caras_dado=caras_dado)
    assert sum(frecuencias.values()) == num_lanzamientos
    assert set(frecuencias.keys()) == set(range(2, 2 * caras_dado + 1))


def test_lanzamientos_cero():
    with pytest.raises(ValueError, match="El número de lanzamientos debe ser un entero positivo"):
        lanzar_dados(num_lanzamientos=0)


def test_lanzamientos_negativo():
    with pytest.raises(ValueError, match="El número de lanzamientos debe ser un entero positivo"):
        lanzar_dados(num_lanzamientos=-10)


def test_lanzamientos_no_entero():
    with pytest.raises(ValueError, match="El número de lanzamientos debe ser un entero positivo"):
        lanzar_dados(num_lanzamientos=3.5)


def test_dado_caras_invalidas():
    with pytest.raises(ValueError, match="El dado debe tener al menos 2 caras"):
        lanzar_dados(num_lanzamientos=100, caras_dado=1)


def test_dado_caras_no_entero():
    with pytest.raises(ValueError, match="El dado debe tener al menos 2 caras"):
        lanzar_dados(num_lanzamientos=100, caras_dado=4.5)
