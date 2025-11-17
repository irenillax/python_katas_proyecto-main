def solo_enteros(valores):
    """
    Enunciado: Devuelve una lista con solo los enteros puros (int) de 'valores'.
    Excluye bool (True/False), aunque heredan de int.
    """
    return list(filter(lambda v: isinstance(v, int) and not isinstance(v, bool), valores))


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", solo_enteros([1, "2", 3, "cuatro", 5]))
    print("Caso 2:", solo_enteros([True, False, 0, 1, 2, "3"]))
    print("Caso 3:", solo_enteros(["a", "b", "c"]))
    print("Caso 4:", solo_enteros([10, -7, 3.0, 4.5, 8]))
    print("Caso 5:", solo_enteros([]))

