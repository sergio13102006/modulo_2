import io
import sys
import pytest
from ejercicio_7 import pedir_entero, pedir_nombre_estudiante, pedir_nota, contador_notas


# =========================
# Tests para pedir_entero
# =========================
def test_pedir_entero_valido(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO("5\n"))
    assert pedir_entero("Ingrese número: ") == 5

def test_pedir_entero_negativo(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO("-3\n4\n"))
    resultado = pedir_entero("Ingrese número: ")
    captured = capsys.readouterr()
    assert resultado == 4
    assert "Error: Debe ingresar un número entero positivo" in captured.out

def test_pedir_entero_vacio(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO("\n2\n"))
    resultado = pedir_entero("Ingrese número: ")
    captured = capsys.readouterr()
    assert resultado == 2
    assert "Error: No se puede dejar vacío" in captured.out


# =========================
# Tests para pedir_nombre_estudiante
# =========================
def test_pedir_nombre_valido(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO("Sergio\n"))
    assert pedir_nombre_estudiante([]) == "Sergio"

def test_pedir_nombre_duplicado(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO("Sergio\nPedro\n"))
    resultado = pedir_nombre_estudiante(["Sergio"])
    captured = capsys.readouterr()
    assert resultado == "Pedro"
    assert "ya fue ingresado" in captured.out

def test_pedir_nombre_invalido_caracter(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO("Pe@dro\nPedro\n"))
    resultado = pedir_nombre_estudiante([])
    captured = capsys.readouterr()
    assert resultado == "Pedro"
    assert "no puede contener números ni caracteres especiales" in captured.out


# =========================
# Tests para pedir_nota
# =========================
def test_pedir_nota_valida(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO("4.5\n"))
    assert pedir_nota("Ingrese nota: ") == 4.5

def test_pedir_nota_fuera_rango(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO("6\n4\n"))
    resultado = pedir_nota("Ingrese nota: ", 0, 5)
    captured = capsys.readouterr()
    assert resultado == 4
    assert "La nota debe estar entre 0 y 5" in captured.out

def test_pedir_nota_invalida(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO("abc\n3.5\n"))
    resultado = pedir_nota("Ingrese nota: ", 0, 5)
    captured = capsys.readouterr()
    assert resultado == 3.5
    assert "Debe ingresar un número válido" in captured.out


# =========================
# Test de flujo completo contador_notas
# =========================
def test_contador_notas_completo(monkeypatch, capsys):
    entradas = "2\n2\nAna\n5\n4\nPedro\n3\n4\n"
    monkeypatch.setattr('sys.stdin', io.StringIO(entradas))
    contador_notas()
    captured = capsys.readouterr()
    assert "Notas registradas de Ana: [5.0, 4.0]" in captured.out
    assert "Notas registradas de Pedro: [3.0, 4.0]" in captured.out
