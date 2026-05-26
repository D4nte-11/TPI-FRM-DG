
def cargar_paises():
    paises = {}
    try:
        with open("paises.csv", "r") as archivo:
            next(archivo)
        
            for linea in archivo:
                datos = linea.strip().split(",")
                nombre = datos[0]
                continente = datos[1]
                poblacion = int(datos[2])
                superficie = float(datos[3])
                paises[nombre] = {"continente": continente, "poblacion": poblacion, "superficie": superficie}
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        pass
    return paises

def guardar_paises(paises):
    with open("paises.csv", "w") as archivo:
        archivo.write("nombre,continente,poblacion,superficie\n")
        for nombre, info in paises.items():
            archivo.write(f"{nombre},{info['continente']},{info['poblacion']},{info['superficie']}\n")

def agregar_pais(paises, continentes):
    try:    
        while True:
            nombre = input("Introduzca el nombre del país: ").strip().title()
            if nombre.replace(" ", "").isalpha():
                if nombre not in paises:
                    break
                else: print("Error: El país ya se encuentra cargado.")
            else: print("Error: El país introducido no es válido.")
        while True:
            continente = input("Ingrese el continente: ").strip().title()
            if continente.isalpha():
                if continente in continentes:
                    break
                else: print(f"Error: El continente introducido no existe, los contintentes existentes son: {continentes}")
            else: print("Error: El continente introducudo no es válido.")
        while True:
            try:
                poblacion = int(input(f"Ingrese la población de {nombre}: ").strip().replace(",","").replace(".",""))
                if poblacion >= 0:
                    break
                else: print("Error: El valor ingresado debe ser mayor a 0.")
            except ValueError:
                print("Error: El valor ingresado no es un número.")
        while True:
            try:
                superficie = float(input(f"Ingrese la superficice de {nombre}: ").strip())
                if superficie > 0:
                    break
                else: print("Error: El valor ingresado debe ser mayor a 0.")
            except ValueError:
                print("Error: El valor ingresado no es un número.")
    except Exception as e:
        print("Ha ocurrido un error inesperado: ", type(e).__name__)
    else:
        paises[nombre] = {'continente':continente,'poblacion':poblacion,'superficie':superficie}
        return f'País {nombre} ha sido agregado correctamente'

# Create acá abajo las funciones para el 3 5 y 6

def buscar_pais(paises):
    print('Buscar paises')
    buscar = input('Ingrese el pais que quiere buscar: ').strip()
    if buscar in paises:
        pass