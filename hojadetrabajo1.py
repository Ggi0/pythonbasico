#Giovanni Concohá
peso = input("¿cuál es tu peso (kg)? ")
estatura = input("¿cuál es tu altura (m)? ")

#imc = peso/(estatura*estatura)
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es", imc) 
