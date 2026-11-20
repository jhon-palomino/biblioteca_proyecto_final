class Libro:
    def __init__(self,titulo, autor, codigo, disponible):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = disponible
        

    def mostrar_info_libro(self):
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Codigo: {self.codigo} | disponible: {self.disponible}"

