from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('farmer_model.lb')  # Make sure this file is in the same folder

history = []  # To store past predictions

@app.route('/')
def home():
    return render_template('project.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project', methods=['GET', 'POST'])
def project():
    if request.method == 'POST':
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        print('output>>>>>>',N, P, K, temperature, humidity, ph, rainfall)
        input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
        prediction = model.predict(input_data)[0]

        prediction = model.predict(input_data)[0]
        print("Prediction from model:", prediction)
        
        history.append((N, P, K, temperature, humidity, ph, rainfall, prediction))
        return render_template('project.html', prediction=prediction)
    return render_template('project.html')

@app.route('/history')
def show_history():
    return render_template('history.html', history=history)

if __name__ == '__main__':
    app.run(debug=True)
