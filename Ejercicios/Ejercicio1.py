# Escribir un programa que almacene las asignaturas de un curso
# por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

L = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(L)

# muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> 
# es cada una de las asignaturas de la lista.

for i in L:
    print("Yo estudio: ", i, "\n")
    
