from functools import reduce

def diferencia_total(numeros):
    """
    Enunciado: Aplica la resta encadenada: (((n1 - n2) - n3) - ...).
    - []      -> 0
    - [x]     -> x
    - [x, y]  -> x - y
    """
    nums = list(numeros)
    if not nums:
        return 0
    # reducir sin valor inicial empieza en [0] y aplica con lo demas
    return reduce(lambda a, b: a - b, nums)


# --- Pruebas  ---
if __name__ == "__main__":
    print("Caso 1:", diferencia_total([10, 2, 3]))     
    print("Caso 2:", diferencia_total([5]))           
    print("Caso 3:", diferencia_total([]))            
    print("Caso 4:", diferencia_total([20, 5, -5]))    
    print("Caso 5:", diferencia_total([1.5, 0.5, 0.5]))

