PROHIBIDAS_ES = {"mapache", "tigre", "serpiente pitón", "cocodrilo", "oso"}

def filtrar_mascotas_legales(mascotas):
    """
    Enunciado: Devuelve una lista con las mascotas NO prohibidas en España.
    - Comparación insensible a mayúsculas/minúsculas.
    - Coincidencia exacta por nombre (no hace búsqueda parcial).
    """
    return list(filter(lambda m: m.strip().lower() not in PROHIBIDAS_ES, mascotas))


# --- Prueba ---
if __name__ == "__main__":
    caso1 = ["Perro", "Gato", "Tigre", "Canario", "Cocodrilo", "mapache", "Serpiente Pitón", "Hámster"]
    print("Caso 1:", filtrar_mascotas_legales(caso1))

    caso2 = ["OSO", "GATO", "SERPIENTE PITÓN", "Loro"]
    print("Caso 2:", filtrar_mascotas_legales(caso2))

    caso3 = []  # Lista vacía
    print("Caso 3:", filtrar_mascotas_legales(caso3))

    # Comprobacion de que no es búsqueda parcial:
    caso4 = ["Oso hormiguero", "Tigresa", "Serpiente", "Pitón"]  # Ninguna coincide exactamente con las prohibidas
    print("Caso 4:", filtrar_mascotas_legales(caso4))

