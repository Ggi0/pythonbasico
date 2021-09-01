#Giovanni Concohá

#Ejercicio 1
#imc

peso = input("¿cuál es tu peso (kg)? ")
estatura = input("¿cuál es tu altura (m)? ")

#imc = peso/(estatura*estatura)
imc = round(float(peso)/float(estatura)**2,2)
print('Tu índice de masa corporal es:', imc,) 



#Ejercicio 2
#serie de Fibonacci
def fibonacci(n):
    if n<2:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

print(fibonacci(n=int(input('\ningrese un número '))))



#Ejercicio 3
#factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n=int(input('\ningrese un número '))))
