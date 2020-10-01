## TALLER 1

# 1- Imprima su nombre usando el comando print().
print("Ivan Rodriguez")

# 2- Si su impresion uso comillas dobles " cambieles a comillas simples. Si usted uso comillas ' cambielas por comillas dobles.
print('Ivan Rodriguez')

# 3- Escriba la variable meal y asignele el valor de breakfast e imprimalo. Luego cambie el valor asignado por lunch e imprimalo.
meal = "breakfast"
print(meal)
meal = "launch"
print(meal)

# 4- Donde se encuentra el error de la siguiente linea de codigo? meal = "lunch, breakfast and "tea". Guarde en un string su respuesta y asignela a una variable llamada error_encontrado. Ahora en una nueva variabla llamada tipo_de_error asignele un string con el tipo de error: "sintax error" o "name error".

error_encontrado = "error en el uso de comillas al asignar un string, utilizar otro tipo de comillas dentro de la asignación"
tipo_de_error = "sintax error"

# 5- Escriba en diferentes variables las ultimas 3 peliculas que vio y asigneles su propio rating (puede ser flotante) segun su criterio.
movie1 = "the seven deadly sins"
rating1 = 3.7
movie2 = "Enola Holmes"
rating2 = 4.2
movie3 = "parasitos"
rating2 = 4.2

# 6- Imprima el resultado de la siguiente ecuacion: 25 * 68 + 13 / 28
ecuacion1 = (25*68) + (13/28)
print(ecuacion1)

# 7- Imprima el resultado de la siguiente operacion: 80 / 0
#print(80/0)
print("indeterminado -> error division por cero")

# 8- ¡Has decidido meterte en el mundo de tejer edredones! Para calcular el número de cuadrados que necesitarás para tu primera colcha, vamos a crear dos variables: quilt_width y quilt_length. Hagamos este primer edredón de 8 cuadrados de ancho y 12 de largo. Imprime el número de cuadrados que necesitarás para crear el edredón!
quilt_width = 8
quilt_length = 12
totaldecuadrados = quilt_width * quilt_length
print(totaldecuadrados)

# 9- Concatenar las cadenas siguientes y guardar el mensaje que forman en la variable mensaje.
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

mensaje = string1 + string2 + string3 + string4 + string5 + string6

# 10- Estamos haciendo compras en línea y encontramos un par de zapatillas nuevas. Justo antes de que nos vayamos, encontramos un bonito suéter y algunos libros que también queremos comprar! Utilice el operador += para actualizar el precio_total e incluir los precios de nice_sweater y fun_books.
precio_total = 0
zapatillas_nuevas = 50
precio_total += zapatillas_nuevas
nice_sweater = 39
precio_total += nice_sweater
fun_books = 20
precio_total += fun_books

# 11- Asigne el string: "Stranger, if you passing meet me and desire to speak to me, why should you not speak to me? And why should I not speak to you?" a la variable to_you

to_you = """Stranger, if you passing meet me and desire to speak to me, why should you not speak to me? And why should I not speak to you?"""