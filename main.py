import funciones as fun
paises = fun.cargar_paises()

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
            print(fun.agregar_pais(paises,  continentes=['Europa', 'America', 'Asia', 'Africa', 'Oceania']))
            fun.guardar_paises(paises)
        case "2":
            print(fun.actualizar_pais(paises))
            fun.guardar_paises(paises)
        case "3":
            fun.buscar_pais(paises)
        case "4":
            fun.filtrar_paises(paises,continentes=['Europa', 'America', 'Asia', 'Africa', 'Oceania'])
        case "5":
            fun.ordenar_paises(paises)
        case "6":
            fun.mostrar_estadisticas(paises)
        case "7":
            print("Gracias por usar nuestro programa. Hasta luego!")
            break
        case _:
            print("Error: la opción ingresada no es válida.")