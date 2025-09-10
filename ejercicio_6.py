def contar_letra_en_frase(frase: str, letra: str):
    """
    Cuenta cuántas veces aparece una letra en una frase y devuelve sus posiciones
    ignorando los espacios (las posiciones se cuentan sin considerar los espacios).
    """
    if not frase:
        raise ValueError("La frase no puede estar vacía.")
    if not letra or len(letra) != 1 or letra == ' ':
        raise ValueError("Debe ingresar exactamente un carácter válido (no espacio).")

    contador = 0
    posiciones = []
    index_sin_espacios = 0  # posición contando solo caracteres que no son espacio

    for caracter in frase:
        if caracter != ' ':  # ignorar espacios
            if caracter == letra:
                contador += 1
                posiciones.append(index_sin_espacios)
            index_sin_espacios += 1  # solo aumentamos para caracteres válidos

    return contador, posiciones


def main():
    while True:
        try:
            frase = input("Ingresa una frase: ").strip()
            letra = input("Ingrese la letra que quiere contar: ").strip()
            contador, posiciones = contar_letra_en_frase(frase, letra)

            print(f"La letra '{letra}' aparece {contador} veces en la frase.")
            if contador > 0:
                print("Las posiciones donde aparece la letra son:", posiciones)
            break
        except ValueError as e:
            print("Error:", e)
            print("Intente de nuevo.\n")


if __name__ == '__main__':
    main()
