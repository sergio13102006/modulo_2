import pytest
from ejercicio_5 import validar_numero, calcular_par_impar

def test_vacio():
    valido, msg = validar_numero("")
    assert not valido
    assert "vacía" in msg

def test_espacio():
    valido, msg = validar_numero(" 123")
    assert not valido
    assert "espacios" in msg

def test_letras():
    valido, msg = validar_numero("abc")
    assert not valido
    assert "enteros positivos" in msg

def test_simbolos():
    valido, msg = validar_numero("@12")
    assert not valido
    assert "enteros positivos" in msg

def test_negativo():
    valido, msg = validar_numero("-5")
    # OJO: "-5" falla en isdigit() primero
    assert not valido
    assert "enteros positivos" in msg

def test_valido():
    valido, num = validar_numero("12")
    assert valido
    assert num == 12



def test_par_multiplo_de_5():
    assert calcular_par_impar(10) == "El número 10 es par y también es múltiplo de 5."

def test_solo_par():
    assert calcular_par_impar(4) == "El número 4 es par, pero no es múltiplo de 5."

def test_solo_multiplo_de_5():
    assert calcular_par_impar(25) == "El número 25 es múltiplo de 5, pero no es par."

def test_ninguno():
    assert calcular_par_impar(7) == "El número 7 no es par ni múltiplo de 5."
