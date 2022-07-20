from fileinput import filename
from flask import Flask,render_template,request,redirect,url_for
import numpy as np
import joblib
import os
model=joblib.load(open('model.pkl','rb'))
app=Flask(__name__)
imgFolder=os.path.join('static','images')
app.config['UPLOAD_FOLDER']=imgFolder
@app.route('/')
def weather():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        f1=float(request.form['f1'])
        f2=float(request.form['f2'])
        f3=float(request.form['f3'])
        f4=float(request.form['f4'])
        feature_array=[f1,f2,f3,f4]
        features=np.array(feature_array).reshape(1,-1)
        pred=model.predict(features)
        name=str(pred)
        filename=os.path.join(app.config['UPLOAD_FOLDER'],str(pred[0])+'.jpg')
        return render_template('index.html', prediction='{}'.format(str(pred[0]).upper()), crop='{}'.format(filename))
if __name__=='__main__':
    app.run(debug=True)