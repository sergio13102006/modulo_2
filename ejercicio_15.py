import random


def crear_tablero(filas, columnas):
    """Crea un tablero de juego lleno de agua ('~')."""
    return [['~' for _ in range(columnas)] for _ in range(filas)]


def mostrar_tablero(tablero):
    """Muestra el tablero con coordenadas de fila y columna."""
    cabecera = "  " + " ".join([chr(ord('A') + i) for i in range(len(tablero[0]))])
    print(cabecera)
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


def validar_coordenada(entrada, filas, columnas):
    """
    Valida y convierte la entrada del jugador a coordenadas de la cuadrícula.

    Retorna:
        tuple: (fila, columna) si es válida
        None: si la entrada no es válida
    """
    entrada = entrada.strip().upper()

    if len(entrada) < 2:
        return None

    letra = entrada[0]
    numero = entrada[1:]

    if not letra.isalpha() or not numero.isdigit():
        return None

    columna = ord(letra) - ord('A')
    fila = int(numero) - 1

    if 0 <= fila < filas and 0 <= columna < columnas:
        return fila, columna

    return None


def disparo(tablero, fila, columna, ubicacion_barco):
    """
    Procesa un disparo en la posición indicada.

    Retorna:
        mensaje (str)
        tablero actualizado
        casilla_tocada (bool)
        repetido (bool)
    """
    if tablero[fila][columna] in ['X', 'O']:
        return "Ya disparaste en esta posición. Pierdes el turno.", tablero, False, True

    if (fila, columna) in ubicacion_barco:
        tablero[fila][columna] = 'X'
        return "¡Tocado!", tablero, True, False
    else:
        tablero[fila][columna] = 'O'
        return "¡Agua!", tablero, False, False


def jugar_batalla_naval(interactivo=True):
    """Función principal del juego."""
    print("¡Bienvenido a Batalla Naval Simplificada!") if interactivo else None
    print("Tienes 10 turnos para hundir un barco de 3 casillas.") if interactivo else None

    dimension = 5
    barco_longitud = 3
    turnos_maximos = 10

    tablero_juego = crear_tablero(dimension, dimension)
    ubicacion_barco = colocar_barco(tablero_juego, barco_longitud)
    casillas_tocadas = 0

    for turno in range(1, turnos_maximos + 1):
        print(f"\n--- Turno {turno} ---") if interactivo else None
        mostrar_tablero(tablero_juego) if interactivo else None

        if interactivo:
            entrada = input("Ingresa las coordenadas (ej. A1): ")
            coord = validar_coordenada(entrada, dimension, dimension)
            while coord is None:
                print("Entrada no válida. Usa el formato 'LetraNúmero' dentro del tablero.") if interactivo else None
                entrada = input("Ingresa las coordenadas (ej. A1): ")
                coord = validar_coordenada(entrada, dimension, dimension)
            fila_disparo, columna_disparo = coord
        else:
            # Para pruebas unitarias, podemos pasar coordenadas externas
            break

        mensaje, tablero_juego, tocado, repetido = disparo(tablero_juego, fila_disparo, columna_disparo,
                                                           ubicacion_barco)
        print(mensaje) if interactivo else None

        if tocado:
            casillas_tocadas += 1
            if casillas_tocadas == barco_longitud:
                print("\n¡Felicitaciones! ¡Has hundido el barco!") if interactivo else None
                mostrar_tablero(tablero_juego) if interactivo else None
                print("¡Has ganado el juego!") if interactivo else None
                return True

    if interactivo:
        print("\n--- Fin del juego ---")
        print(f"Te quedaste sin turnos. ¡Has perdido!")
        print("La ubicación del barco era:")
        for f, c in ubicacion_barco:
            tablero_juego[f][c] = 'B'
        mostrar_tablero(tablero_juego)
    return False


if __name__ == "__main__":
    jugar_batalla_naval()
