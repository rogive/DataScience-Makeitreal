### Taller 6

## Python Loops Exercises
# Usted trabaja como Data Analyst un salon para cuidado femenino. Usted va a calcular importantes metricas del negocio. Empezemos!

## Initial data
# Usted fue proveido con las siguientes listas

# hairstyles los nombres de cortes en el negocio
# prices el precio de cada corte de la lista hairstyles
# last_week el numero de cada corte en hairstyles que fue comprado la semana anterior
# Data
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

## Precios y Rebajas
# Cree una variable llamada total_price e iniciela en 0
# Itera sobre la lista prices y añade cada precio a la variable total_price
# Crea una variable llamada average_price que es total_price dividido por el numero de precios. 
# Recuerde que puede obtener el largo con la funcion len()
# Imprima el valor de average_price para que el resultado luzca como esto: Average Haircut Price: <average_price>
# La dueña quiere bajar todos los precios en 5 usd. Use un list comprenhension para hacer una lista llamada new_prices 
# el cual tiene cada elemento de prices menos 5
# Imprima new_prices

total_price = 0
for price in prices :
  total_price += price
print (total_price)

average_price = total_price / (len(prices))
print ("Average Haircut Price: " + str(average_price))

new_prices = [price-5 for price in prices]
print (new_prices)

## Ingresos
# La dueña del negocio realmente quiere ser rentable, y quiere saber cuanto vendio la semana pasada. 
# Cree una nueva variable llamada total_revenue e iniciela en 0
# Use un ciclo for para crear una variable i que va de 0 a len(hairstyles). Ayuda: puedes usar range() para hacer esto.
# Añade el producto de prices[i] (el precio de cada haircut en la posicion i) y last_week[i] (el numero de personas que
# tuvo un corte en la posicion i) a total_revenue en cada paso.
# Despues del ciclo imprime total_revenue de forma tal que se vea de la siguiente manera. Total Revenue: <total_revenue>
# Encuentra el promedio diario de ingresos dividiendo total_revenue por 7. Llama este numero average_daily_revenue

total_revenue = 0
for i in range(len(hairstyles)) :
  total_revenue += prices[i] * last_week[i]
print ("Total Revenue: " + str(average_price))

average_daily_revenue = total_revenue / 7
print ("Promedio Diario de Ingresos: " + str(average_daily_revenue))