#!/usr/bin/env python3

class CuentaBancaria:
    def __init__(self, titular, saldo = 0.0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, monto):
        print(f"Depositando {monto} en cuenta de {self.titular}")
        if monto>0:
            self.saldo += monto
        else:
            print("Error de deposito: monto menor o igual a cero\n")

    def retirar(self, monto):
        print(f"Retirando {monto} de cuenta de {self.titular}")
        if monto>self.saldo:
            print(f"Error de retiro: saldo insuficiente. Saldo de {self.titular}: ${self.saldo}\n")
        else:
            self.saldo -= monto

    def mostrar_info(self):
        print(f"\nTitular: {self.titular}\nSaldo: ${self.saldo}\n")

def main():
    c1 = CuentaBancaria("Juan")
    c2 = CuentaBancaria("Jose", 5000)
    c3 = CuentaBancaria("Pedro", 10)
    cuentas = (c1, c2, c3)
    for c in cuentas:
        c.mostrar_info()
    c1.depositar(-100)
    for c in cuentas:
        c.retirar(500)
    c1.depositar(1000)
    c1.retirar(500)
    for c in cuentas:
        c.mostrar_info()

if __name__ == "__main__":
    main()