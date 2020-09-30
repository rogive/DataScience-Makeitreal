num1 = int(input('Escoge un número -> '))
if num1 > 10 :
  print('Tu número es una decena')
elif num1 < 10 and num1 > 4 :
  print ('Tu numero esta entre 4 y 10')
else:
  print(f'El número es: {num1}')