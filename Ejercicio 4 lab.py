def calcular_estadisticas(*numeros):
    if not numeros:
        print("No se ingresaron números.")
        return
    
    numeros_ordenados = sorted(numeros)
    n = len(numeros)
    promedio = sum(numeros) / n
    mediana = numeros_ordenados[n//2] if n % 2 != 0 else (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
    varianza = sum((x - promedio) ** 2 for x in numeros) / n
    desviacion = varianza ** 0.5
    
    print(f"Promedio: {promedio}")
    print(f"Mediana: {mediana}")
    print(f"Desviación estándar: {desviacion}\n")

numeros = list(map(float, input("Ingrese una lista de números separados por espacios: ").split()))
calcular_estadisticas(*numeros)
