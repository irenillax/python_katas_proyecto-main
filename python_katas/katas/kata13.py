def mayus_minus_unicas(texto):
    """
    Enunciado: Recibe un texto y devuelve una lista de tuplas (Mayúscula, minúscula)
    sin repetir letras.
    - Usa map() para generar las tuplas.
    - Solo considera caracteres alfabéticos (letras).
    """
    # Eliminar duplicados manteniendo el orden
    letras_unicas = []
    for c in texto:
        if c.isalpha() and c not in letras_unicas:
            letras_unicas.append(c)

    # Aplicar map() para crear las tuplas (mayúscula, minúscula)
    resultado = list(map(lambda x: (x.upper(), x.lower()), letras_unicas))
    return resultado


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", mayus_minus_unicas("Hola Mundo"))
    print("Caso 2:", mayus_minus_unicas("Python"))
    print("Caso 3:", mayus_minus_unicas("AaBbCc"))
    print("Caso 4:", mayus_minus_unicas("123 @@@!!!"))  # No hay letras