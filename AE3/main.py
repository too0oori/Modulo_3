from descuentos import calcular_descuento, probar_casos

if __name__ == "__main__":
    # EJEMPLO 1: Con todos los descuentos aplicados
    cantidad_productos = 12
    compras_previas = 6
    total_compra = 550
    dia_promocion = True

    descuento = calcular_descuento(cantidad_productos, compras_previas, total_compra, dia_promocion)

    print("Cliente 1:")
    print(f"  Productos: {cantidad_productos}, Compras previas: {compras_previas}")
    print(f"  Total: ${total_compra}, Promoción: {dia_promocion}")
    if descuento == 30:
        print(f"  Descuento aplicado: {descuento}% (limitado a 30%)")
    else:
        print(f"  Descuento aplicado: {descuento}%")
    print()

    # Cliente 2: Sin descuentos
    cantidad_productos = 8
    compras_previas = 3
    total_compra = 300
    dia_promocion = False

    descuento = calcular_descuento(cantidad_productos, compras_previas, total_compra, dia_promocion)

    print("Cliente 2:")
    print(f"  Productos: {cantidad_productos}, Compras previas: {compras_previas}")
    print(f"  Total: ${total_compra}, Promoción: {dia_promocion}")
    print(f"  Descuento aplicado: {descuento}%")
    print()

    # Cliente 3: Excede el límite de 30%
    cantidad_productos = 20
    compras_previas = 10
    total_compra = 1000
    dia_promocion = True

    descuento = calcular_descuento(cantidad_productos, compras_previas, total_compra, dia_promocion)

    print("Cliente 3 (posible límite 30%):")
    print(f"  Productos: {cantidad_productos}, Compras previas: {compras_previas}")
    print(f"  Total: ${total_compra}, Promoción: {dia_promocion}")
    if descuento == 30:
        print(f"  Descuento aplicado: {descuento}%")
    else:
        print(f"  Descuento aplicado: {descuento}%")
    print()

    # Casos de borde y adicionales
    probar_casos()
