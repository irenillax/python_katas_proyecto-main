def contar_caracteres(cadena):
    """
    Enunciado: Devuelve el número total de caracteres de 'cadena'.
    Cuenta todo (incluye espacios y signos).
    """
    return len(cadena)


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", contar_caracteres("hola"))
    print("Caso 2:", contar_caracteres("hola mundo"))        
    print("Caso 3:", contar_caracteres(""))                  
    print("Caso 4:", contar_caracteres("¡Python 3.12!"))
    print("Caso 5:", contar_caracteres("áéíóú ñ ç"))

