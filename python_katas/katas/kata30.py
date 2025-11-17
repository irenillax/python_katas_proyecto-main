def son_anagramas(a, b):
    """
    Enunciado: Devuelve True si 'a' y 'b' son anagramas:
    - Compara SOLO letras (isalpha), ignora espacios y signos.
    - No distingue mayúsculas/minúsculas.
    """
    def limpiar(s):
        return sorted(ch.lower() for ch in s if ch.isalpha())

    return limpiar(a) == limpiar(b)


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", son_anagramas("Roma", "amor"))                 
    print("Caso 2:", son_anagramas("Listen", "Silent"))             
    print("Caso 3:", son_anagramas("Árbol", "Lób ar"))              
    print("Caso 4:", son_anagramas("Hola", "Halo"))                 
    print("Caso 5:", son_anagramas("Aaa", "aa"))                    
    print("Caso 6:", son_anagramas("A gentleman", "Elegant man"))   
    print("Caso 7:", son_anagramas("123", "321"))                   

