productos = [
    {"nombre": "Camisa", "precio": 50000},
    {"nombre": "Pantalón", "precio": 80000},
    {"nombre": "Zapatos", "precio": 120000}
]

# Usamos una dictionary comprehension para crear el nuevo diccionario.
precios_con_iva = {producto["nombre"]: producto["precio"] * 1.19 for producto in productos}

print(precios_con_iva)