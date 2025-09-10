import pytest
from ejercicio_14 import procesar_intento, palabra_adivinada

def test_letra_correcta():
    palabra = "python"
    letras_adivinadas = []
    intento = "p"
    mensaje, letras, fallidos, acierto, valido = procesar_intento(palabra, letras_adivinadas, intento, 0)
    assert acierto is True
    assert valido is True
    assert letras == ["p"]
    assert fallidos == 0
    assert "Bien" in mensaje

def test_letra_incorrecta():
    palabra = "python"
    letras_adivinadas = []
    intento = "z"
    mensaje, letras, fallidos, acierto, valido = procesar_intento(palabra, letras_adivinadas, intento, 0)
    assert acierto is False
    assert valido is True
    assert letras == ["z"]
    assert fallidos == 1
    assert "Pierdes un intento" in mensaje

def test_letra_repetida():
    palabra = "python"
    letras_adivinadas = ["p"]
    intento = "p"
    mensaje, letras, fallidos, acierto, valido = procesar_intento(palabra, letras_adivinadas, intento, 0)
    assert valido is False
    assert acierto is False
    assert fallidos == 0
    assert letras == ["p"]
    assert "Ya intentaste esa letra" in mensaje

def test_entrada_invalida():
    palabra = "python"
    letras_adivinadas = []
    # Entrada con número
    mensaje, letras, fallidos, acierto, valido = procesar_intento(palabra, letras_adivinadas, "4", 0)
    assert valido is False
    # Entrada vacía
    mensaje, letras, fallidos, acierto, valido = procesar_intento(palabra, letras_adivinadas, "", 0)
    assert valido is False
    # Entrada con más de una letra
    mensaje, letras, fallidos, acierto, valido = procesar_intento(palabra, letras_adivinadas, "ab", 0)
    assert valido is False

def test_palabra_adivinada_completa():
    palabra = "py"
    letras_adivinadas = ["p", "y"]
    assert palabra_adivinada(palabra, letras_adivinadas) is True

def test_palabra_adivinada_incompleta():
    palabra = "py"
    letras_adivinadas = ["p"]
    assert palabra_adivinada(palabra, letras_adivinadas) is False

def test_normalizacion_mayusculas():
    palabra = "python"
    letras_adivinadas = []
    intento = "P"
    mensaje, letras, fallidos, acierto, valido = procesar_intento(palabra, letras_adivinadas, intento, 0)
    assert letras == ["p"]  # Se normaliza a minúscula
    assert acierto is True

def test_espacios_en_entrada():
    palabra = "python"
    letras_adivinadas = []
    intento = "  t  "
    mensaje, letras, fallidos, acierto, valido = procesar_intento(palabra, letras_adivinadas, intento, 0)
    assert letras == ["t"]
    assert acierto is True
