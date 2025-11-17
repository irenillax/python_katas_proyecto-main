def momento_del_dia(hora: int) -> str:
    """
    Enunciado: Devuelve 'día', 'tarde' o 'noche' según la hora (0-23).
    Definición:
      - día:   06-11
      - tarde: 12-19
      - noche: 20-23 y 00-05
    """
    if not isinstance(hora, int) or hora < 0 or hora > 23:
        raise ValueError("La hora debe ser un entero entre 0 y 23.")
    if 6 <= hora <= 11:
        return "día"
    elif 12 <= hora <= 19:
        return "tarde"
    else:
        return "noche"


if __name__ == "__main__":
    # Modo interactivo
    try:
        h = int(input("Introduce la hora (0-23): "))
        print("Es de", momento_del_dia(h))
    except ValueError as e:
        print("Error:", e)

