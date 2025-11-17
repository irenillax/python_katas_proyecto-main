# Lambda que suma 3 a un número
sumar_tres = lambda x: x + 3 

def aplicar_suma_tres(lista):
    """
   Enunciado: Aplica la lambda 'sumar_tres' a cada elemento de la lista usando map().
    Devuelve una nueva lista.
    """
    return list(map(sumar_tres, lista))


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", aplicar_suma_tres([1, 2, 3]))
    print("Caso 2:", aplicar_suma_tres([0, -1, 10.5]))
    print("Caso 3:", aplicar_suma_tres([]))