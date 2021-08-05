import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
app=Flask(__name__ )
model=pickle.load(open("DecisionTree.pkl","rb"))
@app.route("/")
def home():
    return render_template("index.html")
# @app.route("/predict", methods=["post"])
# def predict():
#     float_features= [float(x) for x in request.form.values()]
#     features= [np.array(float_features)]
#     prediction= model.predict(features)
#
#     return render_template("index.html", prediction_test=" Your expected girl friend is{}".format(prediction))

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html", prediction_text = " Your expected girl friend is{}".format(prediction))

if __name__== '__main__':
    app.run(debug=True)