#Datos de ejemplo para el ejercicio
matriz = [[10, 15, 20], [3, 7, 14]]

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

print("DATOS ORIGINALES")
print(f"Matriz: {matriz}")
print(f"Cantantes: {cantantes}")
print(f"Ciudades: {ciudades}")
print(f"Coordenadas: {coordenadas}")
#Actualizacion Datos
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

print("Matriz actualizada:", matriz)
print("Cantantes actualizados:", cantantes)
print("Ciudades actualizadas:", ciudades)
print("Coordenadas actualizadas:", coordenadas)

print("\n")
#Parte 2
def iterarDiccionario(lista):
    for diccionario in lista:
        salida = []
        for clave, valor in diccionario.items():
            salida.append(f"{clave} - {valor}")
        print(", ".join(salida))
cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]
iterarDiccionario(cantantes)
print("\n")
#Tercera parte
def iterarDiccionario2(llave, lista):
      valores = []
      for diccionario in lista:
         if llave in diccionario:
               valores.append(diccionario[llave])

      for valor in valores:
         print(valor)

iterarDiccionario2("nombre", cantantes)
iterarDiccionario2("pais", cantantes)

# Parte 4: Imprimir información de un diccionario
def imprimirInformacion(diccionario):
    for clave, lista_valores in diccionario.items():
        print(f"{len(lista_valores)} {clave.upper()}")
        for valor in lista_valores:
            print(valor)

# Datos
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

print("Cuarta parte - imprimirInformacion:")
imprimirInformacion(costa_rica)