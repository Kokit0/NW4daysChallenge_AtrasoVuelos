import os

# Definir la estructura de carpetas y archivos
project_structure = {
    'app.py': None,
    'modelo_xgboost.pkl': None,
    'requirements.txt': None,
    'api': {
        '__init__.py': None,
        'routes.py': None,
        # Agrega otros archivos relacionados con la API si es necesario
    },
    'data': {
        'dataset.csv': None,
        # Agrega otros archivos de datos si es necesario
    },
    'notebooks': {
        'Research_notebook01.ipynb': None,
        # Agrega otros notebooks si es necesario
    },
    # Puedes agregar más carpetas y archivos según tus necesidades
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
