import random
def crear_tablero(filas, columnas):
    """Crea un tablero de juego lleno de agua ('~')."""
    return [['~' for _ in range(columnas)] for _ in range(filas)]


def mostrar_tablero(tablero):
    """Muestra el tablero con coordenadas de fila y columna."""
    print("  A B C D E")
    for i, fila in enumerate(tablero):
        print(f"{i + 1} {' '.join(fila)}")


def colocar_barco(tablero, longitud):
    """Coloca un barco de forma aleatoria en el tablero."""
    filas = len(tablero)
    columnas = len(tablero[0])

    orientacion = random.choice(['horizontal', 'vertical'])

    if orientacion == 'horizontal':
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - longitud)
        ubicacion = [(fila, columna + i) for i in range(longitud)]
    else:  # 'vertical'
        fila = random.randint(0, filas - longitud)
        columna = random.randint(0, columnas - 1)
        ubicacion = [(fila + i, columna) for i in range(longitud)]

    return ubicacion


def obtener_coordenadas():
    """Válida y convierte la entrada del jugador a coordenadas de la cuadrícula."""
    while True:
        try:
            entrada = input("Ingresa las coordenadas (ej. A1): ").upper()
            if len(entrada) != 2 or not entrada[0].isalpha() or not entrada[1:].isdigit():
                raise ValueError

            columna_letra = entrada[0]
            fila_numero = int(entrada[1])

            # Convierte la letra a índice de columna (0-4) y el número a índice de fila (0-4)
            columna = ord(columna_letra) - ord('A')
            fila = fila_numero - 1

            if not (0 <= columna <= 4 and 0 <= fila <= 4):
                raise ValueError

            return fila, columna

        except (ValueError, IndexError):
            print("Entrada no válida. Asegúrate de usar el formato 'LetraNúmero' (ej. A1).")


def jugar_batalla_naval():
    """Función principal del juego."""
    print("¡Bienvenido a Batalla Naval Simplificada!")
    print("Tienes 10 turnos para hundir un barco de 3 casillas.")

    # Configuración del juego
    dimension = 5
    barco_longitud = 3
    turnos_maximos = 10

    tablero_juego = crear_tablero(dimension, dimension)
    ubicacion_barco = colocar_barco(tablero_juego, barco_longitud)
    casillas_tocadas = 0

    for turno in range(1, turnos_maximos + 1):
        print(f"\n--- Turno {turno} ---")
        mostrar_tablero(tablero_juego)

        fila_disparo, columna_disparo = obtener_coordenadas()

        if (fila_disparo, columna_disparo) in ubicacion_barco:
            if tablero_juego[fila_disparo][columna_disparo] == 'X':
                print("Ya disparaste en esta posición. Pierdes el turno.")
                continue

            print("¡Tocado!")
            tablero_juego[fila_disparo][columna_disparo] = 'X'
            casillas_tocadas += 1

            if casillas_tocadas == barco_longitud:
                print("\n¡Felicitaciones! ¡Has hundido el barco!")
                mostrar_tablero(tablero_juego)
                print("¡Has ganado el juego!")
                return

        else:
            if tablero_juego[fila_disparo][columna_disparo] in ['O', 'X']:
                print("Ya disparaste en esta posición. Pierdes el turno.")
                continue

            print("¡Agua!")
            tablero_juego[fila_disparo][columna_disparo] = 'O'

    print("\n--- Fin del juego ---")
    print(f"Te quedaste sin turnos. ¡Has perdido!")
    print("La ubicación del barco era:")
    # Muestra el barco para que el jugador vea dónde estaba
    for f, c in ubicacion_barco:
        tablero_juego[f][c] = 'B'
    mostrar_tablero(tablero_juego)


# Iniciar el juego
jugar_batalla_naval()


