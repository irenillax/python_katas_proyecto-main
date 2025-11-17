class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente=True):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def __repr__(self):
        return f"UsuarioBanco(nombre={self.nombre}, saldo={self.saldo}, cuenta_corriente={self.cuenta_corriente})"

    def retirar_dinero(self, cantidad):
        if not self.cuenta_corriente:
            raise ValueError("Cuenta no operativa")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")

        self.saldo -= cantidad
        return self.saldo

    def agregar_dinero(self, cantidad):
        if not self.cuenta_corriente:
            raise ValueError("Cuenta no operativa")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        self.saldo += cantidad
        return self.saldo

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        if not self.cuenta_corriente:
            raise ValueError("Tu cuenta no está operativa")

        if not otro_usuario.cuenta_corriente:
            raise ValueError("La cuenta del destinatario no está operativa")

        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")

        self.saldo -= cantidad
        otro_usuario.saldo += cantidad

        return self.saldo, otro_usuario.saldo


if __name__ == "__main__":
    # dos usuarios de ejemplo
    alicia = UsuarioBanco("Alicia", 100.0, True)
    bob = UsuarioBanco("Bob", 50.0, True)

    print("Estado inicial:")
    print(alicia)
    print(bob)

    # Alicia retira 20
    alicia.retirar_dinero(20.0)
    print("\nAlicia tras retirar 20:")
    print(alicia)

    # Bob ingresa 30
    bob.agregar_dinero(30.0)
    print("\nBob tras ingresar 30:")
    print(bob)

    # Bob transfiere 40 a Alicia
    bob.transferir_dinero(alicia, 40.0)
    print("\nDespués de transferir 40 de Bob a Alicia:")
    print("Alicia:", alicia)
    print("Bob:", bob)