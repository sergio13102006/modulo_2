def pedir_entero(mensaje: str, minimo: int = 1) -> int:
    """
    Pide un número entero al usuario con validación.
    :param mensaje: Texto que se muestra al usuario.
    :param minimo: Valor mínimo permitido.
    :return: Número entero válido.
    """
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: No se puede dejar vacío. Intente de nuevo.")
            continue
        if not valor.isdigit():
            print("Error: Debe ingresar un número entero positivo. Intente de nuevo.")
            continue
        entero = int(valor)
        if entero < minimo:
            print(f"Error: El número debe ser mayor o igual a {minimo}.")
            continue
        return entero


def pedir_nombre_estudiante(nombres_existentes: list) -> str:
    """
    Pide el nombre de un estudiante y evita duplicados o nombres vacíos.
    """
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            continue
        if any(c.isdigit() or c in "@#$/%&*!" for c in nombre):
            print("Error: El nombre no puede contener números ni caracteres especiales.")
            continue
        if nombre in nombres_existentes:
            print(f"Error: El nombre '{nombre}' ya fue ingresado. Ingrese otro.")
            continue
        return nombre


def pedir_nota(mensaje: str, minimo: float = 0.0, maximo: float = 5.0) -> float:
    """
    Pide una nota con validación de rango y número válido.
    """
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: No se puede dejar vacío. Intente de nuevo.")
            continue
        try:
            nota = float(valor)
            if nota < minimo or nota > maximo:
                print(f"Error: La nota debe estar entre {minimo} y {maximo}.")
                continue
            return nota
        except ValueError:
            print("Error: Debe ingresar un número válido (decimal permitido).")


def contador_notas():
    """
    Función principal para contar notas y estudiantes con validación completa.
    """
    print("=== Registro de notas de estudiantes ===")
    n_notas = pedir_entero("Ingrese el número de notas por estudiante: ")
    n_estudiantes = pedir_entero("Ingrese el número de estudiantes: ")

    nombres_estudiantes = []

    for i in range(n_estudiantes):
        print(f"\n--- Estudiante {i+1} ---")
        nombre = pedir_nombre_estudiante(nombres_estudiantes)
        nombres_estudiantes.append(nombre)

        notas_estudiante = []
        for j in range(n_notas):
            nota = pedir_nota(f"Ingrese la nota {j+1} de {nombre}: ")
            notas_estudiante.append(nota)

        print(f"Notas registradas de {nombre}: {notas_estudiante}")
        print("-" * 40)


def main():
    contador_notas()


if __name__ == "__main__":
    main()
