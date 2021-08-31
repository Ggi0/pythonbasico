#hoja de trabajo 1


def jugar(intento=1): 
    respuesta = input("¿De qué color es la fruta en la que estoy pensando? \n") 
    if respuesta != "naranja": 
        if intento < 3: 
            print ("¡Fallaste! Inténta de nuevo" )
            intento += 1 
            jugar(intento) # llamada (recurcividad)
        else: 
            print ("¡Perdiste!") 
    else:
        print ("¡Ganaste!")
jugar()