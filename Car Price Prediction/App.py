from flask import Flask, request, render_template, jsonify
import numpy as np
import joblib
model=joblib.load('model.pkl')
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/pred', methods=['POST'])
def pred():
    if request.method=='POST':
        f1=float(request.form['f1'])
        f2=float(request.form['f2'])
        f3=float(request.form['f3'])
        f4=float(request.form['f4'])
        f5=float(request.form['f5'])
        f6=float(request.form['f6'])
        f7=float(request.form['f7'])
        f8=float(request.form['f8'])
        feature_array=np.array([f1, f2, f3, f4, f5, f6, f7, f8]).reshape(1, -1)
        x=model.predict(feature_array)
        if f3<0.320000 or f3>92.600000:
            return render_template('index.html', prediction='The car Price should be: {} Since the present price crossing the limit the prediction may be wrong.'.format(x))
        elif f4<500.000000 or f4>500000.000000:
            return render_template('index.html', prediction='The car Price should be: {} Since the driven kms crossing the limit the prediction may be wrong.'.format(x))
        else:
            return render_template('index.html', prediction='The car Price should be: {}'.format(x))
if __name__=='__main__':
    app.run(debug=True)