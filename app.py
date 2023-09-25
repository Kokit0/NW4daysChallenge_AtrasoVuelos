
from flask import Flask, request, jsonify
import joblib
import requests

# Load the serialized model
# modelo = joblib.load('modelo_xgboost.pkl') <--- cambia la ruta a tu preferencia
modelo = joblib.load('E:\\OneDrive\\Documents\\nw4dayschallenge\\NW4daysChallenge_AtrasoVuelos\\modelo_xgboost.pkl') # <--- ruta testeo local



# Creamos la Flask app
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

