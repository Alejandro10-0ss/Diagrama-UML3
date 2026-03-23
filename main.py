from models import *
biblioteca = Biblioteca("Biblioteca Universitaria")
bibliotecario = Bibliotecario("Profe Julio", "ID-99")

biblioteca.agregar_al_inventario(Libro("1", "El gato con botas",1883 , "Carlo C.", "Cuento Infantil"))
biblioteca.agregar_al_inventario(Libro("2", "Don Quijote", 1605, "Miguel de Cervantes", "Literatura"))
biblioteca.agregar_al_inventario(Libro("3", "Peter Pan",1911, "J.M Barrie", "Cuento infantil"))
biblioteca.agregar_al_inventario(Libro("4", "Blancanieves",1812 , "Hermanos Grim", "Cuento Infantil"))
biblioteca.agregar_al_inventario(Libro("5", "La cigarra y la Hormiga", ... , "Esopo", "Fabula"))
biblioteca.agregar_al_inventario(Libro("6", "La liebre y la tortuga", ... , "Esopo", " Fabula"))
biblioteca.agregar_al_inventario(Libro("7", "El patito feo",1843 , "Cristian Anderson", "Cuento Infantil"))
biblioteca.agregar_al_inventario(Libro("8", "Los tres Cochinitos",1840 , "James H", " Fabula"))
biblioteca.agregar_al_inventario(Libro("9", "Caperucita Roja", 1697, "Charles P", "Cuento Infantil"))
biblioteca.agregar_al_inventario(Libro("10", "Harry Potter y la piedra filosofal", 1997, "Rowling", "Fantasía"))


print(" REGISTRO DE USUARIO ")
nombre_usuario = input("Ingrese su nombre: ")
id_usuario = input("Ingrese su matricula: ")
estudiante = Usuario(nombre_usuario, id_usuario)
print("SISTEMA: Usuario registrado con éxito.\n")


print(" INICIANDO SISTEMA DE GESTION")
print(" INVENTARIO DISPONIBLE ")
for m in biblioteca.inventario:
    print(f"ID: {m.id_material}  {m.titulo} ({m.anio})  Autor: {getattr(m, 'autor', 'N/A')}")
print(" CARGA DE DATOS FINALIZADA \n")

# 4. Proceso de Préstamo (Siguiendo el estilo de tu imagen)
print(" INICIANDO PROCESO DE PRESTAMO")
print(f"Usuario: {estudiante.nombre} (ID: {estudiante.id_persona})")

libro_a_buscar = input("¿Qué libro desea buscar?  ")
biblioteca.buscar_por_titulo(libro_a_buscar)

confirmar = input("\n¿Desea solicitar el préstamo de este material? (SI/NO): ")

if confirmar.upper() == "SI":
    # Buscamos el objeto libro en el inventario para poder prestarlo
    encontrado = None
    for m in biblioteca.inventario:
        if m.titulo.lower() == libro_a_buscar.lower():
            encontrado = m
    
    if encontrado:
        print("SISTEMA: Verificando disponibilidad")
        bibliotecario.prestar(estudiante, encontrado)
        
        # Resumen final (Estilo ticket de tu captura)
        print("\n - RESUMEN DE PRESTAMO -")
        print(f"Usuario: {estudiante.nombre}")
        print(f"Material: {encontrado.titulo}")
        print(f"Estado: ENTREGADO")
        
    else:
        print("ERROR: El material no se encuentra en la lista.")

else:
    print("SISTEMA: Operación cancelada.")

print("\nCERRANDO SESION... ¡gracias por utilizar el sistema de la biblio!")