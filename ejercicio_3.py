def validar_contasena():
    """
    verifica que la contraseña cumpla con todos los requisitos
    :return:
    """
    contrasena = ""
    con = ''

    while not (len(con) >= 8 and any(char.isupper() for char in con) and any(
            char.isdigit() for char in con)):
        contrasena = str(input("Define tu contraseña: "))
        con = contrasena

        if len(con) < 8:
            validacion8 = "✖️"
        else:
            validacion8 = "✔️"

        if not any(c.isupper() for c in con):
            validacionMayus = "✖️"
        else:
            validacionMayus = "✔️"

        if not any(c.isdigit() for c in con):
            validacionnum = "✖️"
        else:
            validacionnum = "✔️"

        # You also need to define validacionEspacio. I've added a check for it.
        if " " in contrasena:
            validacionEspacio = "✖️"
        else:
            validacionEspacio = "✔️"

        print(
            f"{validacion8}Mínimo 8 caracteres de longitud: \n"
            f"{validacionMayus}Contiene al menos una letra mayúscula: \n"
            f"{validacionnum}Contiene al menos un número: \n"
            f"{validacionEspacio}No debe contener espacios: "
        )
    print(f"Su contraseña ha sido exitosamente guardada. ✔️")
if __name__ == "__main__":
    validar_contasena()