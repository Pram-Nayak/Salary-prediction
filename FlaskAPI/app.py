import flask
from flask import Flask, jsonify, request, render_template
import json
from data_input import data_in
import numpy as np
import pickle

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    request_json = request.get_json()
    x = request_json['input']
    x_in = np.array(x).reshape(1, -1)
    model = load_models()
    prediction = model.predict(x_in)[0]
    response = json.dumps({'response': prediction})
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)