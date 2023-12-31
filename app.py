   
import json
import pickle
import flask

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model
pickle_in = open("XGBoost.pkl","rb")
XGBoost=pickle.load(pickle_in)  

pickle_sc = open("sc.pkl","rb")
sc=pickle.load(pickle_sc)  



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=sc.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=sc.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=XGBoost.predict(final_input)[0]
    output = round(output,1)
    return render_template("home.html",prediction_text="Predicted Compressive strength is {}".format(output) + ' MPa')

   
     
if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8080) #local host
    # app.run(host='0.0.0.0', port=8080) #for AWS
    app.run(host='0.0.0.0', port=80) #for AZURE