# Analisis_acciones_entorno_teorico
Este codigo analiza una matriz de 10 acciones y el rendimiento que han tenido en los 365 dias del año, esta en un enotrno de prueba ideal, la idea es poner en practica lectura de matrices y algoritmos de tendencia en ccodigo, esto poniendo en practica la logica de programacion y el uso de la IA para la creacion del mismo

Este proyecto cuetna solamente con 2 archivos
-> creador_csv.py = crea una matriz aleatoria de acciones con precios aleatorios y lo genera en un documento .csv
-> leer_matriz.py = aqui adentro es donde estan todas las funciones del codigo, desde la de leer la matriz hasta la del analisis de tendenciasa y la interaccion con el usuario

Al seguir siendo solamente un prototipo no cuenta con interfaz grafica, pero en un futuro podria implementarla

nalizador de Tendencias del Mercado (Prototipo)
📌 Descripción

Este proyecto es un prototipo en Python que analiza tendencias de acciones a partir de un archivo CSV con precios históricos (365 días).

El sistema permite:

Seleccionar el día actual.

Elegir un período de análisis (semana, mes o personalizado).

Analizar el mercado completo o una acción específica.

Obtener probabilidades de subida y bajada en forma de tabla comparativa.

El objetivo es ofrecer una herramienta simple pero funcional para estudiar tendencias estadísticas básicas del mercado.

🧠 Lógica del Programa

El flujo del programa es el siguiente:

El usuario ingresa el día actual (1–365).

Selecciona el período a analizar.

Elige si desea analizar:

Mercado general

Una acción específica

El sistema calcula:

Probabilidad de subida

Probabilidad de bajada

Se muestran los resultados en formato de tabla.

📂 Estructura del Archivo CSV

El archivo acciones.csv debe tener el siguiente formato:

Nombre,Día1,Día2,Día3,...,Día365
Apple,150.2,151.8,149.7,...
Intel,30.5,30.8,31.1,...
Nike,120.3,121.0,119.8,...

La primera columna contiene el nombre de la acción.

Las columnas siguientes contienen precios diarios.

Se asume un total de 365 días por acción.

⚙️ Funciones Principales
cargar_datos(ruta_archivo)

Carga el archivo CSV y convierte los datos en:

nombres: lista con los nombres de las acciones.

P: matriz de precios (lista de listas).

Devuelve:

nombres, P
analizar_tendencia(precios, inicio, fin)

Calcula la probabilidad de subida y bajada dentro de un rango de días.

Parámetros:

precios: lista de precios de una acción.

inicio: día inicial (1–365).

fin: día final (1–365).

Devuelve:

(prob_subida, prob_bajada)

Las probabilidades se expresan en porcentaje.

pedir_dia_actual()

Solicita al usuario el día actual validando que:

Sea un número entero.

Esté entre 1 y 365.

pedir_periodo(dia_actual)

Permite seleccionar:

Última semana (7 días)

Último mes (30 días)

Período personalizado

Devuelve:

(inicio, fin)
analizar_mercado(nombres, P, inicio, fin)

Analiza todas las acciones y devuelve una lista de resultados:

[
    {"nombre": "Apple", "subida": 43.2, "bajada": 56.8},
    ...
]
mostrar_tabla_tendencias(resultados, inicio, fin)

Genera una tabla comparativa:

Columna izquierda: acciones con mayor probabilidad de bajada (VENDE).

Columna derecha: acciones con mayor probabilidad de subida (COMPRA).

Ejemplo:

Tendencias Día 48 - Día 55

VENDE                    COMPRA
---------------------------------------------
Apple (43%)              Intel (47%)
Nike (41%)               Nvidia (35%)
🏗 Diseño del Proyecto

Todo el código se encuentra en un solo archivo.

Las funciones están separadas de la ejecución principal.

El flujo principal se encuentra dentro de:

if __name__ == "__main__":

Esto garantiza una estructura limpia y profesional.

📊 Método de Cálculo

La probabilidad se calcula mediante:

Probabilidad=Cantidad de dıˊas con subida o bajadaTotal de comparaciones×100
Probabilidad=
Total de comparaciones
Cantidad de d
ı
ˊ
as con subida o bajada
	​

×100

No se consideran predicciones futuras, únicamente análisis estadístico histórico dentro del rango seleccionado.

🚀 Cómo Ejecutar

Asegúrate de tener Python 3 instalado.

Coloca el archivo acciones.csv en el mismo directorio.

Ejecuta:

python nombre_del_archivo.py

Sigue las instrucciones en pantalla.

📌 Estado del Proyecto

✔ Prototipo funcional
✔ Análisis por período
✔ Mercado completo o acción individual
✔ Validación de entrada
✔ Presentación ordenada de resultados

🔮 Posibles Mejoras Futuras

Agregar gráficos de tendencias.

Implementar análisis con medias móviles.

Exportar resultados a CSV.

Añadir interfaz gráfica.

Incorporar más métricas estadísticas (volatilidad, desviación estándar, etc.).

👨‍💻 Autor: Thomas Bedoya Rendon

Proyecto desarrollado como prototipo académico para análisis estadístico básico del mercado de acciones utilizando Python.
