from flask import Flask, request, jsonify
import joblib

# Cargar el modelo serializado
modelo = joblib.load('modelo_xgboost.pkl')

# Crear la aplicación Flask
app = Flask(__name__)

@app.route('/predecir_atraso', methods=['POST'])
def predecir_atraso():
    try:
        # Obtener datos de entrada en formato JSON
        datos = request.json

        # Realizar la predicción con el modelo
        prediccion = modelo.predict([datos])

        # Convertir la predicción a texto ("Atraso" o "No Atraso")
        etiqueta_prediccion = "Atraso" if prediccion[0] == 1 else "No Atraso"

        # Devolver la respuesta en formato JSON
        respuesta = {'prediccion': etiqueta_prediccion}
        return jsonify(respuesta)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
