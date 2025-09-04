def contador_letras():
    frase = input("Ingresa una frase: ")
    letra = input("Ingrese la letra que quiere contar: ")
    contador = 0
    posiciones = []

    # Iteramos sobre la frase para contar la letra y registrar sus posiciones
    for i, caracter in enumerate(frase.replace(' ', '')):
        if caracter == letra:
            contador += 1
            posiciones.append(i)

    # Mostrar los resultados
    print(f"La letra '{letra}' aparece {contador} veces en la frase.")
    if contador > 0:
        print("Las posiciones donde aparece la letra son:", posiciones)


def main():
    contador_letras()


if __name__ == '__main__':
    main()
