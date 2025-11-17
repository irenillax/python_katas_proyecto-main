def factorial(n):
    """
    Enunciado: Calcula el factorial de un número entero de forma recursiva.
    - Si n es 0 o 1 → devuelve 1
    - Si n < 0 → lanza un error
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        # Llamada recursiva: n! = n * (n-1)!
        return n * factorial(n - 1)


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", factorial(0))   # Esperado: 1
    print("Caso 2:", factorial(1))   # Esperado: 1
    print("Caso 3:", factorial(3))   # Esperado: 6
    print("Caso 4:", factorial(5))   # Esperado: 120

