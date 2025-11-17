def palabras_que_contienen(palabras, objetivo):
    """
    Enunciado: Devuelve una lista con todas las palabras de 'palabras' que contienen 'objetivo' como subcadena.
    - Búsqueda insensible a mayúsculas/minúsculas.
    - 'palabras' puede ser cualquier iterable de strings.
    """
    objetivo = str(objetivo).lower().strip()
    return [p for p in palabras if objetivo in p.lower()]


# --- Prueba ---
if __name__ == "__main__":
    lista = ["Programación", "progreso", "Gato", "Microproceso", "Pro", "Prueba", "GO"]
    print("Objetivo: 'pro'")
    print(palabras_que_contienen(lista, "pro"))
    # Esperado (orden de entrada): ["Programación", "progreso", "Microproceso", "Pro"]
    
    print("Objetivo: 'go'")
    print(palabras_que_contienen(lista, "go"))
    # Esperado: ["Gato", "GO"] -> "go" está en "Gato" (ga**to** -> no, ojo: 'go' no está en 'Gato')
    # Corrección esperada: ["GO"] (porque 'go' no es subcadena de 'Gato')

