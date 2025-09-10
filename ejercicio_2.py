import time

def pedir_opcion(input_func=input):
    while True:
        # no pasar argumentos, solo llamar
        entrada = input_func().strip()

        if entrada == "":
            print("No puede dejar el campo vacío.")
            continue

        if not entrada.isdigit():
            print("Debe digitar solo números enteros")
            continue

        opcion = int(entrada)

        if opcion < 0:
            print("No se permiten números negativos.")
            continue

        if opcion not in [1, 2, 3]:
            print("Opción fuera de rango")
            continue

        return opcion


def menu(input_func=input):
    while True:
        print("\nPor favor escriba el número correspondiente a la opción que desees: MENÚ")
        print("1 Guardar\n2 Cargar\n3 Salir")

        opcion = pedir_opcion(input_func)

        match opcion:
            case 1:
                print("Guardando archivo...")
                time.sleep(1)
                print("Guardado con éxito")

            case 2:
                print("Cargando...")
                time.sleep(1)
                print("Cargado con éxito")

            case 3:
                print("Saliendo del programa...")
                time.sleep(1)
                print("Gracias por utilizar el programa")
                break


if __name__ == "__main__":
    menu()
