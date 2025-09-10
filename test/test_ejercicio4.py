# test_ejercicio4.py
import io
from unittest.mock import patch
import ejercicio_4 as juego


def run_game_with_inputs(inputs, maquina_choice, max_rondas=None):
    fake_inputs = iter(inputs)

    def fake_input(_=None):
        return next(fake_inputs)

    with patch("builtins.input", side_effect=fake_input):
        with patch("random.choice", return_value=maquina_choice):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                juego.juego(0, 0, max_rondas=max_rondas)
                return fake_out.getvalue()


def test_empate():
    salida = run_game_with_inputs(["🤛"], "🤛", max_rondas=1)
    assert "EMPATE" in salida


def test_gana_jugador():
    salida = run_game_with_inputs(["✋", "✋", "✋"], "🤛")
    assert "¡FELICIDADES! ¡HAS GANADO EL JUEGO!" in salida


def test_gana_maquina():
    salida = run_game_with_inputs(["🤛", "🤛", "🤛"], "✋")
    assert "¡LA MÁQUINA HA GANADO EL JUEGO!" in salida


def test_opcion_invalida():
    salida = run_game_with_inputs(["x", "🤛", "🤛", "🤛"], "✋")
    assert "FAILED: Solo puedes elegir" in salida
