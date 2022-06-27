from flask import Flask,render_template,request
import numpy as np
import pickle
app = Flask(__name__)

@app.route('/')
def fun1():
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def hasan():
    a = [i  for i in request.form.values()]
    b = np.array(a,dtype=float)
    b = [b]
    model = pickle.load(open('./heart disease.pkl','rb'))
    predict_value = model.predict(b)
    predict_value = predict_value[0]
    if predict_value ==0:
        return render_template('index.html',prediction_text= 'No heart diseases')
    elif predict_value==1:
        return render_template('index.html', prediction_text='first stage heart diseases')
    elif predict_value ==2:
        return render_template('index.html', prediction_text='second stage heart diseases')
    elif predict_value == 3:
        return render_template('index.html', prediction_text='third stage heart diseases')
    else:
        return render_template('index.html', prediction_text='final stage heart diseases')


if __name__ == '__main__':
    app.run(debug=True)