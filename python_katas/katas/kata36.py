class UsuarioBanco:
    def __init__(self, nombre: str, saldo: float, cuenta_corriente: bool):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def __repr__(self):
        return f"UsuarioBanco(nombre={self.nombre!r}, saldo={self.saldo:.2f}, cuenta_corriente={self.cuenta_corriente})"

    def retirar_dinero(self, cantidad: float):
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene cuenta corriente operativa.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        if self.saldo < cantidad:
            raise ValueError(f"Saldo insuficiente. Disponible: {self.saldo:.2f}")
        
        self.saldo -= cantidad
        return self.saldo

    def agregar_dinero(self, cantidad: float):
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene cuenta corriente operativa.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        
        self.saldo += cantidad
        return self.saldo

    def transferir_dinero(self, origen, cantidad: float):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        if not origen.cuenta_corriente:
            raise ValueError(f"{origen.nombre} no tiene cuenta corriente operativa.")
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene cuenta corriente operativa.")
        if origen.saldo < cantidad:
            raise ValueError(f"Saldo insuficiente en {origen.nombre}.")
        
        origen.saldo -= cantidad
        self.saldo += cantidad
        return (origen.saldo, self.saldo)
