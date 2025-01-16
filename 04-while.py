'''x=0
while x <10:
    x=x+1
    print(x)'''

'''operacion de multiplicación de a x b utilizando sumas
a=3
b=4
salida 3+3+3+3=12
'''

x=0

print('Dame dos numeros para multiplicarlos por suma')
print('')
a=int(input('Ingresa el primer numero: '))
b=int(input('Ingresa el segundo numero: '))
resultado=0

while x<b:
    resultado = resultado + a
    print(a,end="")

    if x<b - 1:
        print("+",end="")
    x=x+1
print("=", resultado)