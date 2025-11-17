def calificacion_texto(nota: float) -> str:
    """
    Enunciado: Devuelve el texto de la calificación:
      0-69   -> insuficiente
      70-79  -> bien
      80-89  -> muy bien
      90-100 -> excelente
    Lanza error si está fuera de [0, 100].
    """
    n = float(nota)
    if n < 0 or n > 100:
        raise ValueError("La nota debe estar entre 0 y 100.")
    if n <= 69:
        return "insuficiente"
    elif n <= 79:
        return "bien"
    elif n <= 89:
        return "muy bien"
    else:
        return "excelente"


if __name__ == "__main__":
    print("Caso 1:", calificacion_texto(0))
    print("Caso 2:", calificacion_texto(75))
    print("Caso 3:", calificacion_texto(85))
    print("Caso 4:", calificacion_texto(95))
    try:
        print("Caso 5:", calificacion_texto(120))
    except ValueError as e:
        print("Caso 5 (error):", e)

