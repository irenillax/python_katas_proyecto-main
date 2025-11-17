# Lambda que calcula el cubo de un número
cubo = lambda x: x ** 3 


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", cubo(0))
    print("Caso 2:", cubo(2))
    print("Caso 3:", cubo(-3))
    print("Caso 4:", cubo(1.5))

