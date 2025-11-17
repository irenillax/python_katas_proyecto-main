import math
from typing import Tuple

def area(figura: str, datos: Tuple[float, ...]) -> float:
    """
    Enunciado: Calcula el área según 'figura' y 'datos':
      - "rectangulo": (base, altura)  -> base * altura
      - "triangulo":  (base, altura)  -> base * altura / 2
      - "circulo":    (radio,)        -> pi * r^2
    """
    f = figura.strip().lower()
    if f == "rectangulo":
        if len(datos) != 2: raise ValueError("rectangulo requiere (base, altura)")
        base, altura = datos
        return base * altura
    elif f == "triangulo":
        if len(datos) != 2: raise ValueError("triangulo requiere (base, altura)")
        base, altura = datos
        return base * altura / 2
    elif f == "circulo":
        if len(datos) != 1: raise ValueError("circulo requiere (radio,)")
        (r,) = datos
        return math.pi * (r ** 2)
    else:
        raise ValueError("Figura no válida: usa rectangulo | triangulo | circulo")


if __name__ == "__main__":
    print("Rectángulo 3x4:", area("rectangulo", (3, 4)))
    print("Triángulo 10x2:", area("triangulo", (10, 2)))
    print("Círculo r=3:", round(area("circulo", (3,)), 5))

