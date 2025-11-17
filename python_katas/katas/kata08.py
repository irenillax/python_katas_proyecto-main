def dividir_interactivo():
    """
    Enunciado: Pide dos números por teclado, intenta dividir e informa del resultado.
    Maneja:
      - ValueError: cuando el input no es numérico
      - ZeroDivisionError: cuando el denominador es 0
    """
    try:
        a = float(input("Introduce el numerador: "))
        b = float(input("Introduce el denominador: "))
        resultado = a / b
    except ValueError:
        print("Entrada sin valor numérico. Operación cancelada.")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    else:
        print(f"División correcta. Resultado: {resultado}")
    finally:
        print("Fin del programa.")
