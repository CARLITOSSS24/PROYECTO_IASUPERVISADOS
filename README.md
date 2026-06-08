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

### 4. Guion para el Video (Enfoque en la Rúbrica)

Para sacar los **5 puntos** en la rúbrica, asegúrate de tocar estos puntos en los 5 minutos:

1.  **Conceptos (1 min):** "Hola, somos Carlos y Manuel. Hoy presentamos el modelo de aprendizaje supervisado. Basándonos en el capítulo 17 de Palma Méndez, implementamos un Árbol de Decisión. La diferencia fundamental con el modelo anterior es que aquí tenemos una variable objetivo (etiquetada) que permite al modelo aprender patrones de causalidad."
2.  **Diseño (2 min):** Muestra el código en pantalla. "Utilizamos `train_test_split` para validar nuestro modelo, asegurando que no memorice los datos, sino que aprenda reglas generalizables."
3.  **Contenido (2 min):** "Aquí vemos la regla de decisión generada: el modelo concluye que si los incidentes superan X cantidad, la estación entra automáticamente en estado de retraso crítico. Esto permite a la gerencia del transporte tomar medidas preventivas antes de que ocurra el colapso."

### Consejo final para los commits:
Como el docente busca evidencia en el **log del repositorio**, haz que tú realices un commit (ej. "Add decision tree logic") y que Manuel realice otro pequeño commit (ej. "Refine documentation in README"), así el log mostrará actividad de ambos.

¿Quieres que te genere el código de Python (`modelo_arbol.py`) para esta parte supervisada?
