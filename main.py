from funciones import *
paises = cargar_paises()

print('''
================
|| Bienvenido ||
================''')
while True:
    opcion = input('''
1. Agregar un país nuevo
2. Actualizar población y Superficie de un país
3. Buscar país por Nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Salir
Introduzca una opción: ''')

    match opcion:
        case "1":
            print(agregar_pais(paises,  continentes=['Europa', 'America', 'Asia', 'Africa', 'Oceania']))
            guardar_paises(paises)
        case "2":
            print(actualizar_pais(paises))
            guardar_paises(paises)
        case "3":
            buscar_pais(paises)
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("Gracias por usar nuestro programa. Hasta luego!")
            break
        case _:
            print("Error: la opción ingresada no es válida.")