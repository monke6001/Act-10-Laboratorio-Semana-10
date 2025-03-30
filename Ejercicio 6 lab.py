
class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
    
    def mostrar_info(self):
        return f"{self.marca} {self.modelo}, Año: {self.anio}, Precio: ${self.precio}"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, puertas):
        super().__init__(marca, modelo, anio, precio)
        self.puertas = puertas
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Puertas: {self.puertas}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, cilindrada):
        super().__init__(marca, modelo, anio, precio)
        self.cilindrada = cilindrada
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Cilindrada: {self.cilindrada}cc"

def menu():
    while True:
        print("\nSistema de Gestión de Vehículos")
        print("1. Agregar Automóvil")
        print("2. Agregar Motocicleta")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            marca = input("Ingrese la marca del automóvil: ")
            modelo = input("Ingrese el modelo: ")
            anio = input("Ingrese el año: ")
            precio = float(input("Ingrese el precio: "))
            puertas = int(input("Ingrese el número de puertas: "))
            auto = Automovil(marca, modelo, anio, precio, puertas)
            print("Información del Automóvil:")
            print(auto.mostrar_info())
        
        elif opcion == "2":
            marca = input("Ingrese la marca de la motocicleta: ")
            modelo = input("Ingrese el modelo: ")
            anio = input("Ingrese el año: ")
            precio = float(input("Ingrese el precio: "))
            cilindrada = int(input("Ingrese la cilindrada: "))
            moto = Motocicleta(marca, modelo, anio, precio, cilindrada)
            print("Información de la Motocicleta:")
            print(moto.mostrar_info())
        
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")

menu()
