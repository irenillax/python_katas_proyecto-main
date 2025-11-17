def doblar_lista(numeros):
    """
    Enunciado: Devuelve una nueva lista con el doble de cada número usando map().
    - numeros: iterable de enteros o flotantes.
    """
    # map aplica la lambda x: x*2 a cada elemento de 'numeros'
    return list(map(lambda x: x * 2, numeros))


# --- Prueba ---
if __name__ == "__main__":
    datos = [1, 2, 3.5, -4, 0]
    print("Entrada :", datos)
    print("Salida  :", doblar_lista(datos))
    # Esperado: [2, 4, 7.0, -8, 0]

