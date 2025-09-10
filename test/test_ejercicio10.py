import pytest
from ejercicio_10 import transponer_con_bucles

def test_matriz_rectangular():
    matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    resultado = transponer_con_bucles(matriz)
    esperado = [
        [1, 4],
        [2, 5],
        [3, 6]
    ]
    assert resultado == esperado

def test_matriz_cuadrada():
    matriz = [
        [1, 2],
        [3, 4]
    ]
    resultado = transponer_con_bucles(matriz)
    esperado = [
        [1, 3],
        [2, 4]
    ]
    assert resultado == esperado

def test_matriz_1xN():
    matriz = [[1, 2, 3, 4]]
    resultado = transponer_con_bucles(matriz)
    esperado = [
        [1],
        [2],
        [3],
        [4]
    ]
    assert resultado == esperado

def test_matriz_Nx1():
    matriz = [
        [1],
        [2],
        [3]
    ]
    resultado = transponer_con_bucles(matriz)
    esperado = [[1, 2, 3]]
    assert resultado == esperado

def test_matriz_vacia():
    matriz = []
    resultado = transponer_con_bucles(matriz)
    assert resultado == []

def test_filas_distinta_longitud():
    matriz = [
        [1, 2],
        [3, 4, 5]
    ]
    with pytest.raises(ValueError, match="todas las filas deben tener la misma cantidad de columnas"):
        transponer_con_bucles(matriz)

def test_filas_no_lista():
    matriz = [1, 2, 3]
    with pytest.raises(TypeError, match="todos los elementos de la matriz deben ser listas"):
        transponer_con_bucles(matriz)
