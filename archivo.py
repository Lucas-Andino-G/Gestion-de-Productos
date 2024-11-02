import os

# Lista para almacenar los productos
productos = []

# Ruta del archivo donde se guardarán los productos
FILE_PATH = "productos.txt"

def cargar_datos():
    """Carga los productos desde el archivo de texto."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(',')
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })

def guardar_datos():
    """Guarda los productos en el archivo de texto."""
    with open(FILE_PATH, 'w') as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados exitosamente.")

def añadir_producto():
    """Añade un nuevo producto a la lista."""
    nombre = input("Ingrese el nombre del producto: ")
    
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")
    
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad disponible: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")
    
    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
    print("Producto añadido exitosamente.")

def ver_productos():
    """Muestra la lista de productos."""
    if not productos:
        print("No hay productos disponibles.")
        return
    print("\nLista de productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    print()

def actualizar_producto():
    """Actualiza un producto existente."""
    nombre = input("Ingrese el nombre del producto que desea actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            nuevo_nombre = input("Ingrese el nuevo nombre del producto (dejar vacío para no cambiar): ")
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            
            while True:
                nuevo_precio = input("Ingrese el nuevo precio del producto (dejar vacío para no cambiar): ")
                if nuevo_precio == "":
                    break
                try:
                    producto['precio'] = float(nuevo_precio)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido para el precio.")
            
            while True:
                nueva_cantidad = input("Ingrese la nueva cantidad (dejar vacío para no cambiar): ")
                if nueva_cantidad == "":
                    break
                try:
                    producto['cantidad'] = int(nueva_cantidad)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido para la cantidad.")
                
            print("Producto actualizado exitosamente.")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    """Elimina un producto de la lista."""
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print("Producto eliminado exitosamente.")
            return
    print("Producto no encontrado.")

def menu():
    """Muestra el menú principal y gestiona las opciones."""
    cargar_datos()  # Cargar datos al iniciar
    while True:
        print("\nGestor de Productos")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()