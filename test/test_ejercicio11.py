import pytest
from ejercicio_11 import validar_cedula

def test_cedula_valida():
    # Suma de dígitos 1+2+3+4=10 (par)
    assert validar_cedula("1234") == True

def test_cedula_invalida_suma_impar():
    # Suma de dígitos 1+2+3=6 (par), 1+2+3+1=7 (impar)
    assert validar_cedula("1231") == False

def test_cedula_vacia():
    with pytest.raises(ValueError, match="La cédula no puede estar vacía"):
        validar_cedula("")

def test_cedula_con_letras():
    with pytest.raises(ValueError, match="La cédula debe contener solo dígitos numéricos"):
        validar_cedula("123a")

def test_cedula_con_espacios():
    with pytest.raises(ValueError, match="La cédula debe contener solo dígitos numéricos"):
        validar_cedula("12 34")

def test_cedula_con_caracteres_especiales():
    with pytest.raises(ValueError, match="La cédula debe contener solo dígitos numéricos"):
        validar_cedula("12-34")

def test_cedula_grande_valida():
    # Suma 4+5+6+7+8=30 (par)
    assert validar_cedula("45678") == True

def test_cedula_grande_invalida():
    # Suma 4+5+6+7+9=31 (impar)
    assert validar_cedula("45679") == False
