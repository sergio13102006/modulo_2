import pytest
from ejercicio_8 import clasificador_numeros


def test_numeros_pares_e_impares():
    numeros = [-5, 10, -15, 20, -25, 30]
    pares, impares, reporte = clasificador_numeros(numeros)

    # Pares correctos
    assert pares == [10, 20, 30]

    # Impares correctos
    assert impares == [-5, -15, -25]


def test_reporte_positivos_negativos():
    numeros = [-5, 10, -15, 20, -25, 30]
    _, _, reporte = clasificador_numeros(numeros)

    esperado = [
        "El número -5 es Negativo",
        "El número 10 es Positivo",
        "El número -15 es Negativo",
        "El número 20 es Positivo",
        "El número -25 es Negativo",
        "El número 30 es Positivo"
    ]

    assert reporte == esperado


def test_lista_vacia():
    numeros = []
    pares, impares, reporte = clasificador_numeros(numeros)

    # Todas las listas deben estar vacías
    assert pares == []
    assert impares == []
    assert reporte == []


def test_todos_positivos():
    numeros = [2, 4, 6, 8]
    pares, impares, reporte = clasificador_numeros(numeros)

    assert pares == [2, 4, 6, 8]
    assert impares == []
    assert all("Positivo" in msg for msg in reporte)


def test_todos_negativos():
    numeros = [-1, -3, -5]
    pares, impares, reporte = clasificador_numeros(numeros)

    assert pares == []
    assert impares == [-1, -3, -5]
    assert all("Negativo" in msg for msg in reporte)


def test_mezcla_decimales():
    numeros = [-2.5, 3.0, 4.5, -1.0]
    pares, impares, reporte = clasificador_numeros(numeros)

    # Pares son números enteros o decimales divisibles por 2
    assert pares == [4.5] or pares == []  # 4.5 no es divisible por 2 exacto, depende si queremos incluir
    # Impares
    assert -2.5 in impares or 3.0 in impares  # solo verificación básica de presencia
