


class Material:
    def __init__(self, id_material, titulo, anio):
        self.id_material = id_material
        self.titulo = titulo
        self.anio = anio
        self.disponible = True

# Herencia para libros
class Libro(Material):
    def __init__(self, id_material, titulo, anio, autor, genero):
        super().__init__(id_material, titulo, anio)
        self.autor = autor
        self.genero = genero

# Herencia para revistas
class Revista(Material):
    def __init__(self, id_material, titulo, anio, edicion):
        super().__init__(id_material, titulo, anio)
        self.edicion = edicion

# Clase base para las personas
class Persona:
    def __init__(self, nombre, id_persona):
        self.nombre = nombre
        self.id_persona = id_persona

# Usuario que pide prestado
class Usuario(Persona):
    def __init__(self, nombre, id_persona):
        super().__init__(nombre, id_persona)
        self.lista_libros = [] # Aquí guardamos lo que se lleva
        self.bloqueado = False

# El encargado de la biblioteca
class Bibliotecario(Persona):
    def prestar(self, usuario, material):
        if material.disponible == True and usuario.bloqueado == False:
            material.disponible = False
            usuario.lista_libros.append(material)
            print("Préstamo realizado con éxito")
        else:
            print("No se puede prestar el material")

    def recibir_devolucion(self, usuario, material):
        material.disponible = True
        usuario.lista_libros.remove(material)
        print("Material devuelto")

# Clase para organizar los materiales (El catálogo)
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []

    def agregar_al_inventario(self, material):
        self.inventario.append(material)

    def buscar_por_titulo(self, titulo_buscar):
        for m in self.inventario:
            if m.titulo == titulo_buscar:
                print("¡Encontrado! El material está en la biblioteca.")
                return 
        print("Lo sentimos, no tenemos ese material.")

# Clase para las multas
class Multa:
    def __init__(self, usuario, dias_retraso):
        self.usuario = usuario
        self.monto = dias_retraso * 10 # 10 pesos por día
    
    def mostrar_multa(self):
        print(f"El usuario {self.usuario.nombre} debe pagar: ${self.monto}")