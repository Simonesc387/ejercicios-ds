class Libro:
    def __init__(self, titulo, autor, isbn, disponibilidad = True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidad = disponibilidad