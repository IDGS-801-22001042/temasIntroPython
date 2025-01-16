import os

def funcion1():
    os.system('cls')
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    res= num1+num2
    print(f'Resultado: {res}')

def funcion2():
    os.system('cls')
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    res= num1-num2
    print(f'Resultado: {res}')

def funcion3():
    os.system('cls')
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    res= num1*num2
    print(f'Resultado: {res}')

def funcion4():
    os.system('cls')
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 2: "))
    res= num1/num2
    print(f'Resultado: {res}')

def run():
    while True:
        os.system('cls')
        print("1.Suma")
        print("2.Resta")
        print("3.Multiplicación")
        print("4.División")
        print("5.Salir")
        op = int(input("Opción: "))

        if op == 1:
            funcion1()
        elif op == 2:
            funcion2()
        elif op == 3:
            funcion3()
        elif op == 4:
            funcion4()
        elif op == 5:
            break  
        else:
            print("Opción inválida")
    

#Controlador
if __name__ == "__main__":
    run()