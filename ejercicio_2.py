import time
def menu():
    opcion = 0

    """
        Pide al usuario que ingrese una de las tres opciones y hace la simulacion de cada una
        :param opcion: almacena el numero de la opcion que desea el usuario
    """
    while True:
        print("Por favor escriba el numero correspondiente a la opción que desees:   MENÚ\n1 Guardar\n2 Cargar\n3 salir ")
        try:
            opcion = int(input(f"Digite una opcion:"))
        except ValueError:
            print(f'debe escribir un numero valido, sin espacios, ni letras')
            continue
        match opcion:
            case 1:
                print(f"Guardando archivo...")
                time.sleep(2)
                print("guardado con exíto")

            case 2:
                print(f"Cagando...")
                time.sleep(2)
                print("Cargado con exito")

            case 3:
                print(f"Saliendo del programa")
                time.sleep(2)
                print("Gracias por utilizar el programa")
                break


if __name__ == "__main__":
    menu()