class Libro:
    def __init__(self,titulo, autor, codigo, disponible):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = disponible
        

    def mostrar_info_libro(self):
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Codigo: {self.codigo} | disponible: {self.disponible}"

    def prestar_libro(self):
        if self.disponible > 0 :
            self.disponible -=1
            return True
        else :
            return False
    def devolver_libro(self):
        if self.disponible < 5:
            self.disponible += 1
            return True
        else:
            return False