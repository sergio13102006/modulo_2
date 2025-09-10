def pedir_numero(input_func=input, output_func=print, minimo=None, maximo=None):
    """
    Pide un número entero al usuario con validaciones:
    - No vacío
    - Solo números enteros
    - No negativos (opcional)
    - No decimales
    - No mezcla de letras y números
    - Dentro de los límites (si se indican minimo y maximo)
    """
    while True:
        entrada = input_func("Digite un número: ").strip()

        # Validar vacío
        if entrada == "":
            output_func("✖️ No puede dejar el campo vacío.")
            continue

        # Validar si es entero (sin letras, sin decimales, sin símbolos)
        if not entrada.isdigit() and not (entrada.startswith("-") and entrada[1:].isdigit()):
            output_func("✖️ Debe digitar solo números enteros, sin letras, decimales ni símbolos.")
            continue

        # Convertir a número
        numero = int(entrada)

        # Validar negativo
        if numero < 0:
            output_func("✖️ No se permiten números negativos.")
            continue

        # Validar límites
        if minimo is not None and numero < minimo:
            output_func(f"✖️ El número debe ser mayor o igual a {minimo}.")
            continue
        if maximo is not None and numero > maximo:
            output_func(f"✖️ El número debe ser menor o igual a {maximo}.")
            continue

        # Si todo está bien
        return numero


if __name__ == "__main__":
    # Ejemplo de uso
    n = pedir_numero(minimo=1, maximo=10)
    print(f"✔️ Número válido ingresado: {n}")
