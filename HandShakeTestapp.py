from flask import Flask, request, json
import numpy as np
from sklearn.mixture import GaussianMixture


#PRUEBA CON FLASK PARA HACER EL HANDSHAKE 

app = Flask(__name__)


@app.route('/model/', methods=['POST'])
def model_call():
    body = request.get_json()
    generator = np.random.default_rng(seed=42)
    x1 = generator.normal(loc=5, scale=1, size=(100, 1))
    x2 = generator.normal(loc=10, scale=2, size=(100, 1))
    x = x1 + x2
    gm = GaussianMixture(n_components=2)
    gm.fit(x)
    try:
        pred = gm.predict(
            np.array(float(body['input'])).reshape(1, -1)
        )
    except:
        return {
            'results': None,
            'message': 'The model could not be evaluated.',
            'error_code': 'INVALID_INPUT'
        }, 400
    return {
        'results': str(pred[0]),
        'message': 'Delay successfully predicted.'
    }, 200