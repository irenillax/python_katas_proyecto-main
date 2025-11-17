def enmascarar(valor):
    """
    Enunciado: Devuelve una versión enmascarada de 'valor' (convertido a str),
    reemplazando todos los caracteres por '#' excepto los últimos 4.
    """
    s = str(valor)
    if len(s) <= 4:
        return s
    return "#" * (len(s) - 4) + s[-4:]


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", enmascarar("123456789"))
    print("Caso 2:", enmascarar("abcd"))
    print("Caso 3:", enmascarar("abc"))
    print("Caso 4:", enmascarar(987654321))
    print("Caso 5:", enmascarar("****-****-****-1234"))
    print("Caso 6:", enmascarar(""))                
    print("Caso 7:", enmascarar("a b c d e f"))    

