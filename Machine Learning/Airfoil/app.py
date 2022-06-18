import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict_api',methods=["POST"])
def predict_api():
    data = request.json['data']
    print(data)
    data_formatted = [list(data.values())]
    output = model.predict(data_formatted)[0]
    return jsonify(output)

@app.route('/predict',methods=["POST"])
def predict():
    data = [float(x) for x in request.form.values()]
    data_formatted = [data]
    output = model.predict(data_formatted)[0]
    return render_template('home.html',prediction_text="Airfoil pressure is {}".format(output))

if __name__ == '__main__':
    app.run(debug=True)