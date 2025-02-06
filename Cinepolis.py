from io import open

class Cinepolis:
    def __init__(self):
        self.compras = []
        self.nombre = ""
        self.personas = 0
        self.boletos = 0
        self.total = 0.0
        self.totalCorte = 0.0
        self.tarjeta = ""

    def menuPrincipal(self):
        while True:
            print("\nCINEPOLIS")
            print("1. Comprar boletos")
            print("2. Terminar")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.realizarCompra()
            elif opcion == "2":
                self.terminarPrograma()
                break
            else:
                print("\nOpción inválida, intenta de nuevo.")

    def realizarCompra(self):
        self.nombre = input("\nNombre de la persona que compra: ")

        self.personas = self.validarPersonas()
        self.boletos = self.validarBoletos()

        self.total = self.calcularTotal(self.boletos)

        print("\n¿Desea pagar con efectivo o tarjeta Cineco?")
        print("e)Efectivo")
        print("t)Tarjeta Cineco")
        self.tarjeta = input("Elige una opción: ").lower()
        if self.tarjeta == "t":
            self.total *= 0.9  

        self.total = round(self.total, 2)

        self.totalCorte += self.total 

        self.compras.append((self.nombre, self.boletos, self.total))

        print(f"\n{self.nombre}, el total a pagar por {self.boletos} boleto(s) es: ${self.total}\n")
        self.guardarEnArchivo(self.nombre, self.boletos, self.total)

    def validarPersonas(self):
        while True:
            personas = int(input("\n¿Cuántas personas asistirán?: "))
            if 1 <= personas <= 7:
                return personas
            elif personas == "":
                print("Caracteres inválidos")
            else:
                print("Deben ser entre 1 y 7 personas.")

    def validarBoletos(self):
        while True:
            boletos = int(input("\n¿Cuántos boletos deseas comprar? (máximo 7 por persona): "))

            if boletos <= 0:
                print("Debes comprar al menos un boleto.")
            elif boletos < self.personas or boletos > self.personas:
                print("\nLa cantidad de boletos no coincide con la cantidad de personas.")
                print("¿Qué deseas cambiar?")
                print("1. Boletos")
                print("2. Personas")
                opcion = int(input("Elige una opción: "))
                if opcion == 1:
                    continue  
                elif opcion == 2:
                    self.personas = self.validarPersonas()
            else:
                return boletos

    def calcularTotal(self, boletos):
        precio_unitario = 12
        if boletos > 5:
            descuento = 0.15
        elif 3 <= boletos <= 5:
            descuento = 0.10
        else:
            descuento = 0

        total = boletos * precio_unitario * (1 - descuento)
        return total

    def guardarEnArchivo(self, nombre, boletos, total):
        with open("compras.txt", "a") as archivo:
            archivo.write(f"{nombre},{boletos},{total}\n")

    def terminarPrograma(self):
        print("\nResumen de compras:\n")
        print(f"{'Nombre':<15}{'Boletos':<10}{'Total':<10}")
        print("-" * 35)
        for compra in self.compras:
            nombre, boletos, total = compra
            print(f"{nombre:<15}{boletos:<10}${total:<10.2f}")
        print("-" * 35)
        print(f"TOTAL GENERAL: --------- ${self.totalCorte:.2f}")  

        print("\nGracias por utilizar el sistema de Cinepolis.")

        
        with open("compras.txt", "w") as archivo:
            archivo.write("")

if __name__ == "__main__":
    cinepolis = Cinepolis()
    cinepolis.menuPrincipal()
