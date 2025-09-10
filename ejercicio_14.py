import random

def palabra_adivinada(palabra, letras_adivinadas):
    """Verifica si todas las letras de la palabra han sido adivinadas."""
    return all(letra in letras_adivinadas for letra in palabra)


def mostrar_tablero(palabra, letras_adivinadas):
    """Muestra el progreso de la palabra con guiones bajos."""
    tablero = " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])
    print("\n" + tablero)


def procesar_intento(palabra_secreta, letras_adivinadas, intento, intentos_fallidos):
    """
    Procesa un intento de letra del jugador.

    Args:
        palabra_secreta (str): La palabra que se debe adivinar.
        letras_adivinadas (list): Letras que ya han sido adivinadas.
        intento (str): Letra ingresada por el jugador.
        intentos_fallidos (int): Número actual de intentos fallidos.

    Returns:
        tuple: (mensaje, letras_adivinadas, intentos_fallidos, acierto, valido)
    """
    intento = intento.strip().lower()

    if not intento.isalpha() or len(intento) != 1:
        return "Entrada no válida. Por favor, ingresa una sola letra.", letras_adivinadas, intentos_fallidos, False, False

    if intento in letras_adivinadas:
        return "Ya intentaste esa letra. Elige otra.", letras_adivinadas, intentos_fallidos, False, False

    letras_adivinadas.append(intento)

    if intento in palabra_secreta:
        return "¡Bien! La letra está en la palabra.", letras_adivinadas, intentos_fallidos, True, True
    else:
        intentos_fallidos += 1
        return "Esa letra no está. Pierdes un intento.", letras_adivinadas, intentos_fallidos, False, True


def jugar_ahorcado(interactivo=True):
    """Función principal para jugar al Ahorcado."""
    palabras = ["python", "programacion", "computadora", "algoritmo", "desarrollo", "interfaz"]
    palabra_secreta = random.choice(palabras).lower()
    letras_adivinadas = []
    intentos_fallidos = 0
    max_intentos = 6

    if interactivo:
        print("¡Bienvenido al Ahorcado!")
        print("Adivina la palabra secreta. Tienes 6 intentos.")

    while intentos_fallidos < max_intentos:
        if interactivo:
            mostrar_tablero(palabra_secreta, letras_adivinadas)
            print(f"Intentos restantes: {max_intentos - intentos_fallidos}")
            print(f"Letras usadas: {', '.join(sorted(letras_adivinadas))}")
            intento = input("Ingresa una letra: ")
        else:
            # Para pruebas unitarias, se podría pasar los intentos externamente
            break

        mensaje, letras_adivinadas, intentos_fallidos, acierto, valido = procesar_intento(
            palabra_secreta, letras_adivinadas, intento, intentos_fallidos
        )

        if interactivo:
            print(mensaje)

        if palabra_adivinada(palabra_secreta, letras_adivinadas):
            if interactivo:
                print("\n¡Felicitaciones! ¡Has adivinado la palabra!")
                print(f"La palabra era: {palabra_secreta}")
            break

    if intentos_fallidos >= max_intentos and interactivo:
        print("\n¡Oh no! Te quedaste sin intentos. ¡Has perdido!")
        print(f"La palabra secreta era: {palabra_secreta}")


if __name__ == "__main__":
    jugar_ahorcado()
