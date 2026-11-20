class Persona:
    def __init__(self, nombre, apellido, dni, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre} {self.apellido} | DNI: {self.dni} | Telefono: {self.telefono}"
    
    
