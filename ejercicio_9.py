def calcular_precios_con_iva(productos, iva=0.19):
    """
    Calcula los precios de los productos incluyendo IVA.

    :param productos: Lista de diccionarios con "nombre" y "precio".
    :param iva: Porcentaje de IVA (por defecto 19% = 0.19)
    :return: Diccionario con el nombre del producto como clave y precio con IVA como valor.
    """
    precios_con_iva = {
        producto["nombre"]: round(producto["precio"] * (1 + iva), 2)
        for producto in productos
    }
    return precios_con_iva


def main():
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000}
    ]

    precios = calcular_precios_con_iva(productos)

    print("=== Precios con IVA incluido ===")
    for nombre, precio in precios.items():
        print(f"{nombre}: {precio}")


if __name__ == "__main__":
    main()
