import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, classification_report
import os

def main():
    print("--- SISTEMA INTELIGENTE DE TRANSPORTE - APRENDIZAJE SUPERVISADO ---")
    
    try:
        df = pd.read_csv('../dataset/dataset_supervisado.csv')
        print("Dataset cargado exitosamente.")
    except Exception as e:
        print("Error cargando dataset. Verifica la ruta.")
        return

    
    features = ['Pasajeros_Dia', 'Tiempo_Espera_Min', 'Conexiones', 'Buses_Hora', 'Incidentes_Mes']
    X = df[features]
    y = df['Estado_Operacion'] 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    
    arbol = DecisionTreeClassifier(max_depth=3, random_state=42)
    arbol.fit(X_train, y_train)

    
    y_pred = arbol.predict(X_test)
    exactitud = accuracy_score(y_test, y_pred)
    print(f"\nExactitud del Modelo: {exactitud * 100}%")
    print("\nReporte de Clasificación:")
    print(classification_report(y_test, y_pred))
    print("\nReglas de Decisión Extraídas del Árbol:")
    reglas = export_text(arbol, feature_names=features)
    print(reglas)

if __name__ == '__main__':
    main()