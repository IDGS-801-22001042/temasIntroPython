from io import open
import math

'''
texto=open("archivo.txt","a")
#texto.write("Hola, soy un archivo de texto\n")
texto.write("Hola mundo2\n")
texto.close()
'''

lectura=""
texto=open("archivo.txt","r")
lectura= texto.readline()
print(lectura)
texto.close()

lectura=""
texto=open("archivo.txt","r")
lectura= texto.readlines()
print(lectura)
texto.close()

lectura=""
texto=open("archivo.txt","r")
lectura= texto.readline()
print(type(lectura))
texto.close()