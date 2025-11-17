def puesto_de_empleado(nombre_completo, empleados):
    """
   Enunciado: Buscar 'nombre_completo' dentro de la lista 'empleados' y devuelve su 'puesto'.
    - No distingue mayúsculas/minúsculas.
    - Ignorar espacios extra al principio/fin del nombre.
    - Si no se encuentra, devuelve: "La persona no trabaja aquí."
    """
    objetivo = str(nombre_completo).strip().lower()

    for emp in empleados:
        nombre = str(emp.get("nombre", "")).strip().lower()
        if nombre == objetivo:
            return emp.get("puesto", None) 

    return "La persona no trabaja aquí."


# --- Prueba ---
if __name__ == "__main__":
    empleados = [
        {"nombre": "Alicia Pérez", "puesto": "Data Analyst"},
        {"nombre": "Bob Martín",   "puesto": "Backend Engineer"},
        {"nombre": "Marta López",  "puesto": "Product Manager"},
    ]

    print("Caso 1:", puesto_de_empleado("Alicia Pérez", empleados))
    print("Caso 2:", puesto_de_empleado("  bob martín ", empleados))   
    print("Caso 3:", puesto_de_empleado("MARTA LÓPEZ", empleados))     
    print("Caso 4:", puesto_de_empleado("Luis García", empleados))     
    print("Caso 5:", puesto_de_empleado("", empleados))                

