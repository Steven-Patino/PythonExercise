import os


def buscar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"] == nombre:
            return p
    return None


def agregar_producto(inventario, nombre, precio, cantidad):
    existente = buscar_producto(inventario, nombre)
    if existente:
        existente["cantidad"] += cantidad
    else:
        inventario.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }) 


def mostrar_inventario(inventario):
    if not inventario:
        print("\nEl inventario actualmente esta vacío.\n")
        return

    print("\n"+"="*40+" INVENTARIO "+"="*40)
    for p in inventario:
        subtotal=p["cantidad"]*p["precio"]
        print(f"Producto: {p['nombre']} | Precio: {p['precio']:.2f} | Cantidad: {p['cantidad']} | Subtotal: {subtotal:.2f}")
    print()



def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario, nombre)
    if not producto:
        return False

    if nuevo_precio != None:
        producto["precio"] = nuevo_precio
    if nueva_cantidad != None:
        producto["cantidad"] = nueva_cantidad

    return True


def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if not producto:
        return False

    inventario.remove(producto)
    return True


def calcular_estadisticas(inventario):
    if not inventario:
        return None

    subtotal = lambda p: p["precio"] * p["cantidad"]

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }


def limpiar():
    input("Preciona Enter para continuar....")
    os.system('cls' if os.name == 'nt' else 'clear')