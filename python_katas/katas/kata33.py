# Lambda que suma dos números
suma = lambda x, y: x + y  # noqa: E731

def sumar_listas(a, b):
    """
   Enunciado: Devuelve una nueva lista con la suma elemento a elemento de 'a' y 'b'.
    Usa map() + zip(). Se recorta a la longitud de la lista más corta.
    """
    return list(map(lambda par: suma(par[0], par[1]), zip(a, b)))


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", sumar_listas([1, 2, 3], [4, 5, 6]))
    print("Caso 2:", sumar_listas([10, -2, 0], [1, 1, 1]))
    print("Caso 3:", sumar_listas([1.5, 2.5], [0.5, 1.0]))
    print("Caso 4:", sumar_listas([], [7, 8]))
    print("Caso 5:", sumar_listas([1, 2, 3, 4], [10, 20]))  

