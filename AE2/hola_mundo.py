# 1. Imprime "Hola, mundo"

print('Hola, mundo') 

# 2. Imprime "Hola, Sofía" con el nombre en una variable

nombre = "Sofía"

print("Hola,", nombre) # con una coma

print("Hola, " + nombre) # con un +

# 3. Imprimir "Hola 156!" con el número en una variable

numero = 7

print("Hola,", numero, "!") # con una coma

print("Hola, " + str(numero) + "!") # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables

comida1 = "lentejas"

comida2 = "fideos con salsa"

print("Me encanta comer {} y {}!".format(comida1, comida2)) # con .format()

print(f"Me encanta comer {comida1} y {comida2}!") # con una cadena f


# BONUS NINJA: Otros métodos de cadena
palabras = ["Me", "encanta", "Python"]
print(" ".join(palabras))  # Une con espacios: "Me encanta Python"
print("-".join(palabras))  # Une con guiones: "Me-encanta-Python"

frase = "Me encanta programar en Python"
print(frase.find("encanta"))  # Encuentra posición: 3
print(frase.find("Python"))  # Encuentra posición: 26
print(frase.find("Java"))    # No encuentra: -1
print(nombre.find("í"))      # Encuentra "í" en "Sofía": 3