def media_y_estado(notas, nota_aprobado=5):
    """
    Calcula la media de una lista de notas y devuelve una tupla (media, estado).
    - Si la media >= nota_aprobado → "aprobado"
    - Si la media < nota_aprobado → "suspenso"
    """
    if not notas:  # Si la lista está vacía
        raise ValueError("La lista de notas no puede estar vacía.")

    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado


# --- Pruebas ---
if __name__ == "__main__":
    print("Caso 1:", media_y_estado([5, 6, 7, 8, 9]))
    print("Caso 2:", media_y_estado([3, 4, 5]))
