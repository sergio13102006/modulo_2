def contador_notas():
    try:
        # Pide el número de notas y estudiantes y los valida.
        n_notas = int(input("Ingrese el número de notas: "))
        n_estudiantes = int(input("Ingrese el número de estudiantes: "))

        # Bucle for para iterar sobre el número de estudiantes
        for i in range(n_estudiantes):
            # Pide el nombre del estudiante
            nombre_estudiante = input(f"Ingrese el nombre del estudiante {i+1}: ")

            print(f"--- Ingrese las notas de {nombre_estudiante} ---")

            # Bucle for anidado para iterar sobre el número de notas por estudiante
            for j in range(n_notas):
                try:
                    nota = float(input(f"Ingrese la nota {j+1}: "))
                    # Aquí podrías guardar o procesar la nota
                    print(f"Nota {j+1} de {nombre_estudiante}: {nota}")
                except ValueError:
                    print("El valor ingresado no es válido. Por favor, ingrese un número.")
            print("-" * 30)

    except ValueError:
        print("El número de notas o estudiantes no es válido. Por favor, ingrese números enteros.")

def main():
    contador_notas()

if __name__ == '__main__':
    main()