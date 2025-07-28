matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

print("=== EJERCICIO 1: Actualizar valores en diccionarios y listas ===")
print("\nEstructuras originales:")
print(f"matriz: {matriz}")
print(f"cantantes: {cantantes}")
print(f"ciudades: {ciudades}")
print(f"coordenadas: {coordenadas}")

matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

print("\n--- Valores Actuazlizados ---")
print(f"matriz: {matriz}")
print(f"cantantes: {cantantes}")
print(f"ciudades: {ciudades}")
print(f"coordenadas: {coordenadas}")

print("\n EJERCICIO 2: Recorrer una lista de diccionarios ")
for cantante in cantantes:
    print(f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")

print("\n EJERCICIO 3: Obtener valores específicos ")
print("\n--- Nombres de los cantantes ---")
for cantante in cantantes:
    print(cantante["nombre"])

print("\n--- Países de los cantantes ---")
for cantante in cantantes:
    print(cantante["pais"])

print("\n EJERCICIO 4: Recorrer diccionario con listas como valores ")
costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

for clave, lista in costa_rica.items():
    print(f"\n{len(lista)} {clave.upper()}")
    for elemento in lista:
        print(elemento)