def tuplas_a_strings(tuplas):
    """
   Enunciado: Convierte una lista/iterable de tuplas en una lista de strings usando map().
    Cada tupla se transforma con str(tupla).
    """
    return list(map(lambda t: str(t), tuplas))


# --- Pruebas ---
if __name__ == "__main__":
    datos1 = [(1, 2), (3, 4, 5), ("a", "b")]
    print("Caso 1:", tuplas_a_strings(datos1))

    datos2 = []
    print("Caso 2:", tuplas_a_strings(datos2))

    datos3 = [(True, False), (None,), (3.14, "x")]
    print("Caso 3:", tuplas_a_strings(datos3))

