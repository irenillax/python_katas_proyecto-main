from functools import reduce

def producto(numeros):
    """
   Enunciado: Devuelve el producto de todos los elementos de 'numeros'.
    - Usa reduce() con acumulador inicial 1.
    - Por convenio, lista vacía -> 1 (elemento neutro de la multiplicación).
    """
    return reduce(lambda a, b: a * b, numeros, 1)


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", producto([1, 2, 3, 4]))
    print("Caso 2:", producto([5]))
    print("Caso 3:", producto([]))           
    print("Caso 4:", producto([2, -3, 4]))    
    print("Caso 5:", producto([1.5, 2]))     
    print("Caso 6:", producto([0, 7, 8]))     

