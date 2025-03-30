
def analizar_texto(texto):
    palabras = texto.lower().split()
    total_palabras = len(palabras)
    palabras_unicas = set(palabras)
    frecuencia_palabras = {}
    
    for palabra in palabras:
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    
    palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get)
    
    print(f"Total de palabras: {total_palabras}")
    print(f"Palabras únicas: {len(palabras_unicas)}")
    print("Frecuencia de palabras:", frecuencia_palabras)
    print(f"Palabra más frecuente: '{palabra_mas_frecuente}' aparece {frecuencia_palabras[palabra_mas_frecuente]} veces.")

texto_usuario = input("Ingrese un texto: ")
analizar_texto(texto_usuario)