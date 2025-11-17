def palabras_mas_largas_que(palabras, n):
    """
   Enunciado: Devuelve las palabras cuya longitud es > n.
    Usa filter().
    """
    if not isinstance(n, int):
        raise TypeError("n debe ser un entero.")
    return list(filter(lambda w: len(str(w)) > n, palabras))


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", palabras_mas_largas_que(["hola", "adiós", "sol", "programación"], 3))
    print("Caso 2:", palabras_mas_largas_que(["a", "bb", "ccc", "dddd"], 2))
    print("Caso 3:", palabras_mas_largas_que([], 5))
    print("Caso 4:", palabras_mas_largas_que(["  trim  ", "ok", "sí"], 4)) 
    print("Caso 5:", palabras_mas_largas_que(["uno", "dos", "tres"], 0))

