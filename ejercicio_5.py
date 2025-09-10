def validar_numero(entrada: str):
    """
    Valida que la entrada sea un número entero válido y no negativo.
    Reglas:
    - No puede estar vacía
    - No puede contener espacios
    - No puede contener letras ni símbolos
    - No puede ser negativo
    """
    if not entrada:
        return False, "Error: La entrada no puede estar vacía."

    if " " in entrada:
        return False, "Error: No se permiten espacios."

    if not entrada.isdigit():
        return False, "Error: Solo se permiten números enteros positivos."

    num = int(entrada)
    if num < 0:
        return False, "Error: El número no puede ser negativo."

    return True, num


def calcular_par_impar(num: int):
    """
    Determina si el número es par, múltiplo de 5 o ambos.
    """
    es_par = num % 2 == 0
    es_multiplo_de_5 = num % 5 == 0

    if es_par and es_multiplo_de_5:
        return f"El número {num} es par y también es múltiplo de 5."
    elif es_par:
        return f"El número {num} es par, pero no es múltiplo de 5."
    elif es_multiplo_de_5:
        return f"El número {num} es múltiplo de 5, pero no es par."
    else:
        return f"El número {num} no es par ni múltiplo de 5."


def main(input_func=input, output_func=print):
    """
    Función principal con bucle de validación.
    """
    while True:
        entrada = input_func("Ingrese un número: ").strip()
        valido, resultado = validar_numero(entrada)

        if not valido:
            output_func(resultado)
            continue

        mensaje = calcular_par_impar(resultado)
        output_func(mensaje)
        break


if __name__ == "__main__":
    main()
