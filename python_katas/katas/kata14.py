def comienza_con(palabras, letra):
    """
   Enunciado: Devuelve las palabras que comienzan con 'letra'.
    - Comparación insensible a mayúsculas/minúsculas.
    - 'palabras' puede ser cualquier iterable de strings.
    """
    letra = str(letra).lower().strip()
    if len(letra) != 1:
        raise ValueError("La 'letra' debe ser un único carácter.")

    return list(filter(lambda w: str(w).lower().startswith(letra), palabras))


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", comienza_con(["Perro", "Pato", "gato", "pez", "Pájaro"], "p"))
    print("Caso 2:", comienza_con(["Sol", "Luna", "Silla", "sombra"], "S"))
    print("Caso 3:", comienza_con([], "a"))
    print("Caso 4:", comienza_con(["árbol", "avión", "Barco", "aMigo"], "a"))

