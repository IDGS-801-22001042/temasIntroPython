import math

class distancias:
    x1=0
    y1=0
    x2=0
    y2=0
    res=0

    def __init__(self,x1=0,y1=0,x2=0,y2=0,res=0):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.res=res
    
    def calcularDist(self):
        self.res=math.sqrt(((self.x2-self.x1)*(self.x2-self.x1))+((self.y2-self.y1)*(self.y2-self.y1)))
        print("La distancia es: {}".format(self.res))

    @classmethod
    def pedirDatos(cls):
        x1 = float(input("Ingrese el valor de la variable X1: "))
        y1 = float(input("Ingrese el valor de la variable Y1: "))
        x2 = float(input("Ingrese el valor de la variable X2: "))
        y2 = float(input("Ingrese el valor de la variable Y2: "))
        return cls(x1, y1, x2, y2)

def main():
    obj = distancias.pedirDatos()
    obj.calcularDist()
if __name__ == "__main__":
    main()
