# Lambda que comprueba si un número es impar
es_impar = lambda x: int(x) % 2 != 0  # noqa: E731

def filtrar_impares(lista):
    """
   Enunciado: Devuelve una nueva lista con solo los números impares usando filter() y la lambda 'es_impar'.
    Admite ints o flotantes que representen enteros (p.ej., 3.0).
    """
    return list(filter(es_impar, lista))


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", filtrar_impares([1, 2, 3, 4, 5]))
    print("Caso 2:", filtrar_impares([0, -1, -2, -3, 8, 11]))
    print("Caso 3:", filtrar_impares([]))
    print("Caso 4:", filtrar_impares([2, 4, 6, 8]))
    print("Caso 5:", filtrar_impares([3.0, 4.0, 7.0])) 

