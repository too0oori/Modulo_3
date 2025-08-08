def calcular_descuento(cantidad_productos, compras_previas, total_compra, dia_promocion):
    descuento = 0

    # Descuento por cantidad de productos y compras previas
    if cantidad_productos > 10:
        descuento += 10
        if compras_previas > 5:
            descuento += 5
    elif compras_previas > 5:
        descuento += 5
    else:
        descuento += 0

    # Descuento por total_compra o día de promoción
    if total_compra > 500:
        descuento += 7

    if dia_promocion:
        descuento += 15

    # Límite máximo del 30%
    if descuento > 30:
        descuento = 30

    return descuento

def probar_casos():
    print("Casos de prueba:")
    
    # Exactamente 10 productos
    resultado = calcular_descuento(10, 8, 600, True)
    print(f"10 productos exactos: {resultado}%")
    
    # Exactamente 5 compras previas
    resultado = calcular_descuento(15, 5, 600, True)
    print(f"5 compras exactas: {resultado}%")
    
    # Exactamente $500
    resultado = calcular_descuento(15, 8, 500, True)
    print(f"$500 exactos: {resultado}%")
    
    # Sin condiciones
    resultado = calcular_descuento(5, 3, 300, False)
    print(f"Sin condiciones: {resultado}%")
    print()


# crear un programa en Python que determine el descuento aplicado a una compra según los siguientes criterios:
# Si el cliente compra más de 10 productos, obtiene un descuento del 10%.
# Si el cliente es frecuente (más de 5 compras previas), se aplica un 5% adicional.
# Si la compra supera los 500 dólares, se otorga un descuento adicional del 7%.
# En días de promoción especial, se aplica un 15% adicional.
# Ningún cliente puede obtener un descuento mayor al 30% en total.

# Requerimientos

# Uso de condicionales: Implementar estructuras if, elif, else para evaluar cada condición.
# Subcondiciones: Combinar condiciones dentro de una misma evaluación.
# Condiciones de borde: Asegurar que el programa maneje casos como exactamente 10 productos, exactamente 500 dólares, etc.
# Condiciones anidadas: Evaluar casos donde varias condiciones sean verdaderas al mismo tiempo.
# Salida controlada: Si ninguna condición se cumple, el descuento será 0%.
# Convención de nombres: Utilizar snake_case en todas las variables y funciones.
# Diagrama de flujo: Dibujar un diagrama que represente la lógica del programa antes de implementarlo.
