
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

def actualizar_pais(paises):
    while True:
        actualizar = input("¿Qué país desea editar?: ").strip().title()
        if actualizar.replace(" ","") in paises:
            parametro_actualizar = input("Ingrese 1 para editar la población o ingrese 2 para editar el perímetro: ").strip()
            break
        else: print(f"Error: {actualizar} no se encuentra en el listado de países.")
    while True:
        contador = 0
        match parametro_actualizar:
            case "1":
                while True:
                    try:
                        poblacion_nueva = int(input(f"Ingrese la nueva población de {actualizar}: ").strip().replace(",","").replace(".",""))
                        if poblacion_nueva >= 0:
                            paises[actualizar]["poblacion"] = poblacion_nueva
                            contador = 1
                            break
                        else: print("Error: El valor ingresado debe ser mayor o igual a 0.")
                    except ValueError:
                        print("Error: El valor ingresado es incorrecto.")
            case "2":
                while True:
                    try:
                        superficie_nueva = float(input(f"Ingrese la nueva superficie de {actualizar}: "))
                        if superficie_nueva > 0:
                            paises[actualizar]["superficie"] = superficie_nueva
                            break
                    except ValueError:
                        print("Error: El valor ingresado es incorrecto.")
            case _:
                print("Error: La opción ingresada no es válida.")
                parametro_actualizar = parametro_actualizar = input("Ingrese 1 para editar la población o ingrese 2 para editar el perímetro: ").strip()
        if contador != 0:
            return f'País {actualizar} editado con éxito!'


# Create acá abajo las funciones para el 3 5 y 6

def buscar_pais(paises):
    if not paises:
        print("No hay países cargados para buscar.")
        return
    buscar = input('Ingrese el país que quiere buscar (coincidencia exacta): ').strip()
    if buscar in paises:
        informacion = paises[buscar]
        print(f'''País: {buscar}
        Continente: {informacion['continente']}
        Población: {informacion['poblacion']}
        Superficie: {informacion['superficie']}
        ''')
    else:
        print(f"No se encontró el país '{buscar}'. La búsqueda exige coincidencia exacta.")

def ordenar_paises(paises):
    if not paises:
        print("No hay países cargados para ordenar.")
        return

    print("Ordenar por:\n1) Nombre\n2) Población\n3) Superficie")
    campo = input("Elija campo (1-3): ").strip()
    orden = input("¿Orden descendente? (s/N): ").strip().lower()
    reverse = True if orden == 's' else False

    if campo == '1':
        items = sorted(paises.items(), key=lambda x: x[0], reverse=reverse)
    elif campo == '2':
        items = sorted(paises.items(), key=lambda x: x[1]["poblacion"], reverse=reverse)
    elif campo == '3':
        items = sorted(paises.items(), key=lambda x: x[1]["superficie"], reverse=reverse)
    else:
        print("Opción no válida. Volviendo al menú.")
        return

    print("\nListado de países ordenado:")
    for nombre, info in items:
        print(f"{nombre} - {info['continente']} - Población: {info['poblacion']} - Superficie: {info['superficie']}")

def mostrar_estadisticas(paises):
    if not paises:
        print("No hay países cargados para mostrar estadísticas.")
        return

    total_paises = len(paises)
    suma_poblacion = sum(info['poblacion'] for info in paises.values())
    suma_superficie = sum(info['superficie'] for info in paises.values())

    promedio_poblacion = suma_poblacion / total_paises
    promedio_superficie = suma_superficie / total_paises

    pais_mas_poblado = max(paises.items(), key=lambda x: x[1]['poblacion'])[0]
    pais_menos_poblado = min(paises.items(), key=lambda x: x[1]['poblacion'])[0]
    pais_mayor_superficie = max(paises.items(), key=lambda x: x[1]['superficie'])[0]
    pais_menor_superficie = min(paises.items(), key=lambda x: x[1]['superficie'])[0]

    print(f'''\nEstadísticas generales: 
            Total de países: {total_paises}
            Población total: {suma_poblacion}
            Población promedio por país: {promedio_poblacion:.2f}
            País más poblado: {pais_mas_poblado} ({paises[pais_mas_poblado]['poblacion']})
            País menos poblado: {pais_menos_poblado} ({paises[pais_menos_poblado]['poblacion']})
            Superficie total: {suma_superficie}
            Promedio De superficie por país: {promedio_superficie:.2f}
            País con mayor superficie: {pais_mayor_superficie} ({paises[pais_mayor_superficie]['superficie']})
            País con menor superficie: {pais_menor_superficie} ({paises[pais_menor_superficie]['superficie']})
        ''')