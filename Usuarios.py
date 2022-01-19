class Usuarios:
    lista_usuarios = []
    def __init__(self, nombre, apellido, edad, dni,):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        Usuarios.lista_usuarios.append(self)
