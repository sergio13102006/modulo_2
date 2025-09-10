import pytest
from ejercicio_13 import procesar_decision

def test_entrada_ir_al_norte():
    habitacion, mensaje, terminado = procesar_decision("entrada", "ir al norte")
    assert habitacion == "sala_espejos"
    assert "Te adentras en una sala" in mensaje
    assert terminado is False

def test_entrada_abrir_cofre():
    habitacion, mensaje, terminado = procesar_decision("entrada", "abrir cofre")
    assert habitacion == "entrada"
    assert "El cofre estaba encantado" in mensaje
    assert terminado is True

def test_entrada_decision_invalida():
    habitacion, mensaje, terminado = procesar_decision("entrada", "saltar")
    assert habitacion == "entrada"
    assert "Decisión no válida" in mensaje
    assert terminado is False

def test_sala_espejos_ir_al_este():
    habitacion, mensaje, terminado = procesar_decision("sala_espejos", "ir al este")
    assert habitacion == "camara_tesoro"
    assert "Has llegado a la Cámara del Tesoro" in mensaje
    assert terminado is True

def test_sala_espejos_tirar_palanca():
    habitacion, mensaje, terminado = procesar_decision("sala_espejos", "tirar palanca")
    assert habitacion == "sala_espejos"
    assert "La palanca activa una trampa" in mensaje
    assert terminado is True

def test_sala_espejos_decision_invalida():
    habitacion, mensaje, terminado = procesar_decision("sala_espejos", "gritar")
    assert habitacion == "sala_espejos"
    assert "Decisión no válida" in mensaje
    assert terminado is False

def test_camara_tesoro():
    habitacion, mensaje, terminado = procesar_decision("camara_tesoro", "cualquier cosa")
    assert habitacion == "camara_tesoro"
    assert "El juego ha terminado" in mensaje
    assert terminado is True

def test_entrada_con_mayusculas_espacios():
    habitacion, mensaje, terminado = procesar_decision("entrada", "  Ir Al Norte  ")
    assert habitacion == "sala_espejos"
    assert terminado is False

def test_sala_espejos_con_mayusculas():
    habitacion, mensaje, terminado = procesar_decision("sala_espejos", "TIRAR PALANCA")
    assert habitacion == "sala_espejos"
    assert terminado is True
