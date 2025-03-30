
productos = []

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    productos.append({"nombre": nombre, "categoria": categoria, "precio": precio, "cantidad": cantidad})
    print("Producto agregado con éxito!\n")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    global productos
    productos = [p for p in productos if p["nombre"] != nombre]
    print("Producto eliminado si existía.\n")

def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    for p in productos:
        if p["nombre"] == nombre:
            print("Producto encontrado:", p)
            return
    print("Producto no encontrado.\n")

def mostrar_productos():
    if not productos:
        print("No hay productos en el inventario.\n")
        return
    print("Lista de productos ordenados por precio:")
    for p in sorted(productos, key=lambda x: x["precio"]):
        print(p)
    print()

def menu():
    while True:
        print("\nGestión de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Mostrar todos los productos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            mostrar_productos()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.\n")

menu()
