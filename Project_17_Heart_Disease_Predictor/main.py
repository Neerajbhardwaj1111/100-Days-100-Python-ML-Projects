from flask import Flask,render_template,request
import numpy as np
import pickle

app = Flask(__name__)

model= pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features =[float(x) for x in request.form.values()] 
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    result = "Positive (High Risk)" if prediction[0] == 1 else "Negative (Low Risk)"
    return render_template("index.html", prediction_text=f'Heart Disease Prediction: {result}')

if __name__ == "__main__":
    app.run(debug=True)
