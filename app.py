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
