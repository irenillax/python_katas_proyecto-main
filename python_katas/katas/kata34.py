class Arbol:
    def __init__(self):
        """Inicializa con tronco=1 y sin ramas."""
        self.tronco = 1
        self.ramas = []

    # 2) Aumentar la longitud del tronco en 1
    def crecer_tronco(self):
        self.tronco += 1

    # 3) Agregar una nueva rama de longitud 1
    def nueva_rama(self):
        self.ramas.append(1)

    # 4) Aumentar en 1 todas las ramas existentes
    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]

    # 5) Eliminar una rama por posición (1-based)
    def quitar_rama(self, posicion: int):
        """
        Elimina la rama en 'posicion' (1-based).
        Lanza IndexError si la posición no existe.
        """
        if posicion < 1 or posicion > len(self.ramas):
            raise IndexError("Posición de rama no válida.")
        self.ramas.pop(posicion - 1)

    # 6) Devolver informacion del árbol
    def info_arbol(self):
        """
        Devuelve un diccionario con:
        - tronco: longitud del tronco
        - numero_ramas: total de ramas
        - longitudes_ramas: lista de longitudes de ramas
        """
        return {
            "tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": list(self.ramas),
        }


# ---- Caso (a modo de ejemplo) ----
if __name__ == "__main__":
    arbol = Arbol()                 

    arbol.crecer_tronco()           
    arbol.nueva_rama()              
    arbol.crecer_ramas()            
    arbol.nueva_rama()              
    arbol.nueva_rama()             
    arbol.quitar_rama(2)            

    print(arbol.info_arbol())      


