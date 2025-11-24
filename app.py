import módulo_servicios as ms
import archivos as ar
inventario=[]


while True:
    ms.limpiar()
    opcion_menu=input(""" 

    |------------------------------------------------|
    |       Bienvenido al sistema de inventario,     |
    |       ¿Qué acción deseas realizar?:            |
    |                                                |
    |       1. Agregar Producto                      |
    |       2. Mostrar inventario                    |
    |       3. Buscar producto                       |
    |       4. Actualizar Procucto                   |
    |       5. Eliminar Producto                     |
    |       6. Estadísticas Generales                |
    |       7. Guardar CSV                           |
    |       8. Cargar CSV                            |
    |       9. Salir                                 |
    |                                                |
    |------------------------------------------------|

Digita el número corresponidente a la acción a realizar: """)

    try:
        opcion_menu=int(opcion_menu)
    except ValueError:
        print("El elemento ingresado no corresponde con ninguna de las opciones, observa bien el menú e intenta de nuevo.")
        continue
    if opcion_menu<1 or opcion_menu>9:
        print("El elemento ingresado no corresponde con ninguna de las opciones, observa bien el menú e intenta de nuevo.")
        continue


    if opcion_menu==1:
        print("\n"+"Haz escogido agregar producto, para hacerlo debes llenar la información que vamos a solicitar a continuación\n" \
        "Lee correctamente las instrucciones.")
        nombre_ingresar=input("Ingresa el nombre del producto: ").strip().capitalize()        
        while True:
            precio=input("Ingresa el costo unitario del objeto antes mencionado: ")
            try:
                precio=float(precio)
                if precio<0:
                    print("El precio no puede ser negativo, intenta de nuevo.")
                    continue
                break
            except:
                print("El dato ingresado no corresponde con algún precio, intenta de nuevo.")
            continue
        while True:
            cantidad=input("Ingresa la cantidad de unidades del objeto antes mencionado: ")
            try:
                cantidad=int(cantidad)
                if cantidad<0:
                    print("La cantidad no puede ser negativa, intenta de nuevo.")
                    continue
                break
            except:
                print("El dato ingresado no corresponde con la información solicitada, intenta de nuevo.")
            continue
        ms.agregar_producto(inventario, nombre_ingresar, precio, cantidad)
        print(f"El producto {nombre_ingresar} ha sido ingresado de manera exitosa al sistema, seras redireccionado al menú principal\n")


    elif opcion_menu==2:
        print("\n"+"Haz escogido mostrar inventario, a continuación se mostrara los datos encontrados:")
        ms.mostrar_inventario(inventario)
        print("\n"+"Se ha terminado la acción seleccionada, Seras redirigido al menú principal\n")


    elif opcion_menu==3:
        print("\n"+"Haz escogido buscar producto, a continuación se solicitara el nombre del producto a buscar:\n")
        nombre_buscar=input("Ingresa el nombre del producto a buscar: ").strip().capitalize()
        producto_encontrado=ms.buscar_producto(inventario, nombre_buscar)
        if producto_encontrado==None:
            print("\n"+f"El producto {nombre_buscar} no se encuentra actualmente en el inventario.")
        else:
            print(f"El producto {nombre_buscar} exite en el inventario, datos: \n")
            print(f"Nombre: {producto_encontrado['nombre']}\nPrecio: {producto_encontrado['precio']}\nCantidad: {producto_encontrado['cantidad']}\n")
        print("\n"+"Se ha terminado la acción seleccionada, Seras redirigido al menú principal\n")


    elif opcion_menu==4:
        print("\n"+"Haz escogido actualizar producto, a continuación se solicitara el nombre del producto a actualizar:")
        nombre_actualizar=input("Ingresa el nombre del producto a actualizar: ").strip().capitalize()
        producto_encontrado=ms.buscar_producto(inventario, nombre_actualizar)
        if producto_encontrado==False:
            print(f"\n"+"El producto {nombre_actualizar} no se encuentra actualmente en el inventario.")
        else:
            while True:
                nuevo_precio=input("Ingresa el nuevo precio del producto (deja en blanco si no deseas cambiarlo): ")
                if nuevo_precio=="":
                    nuevo_precio=None
                    break
                try:
                    nuevo_precio=float(nuevo_precio)
                    if nuevo_precio<0:
                        print("El precio no puede ser negativo, intenta de nuevo.")
                        continue
                    break
                except:
                    print("El dato ingresado no corresponde con algun precio, intenta de nuevo.")
                continue
            while True:
                nueva_cantidad=input("Ingresa la nueva cantidad del producto (deja en blanco si no deseas cambiarlo): ")
                if nueva_cantidad=="":
                    nueva_cantidad=None
                    break
                try:
                    nueva_cantidad=int(nueva_cantidad)
                    if nueva_cantidad<0:
                        print("La cantidad no puede ser negativa, intenta de nuevo.")
                        continue
                    break
                except:
                    print("El dato ingresado no corresponde con la información solicitada, intenta de nuevo.")
                continue
            ms.actualizar_producto(inventario, nombre_actualizar, nuevo_precio, nueva_cantidad)
            print(f"\n"+"El producto {nombre_actualizar} ha sido actualizado de manera exitosa en el sistema, seras redireccionado al menú principal")


    elif opcion_menu==5:
        print("\n"+"Haz escogido eliminar producto, a continuación se solicitara el nombre del producto a eliminar:")
        nombre_eliminar=input("Ingresa el nombre del producto a eliminar: ").strip().capitalize()
        producto_encontrado=ms.buscar_producto(inventario, nombre_eliminar)
        if producto_encontrado==False:
            print("\n"+f"El producto {nombre_eliminar} no se a podido eliminar porque no existe en el inventario, eras redireccionado al menú principal")
        else:
            inventario.remove(producto_encontrado)
            print("\n"+f"El producto {nombre_eliminar} ha sido eliminado de manera exitosa del sistema, seras redireccionado al menú principal")


    elif opcion_menu==6:
        print("\n"+"Haz escogido estadísticas generales, a continuación se mostrara en pantalla la información correspondiente")
        estadisticas=ms.calcular_estadisticas(inventario)
        print(f"Unidades totales en el sistema: {estadisticas["unidades_totales"]}\n"
            f"Costo total del inventario: {estadisticas["valor_total"]}\n"
            f"El producto más costos en el sistema es: {estadisticas["producto_mas_caro"]}\n"
            f"EL producto con más unidades disponibles es: {estadisticas["producto_mayor_stock"]}")
        print("\n"+"Se ha terminado la acción seleccionada, Seras redirigido al menú principal")


    elif opcion_menu==7:
        print("\n"+"Haz escogido actualizar CSV, para hacerlo debes llenar la información que vamos a solicitar a continuación" \
        "Lee correctamente las instrucciones.")
        ruta=input("Ingrese la ruta donde esta el archivo CSV a actualizar (puedes mirar la ruta dando click derecho al documento):\n")
        if ar.guardar_csv(inventario, ruta)!=None:
            print(f"La informacíón ha sido correctamente en el archivo CSV ubicado en la ruta: {ruta}")
        print("\n"+"Se ha terminado la acción seleccionada, Seras redirigido al menú principal\n")


    elif opcion_menu==8:
        print("\n"+"Haz escogido cargar CSV, para hacerlo debes llenar la información que vamos a solicitar a continuación\n")
        ruta=input("Ingrese la ruta donde esta el archivo CSV (puedes mirar la ruta dando click derecho al documento): ")
        inventario_temporal, filas_invalidas=ar.cargar_csv(ruta)

        if inventario_temporal!=[]:
            
            opcion_sobreescribir=input("El archivo ha sido leído de manera exitosa.\n ¿Deseas sobreescribir el inventario actual? Si(S)/No(N): \n" \
            "\n--Al escoger la opción si se reemplazara todo el inventario actual por el contenido del archivo leído\n"
            "--Al escoger la opción no se mantendra el inventario actual, pero se añadiran los productos en el documento que no existan actualmente\n" \
            ", además, se actualizaran los productos ya exitentes con los precios del archivo y se añadiran las unidades indicadas en este\n."
            "\nDigite la opción escogida: ").strip().capitalize()

            if opcion_sobreescribir=="S" or opcion_sobreescribir=="Si":
                inventario=inventario_temporal
                print("El inventario ha sido sobreescrito correctamente, ha sido reemplazo por el documento cargado.")

            elif opcion_sobreescribir=="N" or opcion_sobreescribir=="No":
                for item_temporal in inventario_temporal:
                    item_inventario=ms.buscar_producto(inventario, item_temporal["nombre"])
                    if item_inventario==None:
                        inventario.append(item_temporal)
                    else:
                        if item_inventario["precio"]!=item_temporal["precio"]:
                            ms.actualizar_producto(inventario, item_temporal["nombre"], item_temporal["precio"])
                        if item_inventario["cantidad"]==item_temporal["cantidad"]:
                            ms.actualizar_producto(inventario, item_temporal["nombre"], None, item_inventario["cantidad"]+item_inventario["cantidad"])
                print("Se ha actualizado el inventario con la información util del archivo CSV.")
                    
            print("A continuación se mostrara el estado actual del inventario, despues de los cambios implementados:")
            ms.mostrar_inventario(inventario)

            if filas_invalidas!=0:
                print(f"No se han modificado y/o añadido {filas_invalidas} productos, debido a que eran lineas incompatibles con el formato del inventario, \
                revisar el contenido dentro del CSV si se desea su implementación.")
            print("\n"+"Se ha terminado la acción seleccionada, Seras redirigido al menú principal")


    elif opcion_menu==9:
        print("Haz salido corrctamente del sistema, vuelva pronto.")
        break