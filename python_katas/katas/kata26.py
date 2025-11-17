# Lambda que devuelve el resto de a dividido entre b
resto = lambda a, b: a % b 


# --- Prueba ---
if __name__ == "__main__":
    print("Caso 1:", resto(10, 3))     
    print("Caso 2:", resto(7, 7))     
    print("Caso 3:", resto(7, 2))      
    print("Caso 4:", resto(0, 5))      
    print("Caso 5:", resto(10, -3))    
    

