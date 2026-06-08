# PROYECTO_IASUPERVISADOS
---

### 3. Estructura Documental (Para los PDFs)

#### A. Documento: `descripcion_datos.pdf`
Debes enfatizar la diferencia clave del aprendizaje supervisado: la **Variable Objetivo**.

1.  **Portada:** Igual a la anterior (nombres, docente, fecha).
2.  **Definición del Problema:** Explicación de por qué usamos Árboles de Decisión: "Buscamos un modelo interpretable que permita a los operadores de transporte entender qué factores (incidentes, tiempos de espera) desencadenan un 'Retraso Crítico'".
3.  **Diccionario de Datos:** * Incluye las variables anteriores (Pasajeros, Tiempo, etc.).
    * **Nueva Variable (Target):** `Estado_Operacion` (0: Normal, 1: Crítico). Explica que esta columna es la que "supervisa" el aprendizaje del modelo.

#### B. Documento: `pruebas_componente.pdf`
Este documento debe mostrar que el modelo realmente "aprendió".

1.  **Metodología:** Explica que dividiste los datos en **Entrenamiento (Training)** y **Prueba (Test)**.
2.  **Resultados:**
    * **Exactitud (Accuracy):** Incluye el porcentaje que te arroje el código.
    * **Reglas de Decisión:** Esta es la parte más importante del Capítulo 17. Copia la salida que genera `export_text` en Python. Se verá algo como:
      ```text
      |--- Incidentes_Mes <= 10.50
      |   |--- clase: 0
      |--- Incidentes_Mes > 10.50
      |   |--- clase: 1
      ```
    * **Conclusión:** Explica cómo el árbol de decisión creó estas reglas automáticamente para clasificar las estaciones.

---
