import pytest
from ejercicio_9 import calcular_precios_con_iva

def test_precios_con_iva_basico():
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000}
    ]
    resultado = calcular_precios_con_iva(productos)
    esperado = {
        "Camisa": 59500.0,     # 50000 * 1.19
        "Pantalón": 95200.0,   # 80000 * 1.19
        "Zapatos": 142800.0    # 120000 * 1.19
    }
    assert resultado == esperado

def test_precios_con_iva_diferente_iva():
    productos = [
        {"nombre": "Gorra", "precio": 20000},
        {"nombre": "Bufanda", "precio": 15000}
    ]
    resultado = calcular_precios_con_iva(productos, iva=0.10)  # IVA 10%
    esperado = {
        "Gorra": 22000.0,
        "Bufanda": 16500.0
    }
    assert resultado == esperado

def test_precios_con_iva_lista_vacia():
    productos = []
    resultado = calcular_precios_con_iva(productos)
    assert resultado == {}

def test_precios_con_iva_precio_cero():
    productos = [{"nombre": "Calcetines", "precio": 0}]
    resultado = calcular_precios_con_iva(productos)
    esperado = {"Calcetines": 0.0}
    assert resultado == esperado

def test_precios_con_iva_precio_decimal():
    productos = [{"nombre": "Corbata", "precio": 12345.67}]
    resultado = calcular_precios_con_iva(productos)
    esperado = {"Corbata": round(12345.67 * 1.19, 2)}
    assert resultado == esperado
