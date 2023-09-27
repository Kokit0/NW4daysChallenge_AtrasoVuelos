
#########################################################################
#Este es mi Ayudin-Crea-folder structures. versión ultra liviana. ~Kokke#
#########################################################################

import os
import requests

# Definir la estructura de carpetas y archivos
project_structure = {
    'app.py': None,
    'VACIOmodelo_xgboost.pkl': None,
    'requirements.txt': None,
    'api': {
        '__init__.py': None,
        'routes.py': None,
        # Agrega otros nombres de archivos relacionados con la API si es necesario
    },
    'data': {
        'REEMPLAZAME_POR_dataset_SCL.csv': None,
        # Agrega otros nombres de archivos de datos si es necesario
    },
    'notebooks': {
        'Research_notebook01.ipynb': None,
        # Agrega otros nombres de notebooks predefinidos si es necesario
    },
    
}

# Ruta del directorio del proyecto (local donde hayas descargado mi repo github)
# En mi caso...:
project_directory = 'E:/OneDrive/Documents/nw4dayschallenge/NW4daysChallenge_AtrasoVuelos'

# Función para crear la estructura de carpetas y archivos
def create_project_structure(directory, structure):
    for item, children in structure.items():
        item_path = os.path.join(directory, item)
        if children is None:
            # Si no hay hijos, crea un archivo vacío
            with open(item_path, 'w') as file:
                pass
        else:
            # Si hay hijos, crea una carpeta y luego recursivamente crea su estructura
            os.makedirs(item_path, exist_ok=True)
            create_project_structure(item_path, children)

# Crea la estructura de carpetas y archivos en el directorio del proyecto
create_project_structure(project_directory, project_structure)

print("Estructura de carpetas y archivos creada con éxito.")


# Definir el contenido del archivo app.py
app_code = """
from flask import Flask, request, jsonify
import joblib
import requests

# Load the serialized model
modelo = joblib.load('E:\\OneDrive\\Documents\\nw4dayschallenge\\NW4daysChallenge_AtrasoVuelos\\modelo_xgboost.pkl')

# Crear la Flask app
app = Flask(__name__)

@app.route('/predecir_atraso', methods=['POST'])
def predecir_atraso():
    try:
        # Obtener los datos de entrada en formato JSON
        datos = request.json

        # Asegúrate de que los nombres coincidan con los campos del DataFrame de entrada
        OPERA = datos.get('OPERA')
        MES = datos.get('MES')
        TIPOVUELO = datos.get('TIPOVUELO')
        # Agregaría aquí los demás atributos

        # Realizar la predicción con el modelo
        # Por ejemplo, podría pasar estos atributos al modelo para obtener la predicción
        #prediccion = modelo.predict([['OPERA', 'MES', 'TIPOVUELO']])

        # Convertir la predicción a texto ("Atraso" o "No Atraso")
        # etiqueta_prediccion = "Atraso" if prediccion[0] == 1 else "No Atraso"

        # Devolver la respuesta en formato JSON
        # respuesta = {'prediccion': etiqueta_prediccion}
        respuesta = {'OPERA': OPERA, 'MES': MES, 'TIPOVUELO': TIPOVUELO}  # Algo así haría
        return jsonify(respuesta)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

"""

# Ruta donde se creará el archivo app.py
app_file_path = os.path.join(project_directory, 'app.py')

# Crear el archivo app.py con el contenido definido
with open(app_file_path, 'w') as app_file:
    app_file.write(app_code)

print("Archivo app.py creado con éxito.")



# URL del archivo CSV en GitHub
url_csv = "https://github.com/Kokit0/NW4daysChallenge_AtrasoVuelos/raw/main/data/dataset_SCL.csv"

# Directorio donde se encuentra el archivo CSV
data_directory = os.path.join(project_directory, "data")

# Nombre de archivo CSV
csv_filename = "dataset_SCL.csv"

# Ruta completa del archivo CSV local
local_csv_path = os.path.join(data_directory, csv_filename)

# Descargar el archivo CSV desde la URL y guardarlo en la carpeta data
response = requests.get(url_csv)
if response.status_code == 200:
    with open(local_csv_path, 'wb') as file:
        file.write(response.content)
    print(f"Archivo {csv_filename} descargado exitosamente!")
else:
    print(f"No se pudo descargar el archivo!(Tranquilo. Puedes descargarlo manualmente directo del repositorio!) {csv_filename}. Código de estado: {response.status_code}")
