class CuentaBancaria:
    todas_cuentas = []
    def __init__(self, balance = 0, tasa_interes= 0.01, num_cuenta="N/A"):
        self.balance = balance
        self.tasa_interes = tasa_interes
        self.num_cuenta = num_cuenta
        CuentaBancaria.todas_cuentas.append(self)
    
    def deposito(self, amount):
        self.nuevoBalance = self.balance + amount
        self.balance = self.nuevoBalance
        print("---Depósito---")
        print("La cuenta: " + self.num_cuenta + " tiene : " + str(self.balance))
        return self
    
    def retiro(self, amount):
        if (self.balance - amount) > 0:
            self.nuevoBalance = self.balance - amount
            self.balance = self.nuevoBalance
            print("---Retiro---")
            print("La cuenta: " + self.num_cuenta + " tiene : " + str(self.balance))
        else:
            print("---Mensaje---")
            print("La cuenta no tiene fondos suficientes para continuar la operación")
        return self
    
    def generar_interes(self):
        if self.balance > 0:
            print("---Interés Generado---")
            self.nuevoBalance = self.balance * self.tasa_interes
            print("Se ha generado: " + str(self.nuevoBalance) + " de intereses en la cuenta " + self.num_cuenta)
            self.balance = self.nuevoBalance + self.balance
            print("El nuevo balance es de: " + str(self.balance))
        else:
            print("No se cuenta con balance suficiente para generar interés")
        return self
    
    def mostrar_info_cuenta(self):
        print("---Info de la Cuenta---")
        print("La cuenta " + self.num_cuenta + " tiene : " + str(self.balance))
        print("La tasa de interés es de: " + str(self.tasa_interes))
    
    @classmethod
    def informacion_global(cls):
        print("*---Info de todas las cuentas---*")
        for cuentas in cls.todas_cuentas:
            cuentas.mostrar_info_cuenta()

# Inserción de la clase Usuario
class Usuarios:
    lista_usuarios = []
    cantidad = 0
    def __init__(self, nombre, apellido, edad, dni,ahorros):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.cuenta = CuentaBancaria(0,0.05)
        Usuarios.cantidad +=1
        Usuarios.lista_usuarios.append(self)
    
    #Métodos de Usuario
    def deposito(self, amount):
        self.cuenta.deposito(amount)
        print("---Depósito---")
        print("La cuenta de : " + self.nombre +" " + self.apellido + ", tiene : " + str(self.cuenta.balance))
        return self

    def retiro(self, amount):
        self.cuenta.retiro(amount)
        print("---Retiro---")
        print("La cuenta de : " + self.nombre +" " + self.apellido + ", tiene : " + str(self.cuenta.balance))
        return self
    
    def mostrar_info_cuenta(self):
        print("---Info de la Cuenta---")
        print("La cuenta de : " + self.nombre +" " + self.apellido + ", tiene : " + str(self.cuenta.balance))
        print("La tasa de interés es de: " + str(self.cuenta.tasa_interes))