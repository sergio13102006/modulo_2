import pytest
from ejercicio_6 import contar_letra_en_frase

def test_letra_presente():
    frase = "hola mundo"
    letra = "o"
    contador, posiciones = contar_letra_en_frase(frase, letra)
    assert contador == 2
    assert posiciones == [1, 8]


def test_letra_no_presente():
    frase = "hola mundo"
    letra = "z"
    contador, posiciones = contar_letra_en_frase(frase, letra)
    assert contador == 0
    assert posiciones == []

def test_espacios_ignorados():
    frase = "a b c a"
    letra = "a"
    contador, posiciones = contar_letra_en_frase(frase, letra)
    assert contador == 2
    assert posiciones == [0, 3]


def test_frase_vacia():
    with pytest.raises(ValueError):
        contar_letra_en_frase("", "a")

def test_letra_vacia():
    with pytest.raises(ValueError):
        contar_letra_en_frase("hola", "")

def test_letra_multiple():
    with pytest.raises(ValueError):
        contar_letra_en_frase("hola", "ab")

def test_letra_espacio():
    with pytest.raises(ValueError):
        contar_letra_en_frase("hola", " ")
