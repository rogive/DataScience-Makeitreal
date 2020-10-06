### Taller 4 - Control de Flujo

## 1- In Range

# Cree una funcion llamada in_range() que recibe tres parametros num, lower, upper
# La función debe retornar True si num es mayor o igual que lower y menor o igual que upper. De otra manera retorne False

def in_range (num, lower, upper):
  if num >= lower and num <= upper:
    return True
  return False

print(in_range(6, 4, 10))

## 2- Movie Review

# Cree una funcion llamada movie_review() que tiene un parametro llamado rating
# Si rating es menor o igual que 5 retorne "Avoid at all costs!".
# Si el rating es entre 5 y 9retorne "This one was fun."
# Si el rating es 9 o mas retorne "Outstanding!"

def movie_review(rating) :
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating > 5 and rating < 9 :
    return "This one was fun."
  else :
    return "Outstanding!"

print(movie_review(9.5))

## 3- Twice as Large

# Cree una función llamada twice_as_large() que tome dos parametros num1 y num2
# Retorne True si num1 es mas del doble de num2 y retorne False de lo contrario

def twice_as_large(num1, num2) :
  if num1 > 2*num2 :
    return True
  else :
    return False

print(twice_as_large(9, 5))

## 4- Power

# Cree una funcón llamada large_power() que tome dos parametro: base y exponent
# Si base elevado a la exponent es mayor que 5000 retorne True de lo contrario False

def large_power(base, exponent) :
  if base ** exponent > 5000 :
    return True
  else :
    return False

print(large_power(9, 5))

## 5- Divisible por 10

# Cree una funcion llamada divisible_by_ten() que reciba un parametro llamado num
# La función debe retornar True si num es divisible por 10 y False de lo contrario
# Considere como usar el modulo (%) para validar su divisibilidad

def divisible_by_ten(num) :
  if num % 10 == 0 :
    return True
  else :
    return False

print(divisible_by_ten(120))

## 6- Numero Maximo

# Cree una funcion llamada max_num() que reciba tres parametros llamados num1, num2, num3
# La funcion debe retornar el numero mayor de los tres
# Si dos numeros empatan como el mas grande, debes retornar "es un empate!"

def max_num(num1, num2, num3) :
  if num1 > num2 and num1 > num3 :
    return num1
  elif num2 > num1 and num2 > num3 :
    return num2
  elif num3 > num1 and num3 > num2 :
    return num3
  else:
    return "es un empate!"
print(max_num(2, 2, 6))

## 7- Over Budget

# Cree una función llamada over_budget() que reciba 5 parametros: budget, food_bill, electricity_bill, internet_bill, y rent.
# La función debe retornar True si budget es menor que la suma de los otros cuatro parametros. Retorne False de otra manera

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent) :
  if budget < food_bill + electricity_bill + internet_bill + rent :
    return True
  else :
    return False

print(over_budget(120, 30, 25, 35, 50))