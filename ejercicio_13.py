# Estado inicial del juego
habitacion_actual = "entrada"
juego_terminado = False

# Mensajes iniciales y de bienvenida
print("¡Bienvenido a la Aventura del Templo!")
print("Te encuentras en la entrada de un antiguo templo. Hay un camino al norte y un cofre brillante en el centro.")

# Bucle principal del juego
while not juego_terminado:
    decision = input("¿Qué decides hacer? (ir al norte / abrir cofre): ").lower()

    if habitacion_actual == "entrada":
        if decision == "ir al norte":
            habitacion_actual = "sala_espejos"
            print("Te adentras en una sala con espejos que reflejan extrañas figuras.")
            print("Ves una puerta al este y una palanca oxidada en la pared.")
        elif decision == "abrir cofre":
            print("El cofre estaba encantado y se cierra de golpe, atrapándote para siempre. ¡Has perdido!")
            juego_terminado = True
        else:
            print("Decisión no válida. Inténtalo de nuevo.")

    elif habitacion_actual == "sala_espejos":
        if decision == "ir al este":
            habitacion_actual = "camara_tesoro"
            print("La puerta cruje al abrirse. Has llegado a la Cámara del Tesoro.")
            print("¡Enhorabuena! Has encontrado el tesoro y has ganado el juego.")
            juego_terminado = True
        elif decision == "tirar palanca":
            print("La palanca activa una trampa que te deja inmóvil. ¡Has perdido!")
            juego_terminado = True
        else:
            print("Decisión no válida. Inténtalo de nuevo.")

    elif habitacion_actual == "camara_tesoro":
        # Esta habitación solo tiene un estado de victoria, no hay más decisiones.
        print("El juego ha terminado. ¡Has ganado!")
        juego_terminado = True