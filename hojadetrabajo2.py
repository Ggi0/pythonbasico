
        #Ejercicio 1

print('---------> Ejercicio 1 <---------')
numero=int(input("Ingresa un número entero positivo: " ))
if numero <= 0:
    while numero <= 0:
        print('El número debe ser mayor que 0')
        numero=int(input("Ingresa un número entero positivo: " ))

for x  in range(numero):
    for y in range(x+1):
        print('*', end='')
    print('')

print('---------------------------------')
print('')



        #ejercicio 2

print('---------> Ejercicio 2 <---------')
num=int(input('Ingresa un número entero positivo: '))
if num < 0:
    while num < 0:
        print('El número debe ser mayor que 0')
        num=int(input("Ingresa un número entero positivo: " ))

for i in range(num+1):
    print(num-i, ',', end='')

print()
print('---------------------------------')
print('')    



        #ejercicio 3

print('---------> Ejercicio 3 <---------')
n = int(input('Introduce un número entero del 2 en adelante: '))
if n < 2:
    while n < 2:
        print('El número debe ser 2 o mayor.')
        n = int(input('Introduce un número entero del 2 en adelante: '))

j = 2
while n % j != 0:
    j+=1
if j==n:
    print(str(n) + ' es un número primo.')
else:
    print(str(n) + ' no es un número primo.')

print('---------------------------------')
#giovanni c.