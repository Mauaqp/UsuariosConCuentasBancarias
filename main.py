from CuentaBancaria import CuentaBancaria

cuenta1 = CuentaBancaria(100, 0.01, "cta001")
cuenta2 = CuentaBancaria(10, 0.01, "cta002")

cuenta1.mostrar_info_cuenta()
cuenta2.mostrar_info_cuenta()
# Para la primera cuenta, haz 3 depósitos y 1 retiro, 
# luego genera intereses y muestra la información de la cuenta, todo en una línea de código (es decir, encadenando)
cuenta1.deposito(50).deposito(100).deposito(10).retiro(120).generar_interes().mostrar_info_cuenta()

#Para la segunda cuenta, haz 2 depósitos y 4 retiros, 
# luego genera intereses y muestra la información de la cuenta, todo en una línea de código (es decir, encadenando)
cuenta2.deposito(20).deposito(40).retiro(10).retiro(20).retiro(30).retiro(20).generar_interes().mostrar_info_cuenta()

#Bonus
CuentaBancaria.informacion_global()