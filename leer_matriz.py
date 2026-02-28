import csv

def cargar_datos(ruta_archivo):
    P = []          # Matriz de precios
    nombres = []    # Lista de nombres
    
    with open(ruta_archivo, mode="r") as f:
        lector = csv.reader(f)
        
        encabezado = next(lector)  # Saltamos la primera fila
        
        for fila in lector:
            nombre = fila[0]
            precios = [float(valor) for valor in fila[1:]]
            
            nombres.append(nombre)
            P.append(precios)
    
    return nombres, P


#Ahora proseguiremos a la funcion de probabilidad de subida y de bajada


def analizar_tendencia(precios, inicio, fin):
    """
    precios: lista de precios de una acción
    inicio: día inicial (1–365)
    fin: día final (1–365)
    """

    # Convertimos a índices de Python
    inicio_idx = inicio - 1
    fin_idx = fin - 1

    dias_subida = 0
    dias_bajada = 0
    dias_neutros = 0

    # Recorremos desde inicio hasta fin-1
    for i in range(inicio_idx, fin_idx):
        if precios[i+1] > precios[i]:
            dias_subida += 1
        elif precios[i+1] < precios[i]:
            dias_bajada += 1
        else:
            dias_neutros += 1

    total_comparaciones = fin_idx - inicio_idx

    if total_comparaciones == 0:
        return 0, 0

    prob_subida = (dias_subida / total_comparaciones) * 100
    prob_bajada = (dias_bajada / total_comparaciones) * 100

    return round(prob_subida, 2), round(prob_bajada, 2)


#testeo de las funciones

#nombres, P = cargar_datos("acciones.csv")

# Prueba con acción 0
#prob_subida, prob_bajada = analizar_tendencia(P[0], 50, 80)

#print("Probabilidad subida:", prob_subida, "%")
#print("Probabilidad bajada:", prob_bajada, "%")




#funcion para pedir al usuario dia actual

def pedir_dia_actual():
    while True:
        try:
            dia = int(input("Ingrese el día actual (1-365): "))
            
            if 1 <= dia <= 365:
                return dia
            else:
                print("❌ Error: El día debe estar entre 1 y 365.\n")
        
        except ValueError:
            print("❌ Error: Debe ingresar un número entero.\n")

#testeo de la funcion

#dia_actual = pedir_dia_actual()
#print("Día seleccionado:", dia_actual)



#funcion de periodo a analizar

def pedir_periodo(dia_actual):
    while True:
        print("\nSeleccione el período de análisis:")
        print("1) Última semana (7 días)")
        print("2) Último mes (30 días)")
        print("3) Período personalizado")
        
        opcion = input("Opción: ")

        if opcion == "1":
            inicio = max(1, dia_actual - 7)
            fin = dia_actual
            return inicio, fin
        
        elif opcion == "2":
            inicio = max(1, dia_actual - 30)
            fin = dia_actual
            return inicio, fin
        
        elif opcion == "3":
            try:
                inicio = int(input("Ingrese día de inicio (1-365): "))
                fin = int(input("Ingrese día de fin (1-365): "))
                
                if 1 <= inicio < fin <= 365:
                    return inicio, fin
                else:
                    print("❌ Rango inválido. Asegúrese de que 1 ≤ inicio < fin ≤ 365.\n")
            
            except ValueError:
                print("❌ Debe ingresar números enteros.\n")
        
        else:
            print("❌ Opción inválida. Intente nuevamente.\n")


    #prubando la funcion

#    dia_actual = pedir_dia_actual()
#inicio, fin = pedir_periodo(dia_actual)

#print(f"\nSe analizará del día {inicio} al día {fin}")


#funcion para analizar todo el mercado

def analizar_mercado(nombres, P, inicio, fin):
    resultados = []

    for i in range(len(nombres)):
        prob_subida, prob_bajada = analizar_tendencia(P[i], inicio, fin)
        
        resultados.append({
            "nombre": nombres[i],
            "subida": prob_subida,
            "bajada": prob_bajada
        })

    return resultados


#funcion para la creacion de la tabla de las accoines

def mostrar_tabla_tendencias(resultados, inicio, fin):
    
    # Ordenar para VENDE (mayor bajada primero)
    ranking_bajada = sorted(resultados, key=lambda x: x["bajada"], reverse=True)
    
    # Ordenar para COMPRA (mayor subida primero)
    ranking_subida = sorted(resultados, key=lambda x: x["subida"], reverse=True)

    print("\n==============================================")
    print(f"Tendencias Día {inicio} - Día {fin}")
    print("==============================================\n")

    print(f"{'VENDE':<25} {'COMPRA'}")
    print("-" * 45)

    for i in range(len(resultados)):
        vende = f"{ranking_bajada[i]['nombre']} ({ranking_bajada[i]['bajada']}%)"
        compra = f"{ranking_subida[i]['nombre']} ({ranking_subida[i]['subida']}%)"
        
        print(f"{vende:<25} {compra}")


#testeo de las funciones

if __name__ == "__main__":

    nombres, P = cargar_datos("acciones.csv")

    dia_actual = pedir_dia_actual()
    inicio, fin = pedir_periodo(dia_actual)

    print("\n¿Qué deseas analizar?")
    print("1) Mercado general")
    print("2) Acción específica")

    opcion = input("Opción: ")

    if opcion == "1":
        resultados = analizar_mercado(nombres, P, inicio, fin)
        mostrar_tabla_tendencias(resultados, inicio, fin)

    elif opcion == "2":
        print("\nAcciones disponibles:")
        for i, nombre in enumerate(nombres):
            print(f"{i}) {nombre}")
        
        idx = int(input("Seleccione índice de la acción: "))
        
        prob_subida, prob_bajada = analizar_tendencia(P[idx], inicio, fin)

        print("\n==============================================")
        print(f"Tendencias Día {inicio} - Día {fin}")
        print("==============================================\n")
        print(f"{'VENDE':<25} {'COMPRA'}")
        print("-" * 45)
        print(f"{nombres[idx]} ({prob_bajada}%){' ' * 10}{nombres[idx]} ({prob_subida}%)")