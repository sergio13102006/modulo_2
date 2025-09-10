import pytest
from ejercicio_15 import validar_coordenada, disparo, crear_tablero, colocar_barco, jugar_batalla_naval
import ejercicio_15
# --- Test de validar_coordenada ---

def test_coordenada_valida():
    assert validar_coordenada("A1", 5, 5) == (0, 0)
    assert validar_coordenada("C3", 5, 5) == (2, 2)
    assert validar_coordenada("E5", 5, 5) == (4, 4)

def test_coordenada_fuera_rango():
    assert validar_coordenada("F1", 5, 5) is None
    assert validar_coordenada("A6", 5, 5) is None

def test_coordenada_formato_invalido():
    assert validar_coordenada("", 5, 5) is None
    assert validar_coordenada("1A", 5, 5) is None
    assert validar_coordenada("AA", 5, 5) is None
    assert validar_coordenada("A0", 5, 5) is None

# --- Test de disparo ---

def test_disparo_tocado():
    tablero = crear_tablero(5, 5)
    barco = [(0, 0), (0, 1)]
    mensaje, tablero, tocado, repetido = disparo(tablero, 0, 0, barco)
    assert tocado is True
    assert repetido is False
    assert tablero[0][0] == 'X'
    assert "Tocado" in mensaje

def test_disparo_agua():
    tablero = crear_tablero(5, 5)
    barco = [(0, 0), (0, 1)]
    mensaje, tablero, tocado, repetido = disparo(tablero, 1, 1, barco)
    assert tocado is False
    assert repetido is False
    assert tablero[1][1] == 'O'
    assert "Agua" in mensaje

def test_disparo_repetido():
    tablero = crear_tablero(5, 5)
    tablero[0][0] = 'X'
    barco = [(0, 0), (0, 1)]
    mensaje, tablero, tocado, repetido = disparo(tablero, 0, 0, barco)
    assert tocado is False
    assert repetido is True
    assert "Ya disparaste" in mensaje

# --- Test de colocar_barco ---

def test_colocar_barco_longitud():
    tablero = crear_tablero(5, 5)
    barco = colocar_barco(tablero, 3)
    assert len(barco) == 3
    for fila, col in barco:
        assert 0 <= fila < 5
        assert 0 <= col < 5

# --- Test de flujo de juego (simulación) ---


def test_juego_ganado(monkeypatch):
    barco = [(0,0), (0,1), (0,2)]
    inputs = ["A1", "B1", "C1"]

    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    monkeypatch.setattr(ejercicio_15, 'colocar_barco', lambda t, l: barco)

    resultado = ejercicio_15.jugar_batalla_naval(interactivo=True)
    assert resultado is True

def test_juego_perdido(monkeypatch):
    barco = [(0,0), (0,1), (0,2)]
    inputs = ["D4"] * 10

    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    monkeypatch.setattr(ejercicio_15, 'colocar_barco', lambda t, l: barco)

    resultado = ejercicio_15.jugar_batalla_naval(interactivo=True)
    assert resultado is False

