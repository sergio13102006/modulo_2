import random

def lanzar_dados(num_lanzamientos=10000, caras_dado=6):
    """
    Simula el lanzamiento de dos dados y devuelve un diccionario con la frecuencia de las sumas.

    Args:
        num_lanzamientos (int): Número de veces que se lanzan los dados.
        caras_dado (int): Número de caras de cada dado (mínimo 2).

    Returns:
        dict: Diccionario donde las claves son las sumas posibles y los valores la frecuencia.
    """
    # Validaciones
    if not isinstance(num_lanzamientos, int) or num_lanzamientos <= 0:
        raise ValueError("El número de lanzamientos debe ser un entero positivo.")
    if not isinstance(caras_dado, int) or caras_dado < 2:
        raise ValueError("El dado debe tener al menos 2 caras.")

    # Inicializa frecuencias
    frecuencias_sumas = {suma: 0 for suma in range(2, 2 * caras_dado + 1)}

    # Simula los lanzamientos
    for _ in range(num_lanzamientos):
        dado1 = random.randint(1, caras_dado)
        dado2 = random.randint(1, caras_dado)
        suma = dado1 + dado2
        frecuencias_sumas[suma] += 1

    return frecuencias_sumas


def imprimir_reporte(frecuencias_sumas):
    """
    Imprime el reporte de frecuencias de las sumas de los dados.

    Args:
        frecuencias_sumas (dict): Diccionario con sumas y sus frecuencias.
    """
    print(f"Frecuencia de las sumas después de los lanzamientos:")
    print("-" * 50)
    for suma, frecuencia in sorted(frecuencias_sumas.items()):
        print(f"Suma {suma}: {frecuencia} veces")


def main():
    num_lanzamientos = 10000  # Puedes cambiar este valor si quieres
    frecuencias = lanzar_dados(num_lanzamientos=num_lanzamientos)
    imprimir_reporte(frecuencias)


if __name__ == "__main__":
    main()
