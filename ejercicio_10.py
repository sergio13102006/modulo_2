def transponer_con_bucles(matriz):
    """
    Recibe una matriz y devuelve su transpuesta usando bucles for anidados.
    """
    # 1. Manejar el caso de una matriz vacía para evitar errores.
    if not matriz:
        return []

    # 2. Obtenemos las dimensiones de la matriz original.
    num_filas_original = len(matriz)
    num_columnas_original = len(matriz[0])

    # 3. Creamos una matriz vacía que contendrá el resultado.
    matriz_transpuesta = []

    # 4. El bucle exterior itera sobre las COLUMNAS de la matriz original.
    #    Cada iteración de este bucle creará una NUEVA FILA en la transpuesta.
    for i in range(num_columnas_original):

        # 5. Creamos una lista vacía para la nueva fila que vamos a construir.
        nueva_fila = []

        # 6. El bucle interior itera sobre las FILAS de la matriz original.
        #    Su trabajo es recoger los elementos de una columna.
        for j in range(num_filas_original):
            # 7. Añadimos el elemento de la fila 'j' y columna 'i' a nuestra nueva fila.
            nueva_fila.append(matriz[j][i])

        # 8. Una vez que hemos recorrido toda la columna, añadimos la nueva_fila completa
        #    a nuestra matriz transpuesta.
        matriz_transpuesta.append(nueva_fila)

    # 9. Devolvemos el resultado final.
    return matriz_transpuesta