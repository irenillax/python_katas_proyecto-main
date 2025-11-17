def frecuencia_letras(cadena: str) -> dict:
    """
    Función que cuenta la frecuencia de cada letra en una cadena.
    - Ignora los espacios.
    - No distingue entre mayúsculas y minúsculas.
    """

    # Pasamos todo a minúsculas para no diferenciar 'A' y 'a'
    cadena = cadena.lower()

    # Creamos un diccionario vacío donde guardaremos las frecuencias
    frecuencias = {}

    # Recorrido de cada carácter de la cadena 
    for letra in cadena:
        # Si la letra no es un espacio
        if letra != " ":
            # Añadimos 1 si ya existe, o la inicializamos en 1
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1

    # Resultado diccionario
    return frecuencias


# Ejemplo:
texto = "Soy Irene"
resultado = frecuencia_letras(texto)
print(resultado)