def procesar_decision(habitacion_actual, decision):
    """
    Procesa la decisión del jugador según la habitación actual.

    Args:
        habitacion_actual (str): Nombre de la habitación en la que se encuentra el jugador.
        decision (str): Decisión del jugador (opción elegida).

    Returns:
        tuple: (nueva_habitacion, mensaje, juego_terminado)
    """
    decision = decision.strip().lower()

    if habitacion_actual == "entrada":
        opciones_validas = ["ir al norte", "abrir cofre"]
        if decision not in opciones_validas:
            return habitacion_actual, "Decisión no válida. Inténtalo de nuevo.", False
        if decision == "ir al norte":
            mensaje = ("Te adentras en una sala con espejos que reflejan extrañas figuras.\n"
                       "Ves una puerta al este y una palanca oxidada en la pared.")
            return "sala_espejos", mensaje, False
        elif decision == "abrir cofre":
            mensaje = "El cofre estaba encantado y se cierra de golpe, atrapándote para siempre. ¡Has perdido!"
            return habitacion_actual, mensaje, True

    elif habitacion_actual == "sala_espejos":
        opciones_validas = ["ir al este", "tirar palanca"]
        if decision not in opciones_validas:
            return habitacion_actual, "Decisión no válida. Inténtalo de nuevo.", False
        if decision == "ir al este":
            mensaje = ("La puerta cruje al abrirse. Has llegado a la Cámara del Tesoro.\n"
                       "¡Enhorabuena! Has encontrado el tesoro y has ganado el juego.")
            return "camara_tesoro", mensaje, True
        elif decision == "tirar palanca":
            mensaje = "La palanca activa una trampa que te deja inmóvil. ¡Has perdido!"
            return habitacion_actual, mensaje, True

    elif habitacion_actual == "camara_tesoro":
        mensaje = "El juego ha terminado. ¡Has ganado!"
        return habitacion_actual, mensaje, True

    # Caso por defecto, no debería ocurrir
    return habitacion_actual, "Decisión no válida. Inténtalo de nuevo.", False


def main():
    habitacion_actual = "entrada"
    juego_terminado = False

    # Mensajes iniciales
    print("¡Bienvenido a la Aventura del Templo!")
    print("Te encuentras en la entrada de un antiguo templo. Hay un camino al norte y un cofre brillante en el centro.")

    while not juego_terminado:
        decision = input("¿Qué decides hacer? (ir al norte / abrir cofre): ")
        if not decision.strip():
            print("Entrada vacía. Por favor, elige una opción válida.")
            continue

        habitacion_actual, mensaje, juego_terminado = procesar_decision(habitacion_actual, decision)
        print(mensaje)


if __name__ == "__main__":
    main()
