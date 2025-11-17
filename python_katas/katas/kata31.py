def buscar_nombre_interactivo():
    try:
        nombres = input("Introduce nombres separados por comas: ")
        lista = [n.strip().lower() for n in nombres.split(",")]

        nombre = input("Nombre a buscar: ").strip().lower()

        if nombre in lista:
            print("Nombre encontrado")
        else:
            raise LookupError("El nombre no está en la lista")

    except LookupError as e:
        print(e)


if __name__ == "__main__":
    #Prueba
    buscar_nombre_interactivo()