class ListaVaciaError(Exception):
    """Excepción personalizada para listas vacías al calcular el promedio."""
    pass


def promedio(numeros):
    """
   Enunciado: Calcula el promedio de una lista de números.
    - Lanza ListaVaciaError si la lista está vacía.
    """
    numeros = list(numeros)  # por si pasan un iterable
    if not numeros:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")
    return sum(numeros) / len(numeros)


# --- Pruebas rápidas / demostración de manejo ---
if __name__ == "__main__":
    # Caso 1: lista normal
    try:
        print("Caso 1:", promedio([10, 20, 30]))
    except ListaVaciaError as e:
        print("Caso 1 (error):", e)

    # Caso 2: lista con un solo elemento
    try:
        print("Caso 2:", promedio([7]))
    except ListaVaciaError as e:
        print("Caso 2 (error):", e)

    # Caso 3: lista vacía (dispara la excepción personalizada)
    try:
        print("Caso 3:", promedio([]))
    except ListaVaciaError as e:
        print("Caso 3 (error):", e)

