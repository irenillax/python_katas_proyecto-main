def estudiantes_sobresalientes(estudiantes):
    """
    Enunciado: Recibe una lista de diccionarios con claves:
      - 'nombre' (str), 'edad' (int/float), 'calificacion' (int/float)
    Devuelve solo los estudiantes con calificación >= 90.
    """
    return list(filter(lambda e: float(e.get("calificacion", 0)) >= 90, estudiantes))


# --- Prueba ---
if __name__ == "__main__":
    alumnos = [
        {"nombre": "Ana",   "edad": 20, "calificacion": 95},
        {"nombre": "Luis",  "edad": 22, "calificacion": 88},
        {"nombre": "Marta", "edad": 19, "calificacion": 90},
        {"nombre": "Javi",  "edad": 21, "calificacion": 72},
        {"nombre": "Iris",  "edad": 23, "calificacion": 99.5},
        {"nombre": "Tom",   "edad": 20, "calificacion": "89"}, 
        {"nombre": "Eva",   "edad": 20, "calificacion": "90"},   
    ]

    resultado = estudiantes_sobresalientes(alumnos)
    print("Sobresalientes:", resultado)

