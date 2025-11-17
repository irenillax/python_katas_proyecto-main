def contar_palabras(texto):
    palabras = texto.lower().split()
    contador = {}

    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return contador


def reemplazar_palabra(texto, original, nueva):
    return texto.replace(original, nueva)


def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    filtradas = []

    for p in palabras:
        if p != palabra:
            filtradas.append(p)

    return " ".join(filtradas)


def procesar_texto(texto, opcion, original="", nueva=""):
    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        return reemplazar_palabra(texto, original, nueva)

    elif opcion == "eliminar":
        return eliminar_palabra(texto, original)

    else:
        return "Opción no válida"
    

if __name__ == "__main__":
    texto = "hola mundo hola adios mundo"

    print("Texto original:")
    print(texto)

    # Opción: contar
    print("\nResultado opción 'contar':")
    print(procesar_texto(texto, "contar"))

    # Opción: reemplazar
    print("\nResultado opción 'reemplazar' (mundo -> Python):")
    print(procesar_texto(texto, "reemplazar", "mundo", "Python"))

    # Opción: eliminar
    print("\nResultado opción 'eliminar' (hola):")
    print(procesar_texto(texto, "eliminar", "hola"))