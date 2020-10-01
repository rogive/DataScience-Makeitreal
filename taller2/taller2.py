## Taller 2

# 1- Añadamos en nuestro primer artículo, el Lovely Loveseat que es el nombre de la tienda. Cree una variable llamada 
# lovely_loveseat_description y asígnele la siguiente cadena: "Lovely Loveseat. Tufted polyester blend on wood. 32 inches 
# high x 40 inches wide x 30 inches deep. Red or white."

lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""

# 2- Genial, ahora vamos a crear un precio para el loveseat. Crear una variable lovely_loveseat_price y fijarlo en 254.00

lovely_loveseat_price = 254.00

# 3- Ampliemos nuestro inventario con otro mueble característico! Cree una variable llamada stylish_settee_description y asígnele la siguiente cadena: 
# "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""

# 4- Ahora fijemos el precio de nuestro elegante sofá. Cree una variable stylish_settee_price y asígnele el valor de 180.50.

stylish_settee_price = 180.50

# 5- Fantástico, sólo necesitamos un artículo más antes de estar listos para el negocio. Cree una nueva variable llamada luxurious_lamp_description 
# asígnele lo siguiente: "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""

# 6- Vamos a fijar el precio de este artículo. Cree una variable llamada luxurious_lamp_price ajústela a 52.15.

luxurious_lamp_price = 52.15

#7- Para ser una empresa, también deberíamos estar calculando el impuesto sobre las ventas. Guardemos eso en una variable también. 
# Defina la variable sales_tax y póngala igual a .088. Eso es el 8,8%.

sales_tax = .088

## Nuestro primer cliente

# 8- Nuestro primer cliente está haciendo su compra! Vamos a mantener un recuento de sus gastos definiendo una variable llamada 
# customer_one_total. Ya que no han comprado nada todavía, vamos a poner esa variable igual a 0 por ahora.

customer_one_total = 0

# 9- También debemos mantener una lista de las descripciones de las cosas que están comprando. Crear una variable llamada customer_one_itemization 
# y establecerla como igual a la cadena vacía "". Le añadiremos las descripciones a medida que hagan sus compras.

customer_one_itemization = ""

# 10- Nuestro cliente ha decidido que va a comprar nuestro Lovely Loveseat! Añada el precio a customer_one_total.

customer_one_total += lovely_loveseat_price

# 11- Comencemos a hacer un seguimiento de los artículos que nuestro cliente compró. Añada la descripción del Lovely Lovely Loveseat a customer_one_itemization.

customer_one_itemization += lovely_loveseat_description

# 12 - Nuestro cliente también ha decidido comprar la lámpara de lujo! Sumemos el precio al total del cliente.

customer_one_total += luxurious_lamp_price

# 13- Mantengamos el detalle actualizado y agreguemos la descripción de la Lámpara de Lujo a nuestro detalle.

customer_one_itemization += luxurious_lamp_description

# 14- ¡Están listos para hacer check out! Comencemos por calcular el impuesto sobre las ventas. Cree una variable llamada customer_one_tax y configúrela igual a customer_one_total por sales_tax.

customer_one_tax = customer_one_total * sales_tax

# 15- Añada el tax al coste total del cliente.

customer_one_total += customer_one_tax

# 16- ¡Empecemos a imprimir sus recibos! Comience por imprimir el encabezamiento para su detalle. Imprima la frase "Artículos de cliente uno:".

bill_title = "Artículos de cliente uno:"
print(bill_title)

# 17- Imprima customer_one_itemization.

print(customer_one_itemization)

# 18- Ahora agregue un encabezamiento para su costo total: Imprimir "Total Cliente Uno:"

total_cost_title = "Total Cliente Uno: "
print(total_cost_title)

# 19- Ahora imprima el total! Nuestro primer cliente ahora tiene un recibo por las cosas que compró.

print(customer_one_total)

#20- Felicitaciones! Creamos nuestro catálogo y atendimos a nuestro primer cliente. Usamos nuestro 
# conocimiento de cadenas y números para crear y actualizar variables. Pudimos imprimir una lista detallada
#  y un costo total para nuestro cliente.