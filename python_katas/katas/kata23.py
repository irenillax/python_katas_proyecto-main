from functools import reduce

def concatenar_palabras(palabras):
    """
    Enunciado: Concatena todas las palabras de la lista en un solo string.
    - Usa reduce() con acumulador inicial "".
    - No añade espacios automáticamente (concatenación directa).
    """
    return reduce(lambda a, b: a + b, palabras, "")


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", concatenar_palabras(["Hola", " ", "Irene"]))
    print("Caso 2:", concatenar_palabras(["Pe", "ri", "me", "tro"]))
    print("Caso 3:", concatenar_palabras([]))                 
    print("Caso 4:", concatenar_palabras(["a", "", "b", ""])) 

