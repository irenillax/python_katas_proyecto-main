def precio_final_con_descuento():
    try:
        precio = float(input("Precio original (€): ").strip())
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        tiene_cupon = input("¿Tienes cupón de descuento? (sí/no): ").strip().lower()
        descuento = 0.0

        if tiene_cupon in ("sí", "si", "s"):
            valor = float(input("Valor del cupón (€): ").strip())
            if valor > 0:
                descuento = valor
            else:
                print("Cupón no válido (<= 0). No se aplica descuento.")
        elif tiene_cupon in ("no", "n"):
            pass
        else:
            print("Respuesta no reconocida. Se asume que no hay cupón.")

        final = max(precio - descuento, 0.0)
        print(f"Precio final: {final:.2f} €")

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    precio_final_con_descuento()

