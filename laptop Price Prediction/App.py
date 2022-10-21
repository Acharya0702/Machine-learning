import flask
from flask import Flask
import joblib
from flask import render_template, request
import numpy as np
app = Flask(__name__)
model = joblib.load('model.pkl')
@app.route("/")
def home():
   return render_template('laptop.html')
@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method=='POST':
        f1 = request.form['f1']
        f2 = request.form['f2']
        f3 = request.form['f3']
        f4 = request.form['f4']
        f5 = request.form['f5']
        f6 = request.form['f6']
        f7 = request.form['f7']
        f8 = request.form['f8']
        f9 = request.form['f9']
        f10 = request.form['f10']
        f11 = request.form['f11']
        f12 = request.form['f12']
        f13 = request.form['f13']
        f14 = request.form['f14']
        f15 = request.form['f15']
        f16 = request.form['f16']
        f17 = request.form['f17']
        f18 = request.form['f18']
        feature_array = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18]
        feature = np.asarray(feature_array, dtype='float64').reshape(1,-1)
        prediction = model.predict(feature)
        return render_template('laptop.html', prediction='{}'.format(prediction))
if __name__ == '__main__':
    app.run(debug=True)