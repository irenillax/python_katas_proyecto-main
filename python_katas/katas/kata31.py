def buscar_nombre_interactivo():
    # Pedimos la lista de nombres separados por comas
    texto = input("Introduce nombres separados por comas: ")
    lista = texto.split(",")
    nombres = []

    # Limpiamos espacios
    for n in lista:
        nombres.append(n.strip())

    # Pedimos el nombre a buscar
    nombre = input("Introduce el nombre a buscar: ")

    try:
        if nombre in nombres:
            print("El nombre está en la lista.")
        else:
            raise LookupError("El nombre no está en la lista.")
    except LookupError as e:
        print(e)


if __name__ == "__main__":
    buscar_nombre_interactivo()
