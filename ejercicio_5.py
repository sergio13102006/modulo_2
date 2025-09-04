def calcular_par_impar():
    while True:
        try:
            num = int(input("Ingrese un número: "))

            # Validación de número negativo
            if num < 0:
                print("Error: El número no puede ser negativo. Intente de nuevo.")
                continue  # Vuelve al inicio del bucle

            es_par = num % 2 == 0
            es_multiplo_de_5 = num % 5 == 0

            if es_par and es_multiplo_de_5:
                print(f"El número {num} es par y también es múltiplo de 5.")
            elif es_par:
                print(f"El número {num} es par, pero no es múltiplo de 5.")
            elif es_multiplo_de_5:
                print(f"El número {num} es múltiplo de 5, pero no es par.")
            else:
                print(f"El número {num} no es par ni múltiplo de 5.")

            break  # Sale del bucle si el input es un número no negativo.

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")


def main():
    calcular_par_impar()


if __name__ == '__main__':
    main()