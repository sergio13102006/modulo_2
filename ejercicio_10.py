def transponer_con_bucles(matriz):
    """
    Recibe una matriz (lista de listas) y devuelve su transpuesta usando bucles for anidados.

    Validaciones incluidas:
    - La matriz debe ser una lista de listas.
    - No puede estar vacía.
    - Todas las filas deben tener la misma longitud.

    :param matriz: Lista de listas representando la matriz.
    :return: Matriz transpuesta.
    """
    # Validación: matriz vacía
    if not matriz:
        print("Advertencia: la matriz está vacía.")
        return []

    # Validación: todas las filas deben ser listas
    if not all(isinstance(fila, list) for fila in matriz):
        raise TypeError("Error: todos los elementos de la matriz deben ser listas.")

    # Validación: todas las filas deben tener la misma longitud
    longitudes = [len(fila) for fila in matriz]
    if len(set(longitudes)) != 1:
        raise ValueError("Error: todas las filas deben tener la misma cantidad de columnas.")

    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    # Crear matriz transpuesta
    matriz_transpuesta = []

    for i in range(num_columnas):
        nueva_fila = []
        for j in range(num_filas):
            nueva_fila.append(matriz[j][i])
        matriz_transpuesta.append(nueva_fila)

    return matriz_transpuesta


def main():
    ejemplo = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print("Matriz original:")
    for fila in ejemplo:
        print(fila)

    transpuesta = transponer_con_bucles(ejemplo)

    print("\nMatriz transpuesta:")
    for fila in transpuesta:
        print(fila)


if __name__ == "__main__":
    main()
