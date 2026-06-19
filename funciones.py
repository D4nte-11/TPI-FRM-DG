class igualCero(Exception):
    pass
def cargar_paises():
    paises = {}
    try:
        with open("paises.csv", "r", encoding='utf-8') as archivo:
            next(archivo)
        
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) != 4:
                    continue
                nombre = datos[0]
                continente = datos[1]
                poblacion = int(datos[2])
                superficie = int(datos[3])
                paises[nombre] = {"continente": continente, "poblacion": poblacion, "superficie": superficie}
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        return {}
    return paises

def guardar_paises(paises):
    with open("paises.csv", "w", encoding='utf-8') as archivo:
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
    if not paises:
        print("No hay países cargados para buscar.")
        return
    while True:
        actualizar = input("¿Qué país desea editar?: ").strip().title()
        if actualizar in paises:
            parametro_actualizar = input("Ingrese 1 para editar la población o ingrese 2 para editar el superficie: ").strip()
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
                            contador = 1
                            break
                    except ValueError:
                        print("Error: El valor ingresado es incorrecto.")
            case _:
                print("Error: La opción ingresada no es válida.")
                parametro_actualizar = parametro_actualizar = input("Ingrese 1 para editar la población o ingrese 2 para editar el perímetro: ").strip()
        if contador != 0:
            return f'País {actualizar} editado con éxito!'      

def filtrar_paises(paises,continentes):
    if not paises:
        print("No hay países cargados para buscar.")
        return
    filtro = input('''
1. Continente
2. Rango de población
3. Rango de superficie
Ingrese cómo desea filtrar los países: ''').strip()
    while True:
        match filtro:
            case "1":
                encontrado = False
                continente = input("Ingrese el continente por el cual desea filtrar: ").strip().title()
                if continente in continentes:
                    print(f'''
================
|| {continente} ||
================''')
                    for nombre, info in paises.items():
                        if info['continente'] == continente:
                            print(nombre)
                            encontrado = True
                    if not encontrado: print("No existen países en este continente. ")
                    break
                else: print("Error: El continente ingresado no existe.")
            case "2":
                while True:
                    try:
                        encontrado = False
                        rango_pob_min = int(input("Ingrese el mínimo por el que desea buscar: ").strip().replace(",","").replace(".",""))
                        rango_pob_max = int(input("Ingrese el máximo por el que desea buscar: ").strip().replace(",","").replace(".",""))
                        if rango_pob_min >= 0 and rango_pob_max >= 0:
                            print('''  
================
|| Población  ||
================''')
                            for nombre, info in paises.items():
                                if info['poblacion'] >= rango_pob_min and info['poblacion'] <= rango_pob_max:
                                    print(f"{nombre}: {info['poblacion']}")
                                    encontrado = True
                            if not encontrado:
                                print("\nNo se ha encontrado país con ese rango de habitantes. ")
                        else: raise igualCero("Error: El número ingresado debe ser mayor o igual a 0.")
                    except ValueError:
                        print("Error: El valor ingresado no es válido.")
                    except igualCero as e:
                        print(e)
                    else: break
                break
            case "3":
                while True:
                    try:
                        encontrado = False
                        rango_sup_min = float(input("Ingrese el mínimo por el que desea buscar: ").strip())
                        rango_sup_max = float(input("Ingrese el máximo por el que desea buscar: ").strip())
                        if rango_sup_min > 0 and rango_sup_max > 0:
                            print('''
================
|| Superficie ||
================''')
                            for nombre, info in paises.items():
                                if info['superficie'] >= rango_sup_min and info['superficie'] <= rango_sup_max:
                                    print(nombre)
                                    encontrado = True
                            if not encontrado:
                                print("\nNo se ha encontrado país en ese rango de superficie. ")
                        else: raise igualCero("Error: El número ingresado debe ser mayor a 0.") 
                    except ValueError:
                        print("Error: El valor ingresado no es válido.")
                    except igualCero as e:
                        print(e)
                    else: break
                break
            case _:
                print("Error: la opción ingresada no es válida.")
                filtro = input('''
1. Continente
2. Rango de población
3. Rango de superficie
Ingrese cómo desea filtrar los países: ''').strip()
# Create acá abajo las funciones para el 3 5 y 6

def buscar_pais(paises):
    if not paises:
        print("No hay países cargados para buscar.")
        return
    buscar = input('Ingrese el país que desea buscar: ').strip().title()
    encontrado = False
    for nombre, informacion in paises.items():
        if buscar.lower() in nombre.lower():
            print(f'''País: {nombre}
            Continente: {informacion['continente']}
            Población: {informacion['poblacion']}
            Superficie: {informacion['superficie']}
            ''')
            encontrado = True
    if not encontrado:
        print(f"No se encontró ningún país relacionado con '{buscar}'. ")

def orden():
    orden = input("¿Orden descendente? (s/n): ").strip().lower()
    reverse = True if orden == 's' else False
    return reverse

def ordenar_paises(paises):
    if not paises:
        print("No hay países cargados para ordenar.")
        return
    while True:
        contador = 0
        campo= input('''Ordenar por:
    1) Nombre
    2) Población
    3) Superficie
    Elija una opción: ''').strip()
        
        match campo:
            case '1':
                items = sorted(paises.items(), key=lambda x: x[0], reverse=orden())
            case '2':
                items = sorted(paises.items(), key=lambda x: x[1]["poblacion"], reverse=orden())
            case '3':
                items = sorted(paises.items(), key=lambda x: x[1]["superficie"], reverse=orden())
            case _:
                print("Error: La opción no es válida. ")
                contador += 1
        if contador == 0:
            print("\nListado de países ordenado:")
            for nombre, info in items:
                print(f"{nombre} - {info['continente']} - Población: {info['poblacion']} - Superficie: {info['superficie']}")
            break

def mostrar_estadisticas(paises):
    if not paises:
        print("No hay países cargados para mostrar estadísticas.")
        return
    
    continentes = {'Europa':0, 'America':0, 'Asia':0, 'Africa':0, 'Oceania':0}

    for info in paises.values():
        continentes[info['continente']] += 1

    total_paises = len(paises)
    suma_poblacion = sum(info['poblacion'] for info in paises.values())
    suma_superficie = sum(info['superficie'] for info in paises.values())

    promedio_poblacion = suma_poblacion / total_paises
    promedio_superficie = suma_superficie / total_paises

    pais_mas_poblado = max(paises.items(), key=lambda x: x[1]['poblacion'])[0]
    pais_menos_poblado = min(paises.items(), key=lambda x: x[1]['poblacion'])[0]

    print(f'''\nEstadísticas generales: 
            Total de países: {total_paises}
            Países por continente:
                Europa: {continentes['Europa']}
                América: {continentes['America']}
                Asia: {continentes['Asia']}
                África: {continentes["Africa"]}
                Oceania: {continentes["Oceania"]}
            Población total: {suma_poblacion}
            Promedio de población: {promedio_poblacion:.2f}
            País más poblado: {pais_mas_poblado} ({paises[pais_mas_poblado]['poblacion']})
            País menos poblado: {pais_menos_poblado} ({paises[pais_menos_poblado]['poblacion']})
            Superficie total: {suma_superficie}
            Promedio de superficie: {promedio_superficie:.2f}''')