from modelos.persona import Persona
from modelos.libro import Libro

#personas
persona1 = Persona("carlos", "perez", "12345678","987654321")
persona2 =  Persona("jhon","palomino", "3421676", "987645321")

#libros
libro1 = Libro("los ojos de mi princesa","carlos cuauhtemoc sanchez", "LIB001", 5)
libro2 = Libro("los ojos de mi princesa2","carlos cuauhtemoc sanchez", "LIB002", 5)
libro3 = Libro("la seleccion", "kiera cass", "LIB003", 5)
libro4 = Libro("la elite", "kiera cass", "LIB005", 5)


#METODO MOSTRAR INFORMACION
print(persona1.mostrar_informacion())
print(persona2.mostrar_informacion())

#MOSTRAR INFORMACION DE LIBROS
print(libro1.mostrar_info_libro())
print(libro2.mostrar_info_libro())
print(libro3.mostrar_info_libro())
print(libro4.mostrar_info_libro())

#METODO PRESTAR LIBROS
print("antes de:", libro1.disponible)
resultado = libro1.prestar_libro()
print("despues de:", libro1.disponible)

if resultado:
    print("prestamo realizado correctamente")
else:
    print("no hay stock suficiente")

#METODO DEVOLVER LIBRO
print("antes de:",libro1.disponible)
resultado = libro1.devolver_libro()
print("despues de:", libro1.disponible)


if resultado:
    print("libro devuelto correctamente")
else:
    print("ERROR no se puede devolver este libro")
    


