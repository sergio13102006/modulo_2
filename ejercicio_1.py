def definir_precio(edad):
    """
    esta función define el precio de la boleta dependiendo la edad.
    :param edad: recibe la edad del usuario.
    :return: retorna el precion ya definido en la función
    """
    precio = 0
    if 0 < edad <= 80:
        if 0 <= edad <= 12:
            precio = 10000
        elif 12 < edad <= 18:
            precio = 15000
        else:
            precio = 20000
        return precio
    elif edad > 80:
        print("Tienes una superedad!!")
    else:
        print("No escribiste correctamente tu edad.")
    return None

def definir_descuento(es_estudiante, precio):
    """
    define si la persona tiene o no descuento
    :param es_estudiante:recibe si es estudiante o no
    :param precio: guarda el precio de la boleta dependiendo la edad
    """
    if es_estudiante == 1:
        descuento = precio * 0.1
        precio_total = precio - descuento
        print(f"El costo de tu entrada es de ${precio},")
        print(f"con el descuento de estudiante queda en ${precio_total}.")
    elif es_estudiante == 0:
        print(f"El costo de tu entrada es de ${precio}.")
        print("Ten en cuenta que no se aplicó el descuento de estudiante.")
    else:
        print("Opción no válida. Debes escribir 1 si eres estudiante o 0 si no lo eres.")
def main():
    """
    depura el codigo
    """
    edad_str = input("Escribe en números ¿cuál es tu edad? ")
    try:
        edad = float(edad_str)
        precio = definir_precio(edad)
        if precio is not None:
            es_estudiante_str = input("Escribe el número 1 si eres estudiante\nescribe el número 0 si no eres estudiante:\n")
            try:
                es_estudiante = int(es_estudiante_str)
                definir_descuento(es_estudiante, precio)
            except ValueError:
                print("Entrada no válida para la opción de estudiante. Por favor, ingresa 1 o 0.")
    except ValueError:
        print("Entrada no válida para la edad. Por favor, ingresa un número.")

if __name__ == "__main__":
    main()