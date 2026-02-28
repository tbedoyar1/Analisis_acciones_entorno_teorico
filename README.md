# Analisis_acciones_entorno_teorico
Este codigo analiza una matriz de 10 acciones y el rendimiento que han tenido en los 365 dias del año, esta en un enotrno de prueba ideal, la idea es poner en practica lectura de matrices y algoritmos de tendencia en ccodigo, esto poniendo en practica la logica de programacion y el uso de la IA para la creacion del mismo

Este proyecto cuetna solamente con 2 archivos
-> creador_csv.py = crea una matriz aleatoria de acciones con precios aleatorios y lo genera en un documento .csv
-> leer_matriz.py = aqui adentro es donde estan todas las funciones del codigo, desde la de leer la matriz hasta la del analisis de tendenciasa y la interaccion con el usuario

Al seguir siendo solamente un prototipo no cuenta con interfaz grafica, pero en un futuro podria implementarla


# 📈 Analizador de Tendencias del Mercado

---

## 📌 Descripción

Este proyecto es un prototipo desarrollado en **Python** que permite analizar tendencias de acciones a partir de un archivo CSV con precios históricos (365 días).

El sistema calcula probabilidades de subida y bajada en un período determinado, permitiendo analizar:

- 📊 El mercado completo  
- 📈 Una acción específica  

El objetivo es aplicar análisis estadístico básico sobre datos históricos de precios.

---

## 🧠 Flujo del Programa

El programa sigue el siguiente flujo lógico:

1. El usuario ingresa el **día actual** (1–365).
2. Selecciona el **período de análisis**:
   - Última semana (7 días)
   - Último mes (30 días)
   - Período personalizado
3. Elige el tipo de análisis:
   - Mercado general
   - Acción específica
4. El sistema calcula:
   - Probabilidad de subida
   - Probabilidad de bajada
5. Se muestran los resultados en formato de tabla comparativa.

---

## 📂 Formato del Archivo CSV

El archivo `acciones.csv` debe tener la siguiente estructura:

```csv
Nombre,Día1,Día2,Día3,...,Día365
Apple,150.2,151.8,149.7,...
Intel,30.5,30.8,31.1,...
Nike,120.3,121.0,119.8,...
```

### Requisitos

- La primera columna debe contener el **nombre de la acción**.
- Las columnas siguientes deben contener los **precios diarios**.
- Se asume un total de **365 días por acción**.

---

## ⚙️ Estructura del Código

El proyecto está organizado en un solo archivo Python con la siguiente estructura:

```python
- Funciones
    - cargar_datos()
    - analizar_tendencia()
    - pedir_dia_actual()
    - pedir_periodo()
    - analizar_mercado()
    - mostrar_tabla_tendencias()

- Bloque principal:
    if __name__ == "__main__":
```

Esto garantiza una estructura limpia y modular.

---

## 🔎 Funciones Principales

### 📥 cargar_datos(ruta_archivo)

Carga el archivo CSV y lo convierte en:

- `nombres` → Lista con los nombres de las acciones.
- `P` → Matriz de precios (lista de listas).

Devuelve:

```python
nombres, P
```

---

### 📊 analizar_tendencia(precios, inicio, fin)

Calcula la probabilidad de subida y bajada dentro de un rango de días.

**Parámetros:**

- `precios`: lista de precios de una acción.
- `inicio`: día inicial (1–365).
- `fin`: día final (1–365).

**Devuelve:**

```python
(prob_subida, prob_bajada)
```

Las probabilidades se expresan en porcentaje (%).

---

### 📅 pedir_dia_actual()

Solicita al usuario el día actual validando que:

- Sea un número entero.
- Esté entre 1 y 365.

---

### ⏳ pedir_periodo(dia_actual)

Permite seleccionar el período de análisis:

- Última semana
- Último mes
- Período personalizado

Devuelve:

```python
(inicio, fin)
```

---

### 🌎 analizar_mercado(nombres, P, inicio, fin)

Analiza todas las acciones y genera una lista de resultados con:

- Nombre
- Probabilidad de subida
- Probabilidad de bajada

---

### 📋 mostrar_tabla_tendencias(resultados, inicio, fin)

Genera una tabla comparativa ordenada:

- Columna izquierda → Mayor probabilidad de bajada (**VENDE**)
- Columna derecha → Mayor probabilidad de subida (**COMPRA**)

Ejemplo:

```
==============================================
Tendencias Día 48 - Día 55
==============================================

VENDE                    COMPRA
---------------------------------------------
Apple (43%)              Intel (47%)
Nike (41%)               Nvidia (35%)
```

---

## 📐 Método de Cálculo

La probabilidad se calcula mediante la siguiente fórmula:

```
Probabilidad = (Cantidad de días con subida o bajada / Total de comparaciones) × 100
```

Se basa únicamente en análisis estadístico histórico dentro del rango seleccionado.

No realiza predicciones futuras ni modelos de machine learning.

---

## 🚀 Cómo Ejecutar el Proyecto

1. Instalar Python 3.
2. Colocar `acciones.csv` en el mismo directorio del archivo `.py`.
3. Ejecutar en terminal:

```bash
python nombre_del_archivo.py
```

4. Seguir las instrucciones en pantalla.

---

## 📌 Estado del Proyecto

✔ Prototipo funcional  
✔ Validación de entradas  
✔ Análisis por período  
✔ Mercado general o acción individual  
✔ Presentación estructurada de resultados  

---

## 🔮 Posibles Mejoras Futuras

- 📊 Implementar gráficos de tendencias.
- 📈 Agregar medias móviles.
- 📉 Calcular volatilidad y desviación estándar.
- 💾 Exportar resultados a CSV.
- 🖥 Crear interfaz gráfica.
- 🤖 Incorporar modelos predictivos.

---

## 👨‍💻 Autor

Proyecto desarrollado como prototipo académico para análisis estadístico básico del mercado de acciones utilizando Python.
