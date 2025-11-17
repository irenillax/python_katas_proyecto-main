def primer_duplicado(valores):
    """
    Enunciado: Recorre la lista en orden y devuelve el primer elemento que ya se había visto.
    Si no hay duplicados, devuelve None.
    """
    vistos = set()
    for v in valores:
        if v in vistos:
            return v
        vistos.add(v)
    return None


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", primer_duplicado([1, 2, 3, 2, 4, 3]))
    print("Caso 2:", primer_duplicado(["a", "b", "c", "a"]))
    print("Caso 3:", primer_duplicado([True, False, True, False]))
    print("Caso 4:", primer_duplicado([]))
    print("Caso 5:", primer_duplicado([1, 2, 3, 4]))
    print("Caso 6:", primer_duplicado(["x", "y", "y", "x"]))

