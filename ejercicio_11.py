def validar_cedula(cedula_str):
    """
    Valida una cédula (string) según la regla: la suma de sus dígitos debe ser par.

    Args:
      cedula_str: El número de cédula como una cadena de texto.

    Returns:
      True si la suma de los dígitos es par, False en caso contrario.
    """
    suma_digitos = 0
    # Itera sobre cada caracter del string 'cedula_str'.
    for caracter in cedula_str:
        # Convierte cada caracter a entero y lo suma.
        suma_digitos += int(caracter)

    # Comprueba si la suma es par.
    # El operador '%' (módulo) da el residuo de una división.
    # Si el residuo de dividir por 2 es 0, el número es par.
    if suma_digitos % 2 == 0:
        return True
    else:
        return False


# --- Programa Principal ---

# Bucle infinito que se romperá solo cuando la cédula sea válida.
while True:
    cedula_usuario = input("Por favor, ingresa tu número de cédula: ")

    # Llama a la función de validación con la entrada del usuario.
    if validar_cedula(cedula_usuario):
        print("✅ ¡Cédula válida! Gracias.")
        # Rompe el bucle si la función devuelve True.
        break
    else:
        print("❌ Cédula inválida. La suma de los dígitos debe ser un número par. Inténtalo de nuevo.")