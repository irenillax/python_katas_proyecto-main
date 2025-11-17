def promedio_basico(numeros):
    """
    Enunciado: Devuelve la media aritmética de una lista de números.
    Lanza ValueError si la lista está vacía.
    """
    numeros = list(numeros)
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    return sum(numeros) / len(numeros)


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", promedio_basico([1, 2, 3, 4]))
    print("Caso 2:", promedio_basico([5]))
    print("Caso 3:", promedio_basico([10, -10, 10, -10]))
    try:
        print("Caso 4:", promedio_basico([]))
    except ValueError as e:
        print("Caso 4 (error):", e)
    print("Caso 5:", promedio_basico([1.5, 2.5, 3.0]))

