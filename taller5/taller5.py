### Taller 5

## Part I
# Cree una lista de consumidores llamada: first_names
# Ingrese los siguientes valores a la lista: Ainsley, Ben, Chani y Depak.
# Cree una lista vacia llamada age.
# Use append para añadir la edad 42 a la lista creada
# Cree una nueva lista llamada all_ages que combina la lista age con la siguiente lista: 32, 41, 29.
# Cree una nueva variable llamada: name_and_age que combina las dos listas anteriores
# Cree un rango llamado ids que va de 0 a 3.

first_names = []
first_names += ["Ainsley", "Ben", "Chani", "Depak"]
age = []
age.append(42)
all_ages = age + [ 32, 41, 29 ]
name_and_age = first_names + all_ages
ids = range(0,3)

print(name_and_age)

## Part II
# Cree una lista llamada subjects y llenela con las clases que usted esta tomando: "physics", "calculus", "poetry", "history"
# Cree una lista llamada grades y llenela con los siguientes puntajes: 98, 97, 85, 88
# Use la funcion zip para combinar ambas listas. Guarde ese objeto como una list dentro de una variable llamada: gradebook
# Imprima gradebook. es el resultado que esperabamos?
# Su clase de Computer Science ya tiene score, y sacaste un perfecto 100
# Despues de las definiciones de subjects y grades, pero antes de que creara la variable gradebook, use append para añadir "computer science" a subjects y 100 a grades
# Estas son sus calificaciones del semestre anterior: last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
# Cree una nueva variable llamada full_gradebook con los items de ambos semestres: gradebook y last_semester_gradebook

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
subjects.append("computer science")
grades.append(100)
gradebook = list(zip(subjects, grades))
print(gradebook)
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)