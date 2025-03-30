
contactos = []

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    correo = input("Ingrese el correo electrónico: ")
    contactos.append((nombre, numero, correo))
    print("Contacto agregado con éxito!\n")

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    for c in contactos:
        if c[0] == nombre:
            print("Contacto encontrado:", c)
            return
    print("Contacto no encontrado.\n")

def listar_contactos():
    if not contactos:
        print("No hay contactos en la agenda.\n")
        return
    print("Lista de contactos ordenados alfabéticamente:")
    for c in sorted(contactos):
        print(c)
    print()

def menu():
    while True:
        print("\nGestión de Contactos")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar contactos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            listar_contactos()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.\n")

menu()
