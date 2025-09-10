def clasificador_numeros(numeros):
    """
    Clasifica una lista de números en pares/impares y positivos/negativos.
    :param numeros: Lista de números a clasificar.
    :return: Tuple (numeros_pares, numeros_impares, reporte_numeros)
    """
    numeros_pares = [num for num in numeros if num % 2 == 0]
    numeros_impares = [num for num in numeros if num % 2 != 0]

    reporte_numeros = [
        f"El número {num} es Positivo" if num >= 0 else f"El número {num} es Negativo"
        for num in numeros
    ]

    return numeros_pares, numeros_impares, reporte_numeros


def main():
    numeros = [-5, 10, -15, 20, -25, 30]

    pares, impares, reporte = clasificador_numeros(numeros)

    print("=== Clasificador de números ===")
    print("Lista original:", numeros)
    print("Números pares:", pares)
    print("Números impares:", impares)
    print("\nReporte:")
    for mensaje in reporte:
        print(mensaje)


if __name__ == "__main__":
    main()
