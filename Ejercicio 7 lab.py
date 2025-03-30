import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Ejercicio 7: Ordenamiento y Búsqueda
size = int(input("Ingrese el tamaño de la lista: "))
random_list = [random.randint(0, 100) for _ in range(size)]
print("Lista antes de ordenar:", random_list)
sorted_list = quicksort(random_list)
print("Lista ordenada:", sorted_list)
target = int(input("Ingrese un número a buscar: "))
index = binary_search(sorted_list, target)
if index != -1:
    print(f"El número {target} se encuentra en la posición {index}.")
else:
    print(f"El número {target} no está en la lista.")