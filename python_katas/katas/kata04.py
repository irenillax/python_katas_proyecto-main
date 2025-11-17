def diferencia_listas(a, b):
    """
    Enunciado: Calcula la diferencia elemento a elemento entre dos listas (a_i - b_i).
    - Si las listas tienen distinta longitud, se usa la mínima (zip).
    - Usa map() para aplicar la resta a cada par.
    """
    return list(map(lambda par: par[0] - par[1], zip(a, b)))


# --- Prueba ---
if __name__ == "__main__":
    l1 = [10, 20, 30, 40]
    l2 = [1, 2, 3, 4]
    print("Caso 1:", diferencia_listas(l1, l2))  # [9, 18, 27, 36]

    # Longitudes distintas: recorte hacia la más corta
    l3 = [5, 7, 9]
    l4 = [1, 2]
    print("Caso 2:", diferencia_listas(l3, l4))  # [4, 5]

    # Con flotantes y negativos
    l5 = [1.5, -2.0, 0]
    l6 = [0.5, 3.0, -1]
    print("Caso 3:", diferencia_listas(l5, l6))  # [1.0, -5.0, 1]

