from conversor import km_a_millas, celsius_a_fahrenheit, litros_a_galones

print("Seleccione una conversión:")
print("1. Kilómetros a millas")
print("2. Celsius a Fahrenheit")
print("3. Litros a galones")

opcion = input("Ingrese una opción: ")
valor = float(input("Ingrese el valor a convertir: "))

if opcion == "1":
    print(f"{valor} km son {km_a_millas(valor)} millas.")
elif opcion == "2":
    print(f"{valor}°C son {celsius_a_fahrenheit(valor)}°F.")
elif opcion == "3":
    print(f"{valor} litros son {litros_a_galones(valor)} galones.")
else:
    print("Opción no válida.")