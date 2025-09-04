import random


def jugar_ahorcado():
    """Función principal para jugar al Ahorcado."""

    palabras = ["python", "programacion", "computadora", "algoritmo", "desarrollo", "interfaz"]
    palabra_secreta = random.choice(palabras).lower()
    letras_adivinadas = []
    intentos_fallidos = 0
    max_intentos = 6

    print("¡Bienvenido al Ahorcado!")
    print("Adivina la palabra secreta. Tienes 6 intentos.")

    while intentos_fallidos < max_intentos:
        # 1. Mostrar el estado del juego
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        print(f"Intentos restantes: {max_intentos - intentos_fallidos}")
        print(f"Letras usadas: {', '.join(sorted(letras_adivinadas))}")

        # 2. Solicitar y validar la entrada del jugador
        entrada = input("Ingresa una letra: ").lower()

        if not entrada.isalpha() or len(entrada) != 1:
            print("Entrada no válida. Por favor, ingresa una sola letra.")
            continue

        if entrada in letras_adivinadas:
            print("Ya intentaste esa letra. Elige otra.")
            continue

        letras_adivinadas.append(entrada)

        # 3. Lógica del juego
        if entrada in palabra_secreta:
            print("¡Bien! La letra está en la palabra.")
        else:
            print("Esa letra no está. Pierdes un intento.")
            intentos_fallidos += 1

        # 4. Comprobar si el jugador ha ganado
        if palabra_adivinada(palabra_secreta, letras_adivinadas):
            print("\n¡Felicitaciones! ¡Has adivinado la palabra!")
            print(f"La palabra era: {palabra_secreta}")
            break

    # 5. Comprobar si el jugador ha perdido
    if intentos_fallidos >= max_intentos:
        print("\n¡Oh no! Te quedaste sin intentos. ¡Has perdido!")
        print(f"La palabra secreta era: {palabra_secreta}")


def mostrar_tablero(palabra, letras_adivinadas):
    """Muestra el progreso de la palabra con guiones bajos."""
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    print("\n" + tablero)


def palabra_adivinada(palabra, letras_adivinadas):
    """Verifica si todas las letras de la palabra han sido adivinadas."""
    for letra in palabra:
        if letra not in letras_adivinadas:
            return False
    return True


# Inicia el juego
jugar_ahorcado()