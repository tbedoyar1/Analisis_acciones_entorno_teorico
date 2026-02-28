import csv
import random

NUM_ACCIONES = 10
NUM_DIAS = 365

archivo = "acciones.csv"

with open(archivo, mode="w", newline="") as f:
    writer = csv.writer(f)
    
    # Crear encabezado
    encabezado = ["nombre"] + [f"dia{i+1}" for i in range(NUM_DIAS)]
    writer.writerow(encabezado)
    
    for i in range(NUM_ACCIONES):
        nombre_accion = f"ACCION_{i}"
        
        precios = []
        
        # Precio inicial aleatorio entre 50 y 200
        precio = random.uniform(50, 200)
        
        for _ in range(NUM_DIAS):
            # Simulamos variación diaria pequeña
            cambio = random.uniform(-2, 2)
            precio += cambio
            
            # Evitamos precios negativos
            if precio < 1:
                precio = 1
            
            precios.append(round(precio, 2))
        
        writer.writerow([nombre_accion] + precios)

print("Archivo acciones.csv creado correctamente.")