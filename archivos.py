import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("El inventario suministrado no contiene ninguna información, no se ha realizado ningn cambio.")
        return None

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except PermissionError:
        print("Ha ocurrido un problema al leer el archivo, No se tienen los permisos para escribir en esa ruta.")

    except Exception as e:
        print(f"Ha ocurrido un problema al leer el archivo, corresponde al error: {e}")


def cargar_csv(ruta):
    productos = []
    filas_invalidas = 0

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            encabezado = next(reader)

            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Ha ocurrido un error, El archivo no tiene un encabezado válido.")
                return [], 0

            for fila in reader:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    productos.append({
                        "nombre": nombre.capitalize().strip(),
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except Exception:
                    filas_invalidas += 1

    except FileNotFoundError:
        print("El archivo no ha sido encontrado, revisa correctamente la ruta ingresada.")
        return [], 0

    except UnicodeDecodeError:
        print("Ha ocurrido un problema al leer el archivo, verificar que la codificacíon de este sea compatible con UTF-8.")
        return [], 0

    except Exception as e:
        print(f"Ha ocurrido un problema al leer el archivo, corresponde al error: {e}.")
        return [], 0

    return productos, filas_invalidas
