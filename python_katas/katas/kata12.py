def longitudes_palabras(frase):
    """
    Enunciado: Recibe una frase y devuelve una lista con la longitud de cada palabra.
    Usa la función map().
    """
    # 1️⃣ Dividimos la frase por espacios -> lista de palabras
    palabras = frase.split()

    # 2️⃣ Aplicamos len() a cada palabra usando map
    longitudes = list(map(len, palabras))

    return longitudes


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", longitudes_palabras("Hola mundo"))
    print("Caso 2:", longitudes_palabras("Python es divertido"))
    print("Caso 3:", longitudes_palabras("Esto   tiene   espacios   dobles"))
    print("Caso 4:", longitudes_palabras(""))  # Frase vacía
