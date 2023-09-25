
########################################################################
#Este es mi Ayudin-Crea-folder structures. versión ultra liviana.#######
########################################################################

import os


# Definir la estructura de carpetas y archivos
project_structure = {
    'app.py': None,
    'modelo_xgboost.pkl': None,
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

# Load the serialized model
modelo = joblib.load('modelo_xgboost.pkl')

# Create the Flask application
app = Flask(__name__)

@app.route('/predecir_atraso', methods=['POST'])
def predecir_atraso():
    try:
        # Get input data in JSON format
        datos = request.json

        # Make the prediction with the model
        prediccion = modelo.predict([datos])

        # Convert the prediction to text ("Atraso" or "No Atraso")
        etiqueta_prediccion = "Atraso" if prediccion[0] == 1 else "No Atraso"

        # Return the response in JSON format
        respuesta = {'prediccion': etiqueta_prediccion}
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
