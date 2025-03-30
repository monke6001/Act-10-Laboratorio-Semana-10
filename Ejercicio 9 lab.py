# Paradigma Imperativa
n = int(input("Ingrese un número para contar hasta él: "))
contador = 1
while contador <= n:
    print(contador, end=' ')
    contador += 1
print()

# Paradigma Estructurada
def calcular_factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

num = int(input("Ingrese un número para calcular su factorial: "))
print(f"Factorial de {num} es {calcular_factorial(num)}")

# Paradigma Modular
# Archivo: operaciones.py (Simulado dentro del mismo archivo)
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "No se puede dividir por cero"

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
print(f"Suma: {suma(a, b)}")
print(f"Resta: {resta(a, b)}")
print(f"Multiplicación: {multiplicacion(a, b)}")
print(f"División: {division(a, b)}")

# Paradigma Orientado a Objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def presentar(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}.")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
carrera = input("Ingrese su carrera: ")
estudiante = Estudiante(nombre, edad, carrera)
estudiante.presentar()