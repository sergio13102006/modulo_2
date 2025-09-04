def clasificador_num():
    numeros=[-5, 10, -15, 20, -25, 30]
    numeros_pares = [numero for numero in numeros if numero % 2 == 0]
    print(numeros_pares)
    numeros_impares = [numero for numero in numeros if numero % 2 != 0]
    print(numeros_impares)
    reporte_numeros = [f"El número {num} es Positivo" if num >= 0 else f"El número {num} es Negativo" for num in
                       numeros]
    for mensaje in reporte_numeros:
        print(mensaje)

def main():
    clasificador_num()


if __name__ == '__main__':
    main()