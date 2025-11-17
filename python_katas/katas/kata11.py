def pedir_edad():
    """
    Enunciado: Pide al usuario su edad y valida:
      - Que sea un número entero.
      - Que esté entre 0 y 120.
    Maneja excepciones y muestra mensajes claros.
    """
    try:
        edad = int(input("Introduce tu edad: "))

        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera del rango permitido (0–120).")

        print(f"Edad válida: {edad}")
        return edad

    except ValueError as e:
        print(f"Error: {e}")
        return None
    finally:
        print("Fin validación de edad.")


# --- Ejecución ---
if __name__ == "__main__":
    pedir_edad()

