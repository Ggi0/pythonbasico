
        #Ejercicio 1
print('---------> Ejercicio 1 <---------')

contraseña = str(input('Crea una contraseña: '))
contraseña2 = str(input('Confirma tu contraseña: '))

if contraseña != contraseña2:
    while contraseña != contraseña2:
        print('')
        print('Datos erroneos. Por favor, inténtelo otra vez.')
        contraseña2 = str(input('Confirma tu contraseña: '))

if contraseña == contraseña2:
    print('')
    print('Tu contraseña es correcta.')
    print('')

print('---------------------------------')
print('')

        #Ejercicio 2
import re
print('---------> Ejercicio 2 <---------')

alumno = str(input('ingrese su primer nombre: '))
sexo = str(input('Sexo (M o H):' ))

if sexo == 'M':
    if re.search('[A-M]', alumno):
        grupo = 'Grupo A'
    else:
        grupo = 'Grupo B'
else:
    if re.search('[N-Z]', alumno):
        grupo = 'Grupo A'
    else:
        grupo = 'Grupo B'
print('Tu perteneces al ' + grupo)
print('---------------------------------')
