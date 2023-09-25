# NW4daysChallenge_AtrasoVuelos

# **Análisis del proyecto de Juan sobre Predicción de Atrasos en Vuelos**


Este proyecto se centra en la evaluación y mejora de un modelo de predicción de atrasos de vuelos y su implementación en una interfaz de usuario, con el objetivo de poner a prueba su eficiencia mediante una API REST y un test de estrés.

**Introducción:**
Durante el desarrollo de este proyecto, se llevaron a cabo diversas tareas de análisis de datos y modelado con el objetivo de predecir atrasos en vuelos. Se exploraron los datos iniciales y se aplicaron varias técnicas de procesamiento, incluyendo la construcción de nuevos atributos y la estandarización de los datos. Además, se probaron varios modelos de aprendizaje automático, se ajustaron hiperparámetros y se evaluaron sus resultados. Este es un notebook de investigación basado en lo creado por Juan y budcó expandir ciertos aproaches que Juan n cubrió, en especial, implementar técnicas distintas en lso modelos utilzados e intepretaciones especificas, se detalla el proceso seguido y se presentan los resultados obtenidos. A modo de guía se sugiere focalizar el Notebook en 3 fases. 

* La primera: exploratoria con mpdificaciones en los datos y exposición gráfica simple cmo tablas informativa unicamente.

* la seguna modificación y preparación de los datos (técnicas de regularizacion, encoding, PCA ,etc) 

* y la ultima, probar distintas estratégias con modelos que adhieren mejor aun analisis de clasificación predictorio de caracter preliminar binario como Atraso/no atraso.

**Exploración de Datos:**
Se inició el proyecto realizando una exploración de los datos, identificando características clave y tendencias. Se observó que los datos presentaban desafíos, como el desequilibrio entre las clases de atraso, exceso/ausencia de datos para algunosatributos como algunos destinos y la necesidad de manejar atributos categóricos como dificultad general.

**Preprocesamiento de Datos:**
Para abordar los desafíos, se realizaron los siguientes pasos:

1. **Reconstrucción de Datos:** Se reconstruyeron los datos previamente procesados, mejorando la selección de columnas y descartando aquellas que no eran relevantes.

2. **Construcción de Nuevos Atributos:** Se validó la creación de atributos como "dif_min," que refleja la diferencia máxima entre los tiempos de vuelo planificados y operados, y "atraso_15," un indicador binario de atrasos mayores a 15 minutos. son un buen proxy para el alcance preliminar del proyecto.

3. **One-Hot Encoding:** Para manejar atributos categóricos, se aplicó la técnica de one-hot encoding.

4. **Eliminación de Datos No Relevantes:** Se eliminaron filas con valores alfanuméricos en características específicas, ya que representaban un pequeño porcentaje del conjunto de datos. (Feature: Vlo-I/Vlo-O | 0.02% erased).

**Modelado:**
Se probaron varios modelos de aprendizaje automático, incluyendo Regresión Logística, SVM, y XGBoost. Se realizaron ajustes de hiperparámetros y se aplicaron técnicas de regularización como Lasso y Ridge junto a tunning se sus distintas estratégias para optimizar timepo de procesamiento y resultado esperado. Además, se utilizó la técnica de sobremuestreo SMOTE para abordar el desequilibrio de clases.

**Resultados:**
El modelo final de XGBoost con SMOTE y estandarización mostró mejoras significativas en términos de precisión y recall en comparación con los modelos anteriores. El F1-score balanceado indicó un equilibrio razonable entre precision y recall. La precisión general del modelo fue del 82%, aunque la precisión para la clasificación de "Atraso" sigue siendo un área de mejora pero un rfecall de un 0.78 es un buen paso en la dirección correcta.

### Desafíos Enfrentados

- **Sobreajuste (Overfitting):** Inicialmente, el modelo tenía problemas de sobreajuste, lo que requería ajustes adicionales.

- **Desbalance de Datos:** Los datos presentaban un desbalance entre vuelos a tiempo y con atrasos, lo que afectó la calidad del modelo.

- **Limitaciones de Recursos:** Restricciones de hardware y tiempo de procesamiento limitaron la optimización de hiperparámetros y modelos. Mas tiempo o mas recursos hubieran mejorado este resultado.

## Interfaz de Usuario

Se creó una interfaz de usuario simple en `front.html`, que en teoría permite a los usuarios ingresar información relevante para la predicción, como el operador de vuelo y el mes. Esta interfaz debía de actuar como el punto de entrada para interactuar con el modelo.

### Pendientes y Pasos Sugeridos

A pesar de los avances, aún quedan tareas por completar para alcanzar la meta final:

1. **Implementación de API REST:** El modelo se exportó y serializó en formato .pkl. Sin embargo, persisten problemas técnicos al intentar conectar el modelo a una API REST. Las pruebas en un entorno local (mi notebook) se han realizado, pero la falta de acceso desde el navegador (distintos fueron probados) podría estar relacionada con limitaciones del dispositivo utilizado. Es posible que se requieran configuraciones más avanzadas de computación que están fuera del alcance de este proyecto inicial. Si yo dispusiera de un dispositivo más moderno, se esperaría una implementación exitosa de la API REST. De seguro.

2. **Prueba de Estrés (Stress Test):** Se avanzó en inicializar las herramientas de prueba de estrés utilizando herramientas como [wrk](https://github.com/wg/wrk) para evaluar el rendimiento del sistema bajo una alta carga, con el objetivo de procesar eficientemente al menos 50,000 solicitudes en 45 segundos. Mont´pe le modelo en uin postman para forzar lso reauests pero sin acceso desde mi computador al puerto  'http://127.0.0.1:5000/predecir_atraso' que diseñé en la app.py,, no pujedo hacer la validación del funcxionamiento dle modelo. lamentablemente. ME encantar´pia contarcon el apoyo de alguien mas experto en diseño de sistemas infraestructura a este nivel para verificar su correcto funcionamiento. 

3. **Despliegue en la Nube:** Idealmente, se consideraría desplegar la aplicación en una plataforma en la nube para garantizar su disponibilidad y escalabilidad. Enlo personal, puedo manejar SageMaker, Elastic (de AWS) y he desarrollado pruebas de concepto con Azure web pero me limitan los costos para probar la eficiencia del modelo una vesm ontado y no dispngo de credito para ejecutar tales cloud deployment.

## Próximos Pasos

El proyecto se encuentra en una etapa avanzada, y se espera que se completen las tareas pendientes para lograr una solución funcional y eficiente. La implementación de la API REST y la prueba de estrés son muchisimo mas sencillas de implementar y resolver que mejorar la precisión y fitness de un modelo o búsqueda de mejores datos, feature engineering, etc. Por lo que me gustaría completar este proceso y ver como optimizarlo y automatizarlo. Creo que son pasos cruciales para demostrar la capacidad del modelo en un entorno real.


**Conclusión:**
En resumen, este proyecto involucró un proceso completo de exploración, preprocesamiento y modelado de datos para predecir atrasos en vuelos. Hubo varios cambios de dirección en su desarrollo, como la prueba con otros modelos que no se adjuntaron por entregar nulo valor analítico. pero sirvió como referencia y descarte del tipo de objetivo del analisis y el tipo de variables en juego. Si bien con XGboost se lograron mejoras notables en la precisión y el recall luego de realizar multiples ocmvbinaciones de otras técnicas y 'tuneo', todavía existen oportunidades para ajustes adicionales y mejoras en la detección de atrasos. como ejercicio y mqueteo, el proyecto representa un avance significativo en la dirección correcta y sienta las bases para futuros desarrollos y refinamientos una ves se seleccione un dataset de optima calidad y un objetivo conciso a explorar bajo los algoritmos preliminares.

**Librerías Claves Utilizadas:**
- Pandas
- Scikit-learn
- XGBoost
- Imbalanced-learn (SMOTE)
- Matplotlib
- Seaborn

**Duración del Proyecto:**
El proyecto se realizó en un total de aproximadamente 8-9 horas distribuidas en varias sesiones de trabajo a lo largo de 4 días efectivos.

# cómo lo corremos?
### PASOS:

Clonemos el repository

```bash
https://github.com/Kokit0/NW4daysChallenge_AtrasoVuelos.git
```
### Crea el entorno (Conda o custom) luego de abrir y cargar el repositorio.

#### en terminal VSCode (o tu Git BASH en la carpeta donde descargues el proyecto)
```bash
python -m venv NWMLEMLOPSenv
```
#### Recuerda activar tu entorno!
```bash
NWMLEMLOPSenv/Scripts/activate
```

### Instalar dependencias
Estas son dependencias basales para correr el modelo desde un repositorio con u sistema de folder y files mas  desarrollado. para ver el modelo en ejecución en modo prueba, lo mas simple es activar un entorno y verlo directamente en el .ipynb E:\OneDrive\Documents\nw4dayschallenge\NW4daysChallenge_AtrasoVuelos\notebooks\Challenge_NW_MLE_MLOPS_Atraso_vuelos_v2.ipynb 

```
pip install -r .\requirements.txt
```

### Ejecutar generador_Templado.py (si deseas una instancia limpia custom)
Este templado es una herramienta quer cree para generar el sistema decarpetas inicial sobre le cual sep uede iterar en el mismo reposssitorio copiado en su propia IDE. es solamente un headstart y permite comenxzar a organisar el repositorio para mayores systematizaciones. En otro ptroyecto qu estoy desarrollando en paralelo a este, he creado un end to end con MLFlow que explora mucho mas a fondo la generación de estos templados de kickstart. por ahora lo usaré como prueba de concepto funcional.

```python
python Generador_Template.py  
```

### Actualizar dataset segun predilección. En nuestro caso utilizaremos 'dataset_SCL.csv'
https://github.com/Kokit0/NW4daysChallenge_AtrasoVuelos/raw/main/data/dataset_SCL.csv

### Ejecutemos la app Flask (app.py)

```python
python app.py
```

## Interfaz de Usuario

