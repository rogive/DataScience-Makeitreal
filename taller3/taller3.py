### TALLER 3

## 1- Average
#Escriba una función llamada average()que recibe dos parametros llamados num1 y num2
#La Función debe retornar el valor promedio de esos dos numeros

def average(num1, num2):
  return (num1+num2)/2
print(average(3,5))

## 2- Exponencial
#Escriba una funcion llamada tenth_power() que reciba un parametro llamado num
#La función debe retornar num a la 10ma potencia

def tenth_power(num):
  return num**10
print(tenth_power(2))

## 3- Bond
#Escriba una funcion llamada introduction() que reciba dos parametros first_name y last_name
#La funcion debe retornar el last_name seguido por una coma, un espacio, first_name, otro 
# espacio y finalmente last_name

def introduction(first_name, last_name):
  return (last_name + ", " + first_name + ", " + last_name)
print(introduction("Ivan", "Rodriguez"))

## 4- Raiz cuadrada
#Escriba una funcion llamada square_root() que toma un parametro llamado num
#Use los exponentes (**)para retornar la raiz cuadrada de num

def square_root(num):
  return num**(1/2)
print(square_root(625))

## 5- Propina

# Cree una funcion llamada tip() que reibe dos parametros llamados total y percentage
# Esta funcion deberia retornar el monto que usted deberia dar de propina dado un total
# y un porcentaje que usted quiera.

def tip(total, percentage):
  return total*(1+(percentage/100))
print(tip(50000, 10))

## 6- Porcentaje de ganancias

# Cree una funcion llamada win_percentage() que toma dos parametros llamados wins y losses
# La funcion debe retornar el porcentaje total de juegos ganados por un equipo dados esos dos datos.

def win_percentage(wins, losses):
  return ((wins*100)/(wins+losses))
print(win_percentage(6, 4))

## 7- Primeros tres multiples

# Escriba una funcion llamada first_three_multiples() que toma un parametro llamado num
# Esta funcion debe imprimir los primeros tres multiplos de num, luego deberia retornar el tercer multiplo.
# Por ejemplo, first_three_multiples(7) deberia retornar 7, 14 y 21 en tres lineas diferentes y retornar 21

def first_three_multiples(num):
  print(num*1, num*2, num*3)
  return num*3
print(first_three_multiples(7))

## 8- Año Perruno

# Dicen que un año en un humano es equivalente a 7 años en la vida de los perros.
# Escriba una funcion llamada dog_years() que toma dos parametros name y age
# La funcion debe computar a age en años de perro y retornar el siguiente string: {name},
# tu tienes {age} años en años de perro

def dog_years(name, age):
  life_dog = age * 7
  return (name + ", tu tienes " + str(life_dog) + " años en años de perro")
print(dog_years("ivan", 28))