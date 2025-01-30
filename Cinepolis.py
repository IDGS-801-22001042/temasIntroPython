from io import open

class Cinepolis:
    def __init__(self):
        self.compras = []
        self.opcion = ""
        self.nombre = ""
        self.personas = 0
        self.boletos = 0
        self.total = 0.0
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
                print("Opción inválida, intenta de nuevo.")

    def realizarCompra(self):
        self.nombre = input("\nNombre de la persona que compra: ")

        while True:
            self.personas = int(input("¿Cuántas personas asistirán?: "))

            if 1 <= self.personas <= 7:
                self.boletos = self.validarBoletos()
                self.total = self.calcularTotal(self.boletos)

                self.tarjeta = input("¿Pagarás con tarjeta Cinepolis? (s/n): ").lower()
                if self.tarjeta == "s":
                    self.total *= 0.9

                self.total = round(self.total, 2)

                self.compras.append((self.nombre, self.boletos, self.total))

                print(f"\n{self.nombre}, el total a pagar por {self.boletos} boleto(s) es: ${self.total}\n")
                self.guardarEnArchivo(self.nombre, self.boletos, self.total)
                break
            else:
                print("Debes ingresar una cantidad entre 1 y 7.")

    def validarBoletos(self):
        while True:
            boletos = int(input("¿Cuántos boletos deseas comprar? (máximo 7 por persona): "))

            if boletos <= 0:
                print("Debes comprar al menos un boleto. Intenta de nuevo.")
            elif boletos > 7:
                print("No puedes comprar más de 7 boletos por persona. Intenta de nuevo.")
            elif boletos < self.personas:
                print("Cantidad insuficiente de boletos.")
                opcion2 = int(input("¿Desea cambiar la cantidad de boletos o de personas?\n1. Boletos\n2. Personas\nElige una opción: "))
                if opcion2 == 1:
                    continue  
                elif opcion2 == 2:
                    return self.realizarCompra()  
            elif boletos > self.personas:
                print("Cantidad excedente de boletos. Intenta de nuevo.")
                opcion2 = int(input("¿Desea cambiar la cantidad de boletos o de personas?\n1. Boletos\n2. Personas\nElige una opción: "))
                if opcion2 == 1:
                    continue  
                elif opcion2 == 2:
                    return self.realizarCompra()  
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
            print(f"{nombre:<15}{boletos:<10}{total:<10}")

        print("\nGracias por utilizar el sistema de Cineco.")
        with open("compras.txt", "w") as archivo:
            archivo.write("")

if __name__ == "__main__":
    cinepolis = Cinepolis()
    cinepolis.menuPrincipal()
