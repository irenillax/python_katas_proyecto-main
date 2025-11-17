from functools import reduce

def digitos_a_numero(digitos):
    """
   Enunciado: Convierte una lista/iterable de dígitos (0-9) en el número entero correspondiente.
    Usa reduce().
    Ej.: [5,7,2] -> 572
    """


    return reduce(lambda acc, d: acc * 10 + d, digitos, 0)


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", digitos_a_numero([5, 7, 2]))
    print("Caso 2:", digitos_a_numero([0, 3, 4]))
    print("Caso 3:", digitos_a_numero([9]))
    print("Caso 4:", digitos_a_numero([]))          
    print("Caso 5:", digitos_a_numero([0, 0, 1]))   

