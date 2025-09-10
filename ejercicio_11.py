def validar_cedula(cedula_str):
    """
    Valida una cédula según la regla: la suma de sus dígitos debe ser par.

    Validaciones:
    - No vacía
    - Solo caracteres numéricos
    - Suma de dígitos par

    Args:
        cedula_str (str): Cédula a validar.

    Returns:
        bool: True si la cédula es válida, False en caso contrario.
    """
    # Validación: no vacío
    if not cedula_str:
        raise ValueError("La cédula no puede estar vacía.")

    # Validación: solo números
    if not cedula_str.isdigit():
        raise ValueError("La cédula debe contener solo dígitos numéricos.")

    suma_digitos = sum(int(caracter) for caracter in cedula_str)

    return suma_digitos % 2 == 0


def main():
    while True:
        cedula_usuario = input("Por favor, ingresa tu número de cédula: ").strip()

        try:
            if validar_cedula(cedula_usuario):
                print("Cédula válida. Gracias.")
                break
            else:
                print("Cédula inválida. La suma de los dígitos debe ser un número par. Inténtalo de nuevo.")
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
