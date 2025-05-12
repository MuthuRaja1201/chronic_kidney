from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input values from form
        sg = float(request.form['sg'])
        htn = float(request.form['htn'])
        hemo = float(request.form['hemo'])
        dm = float(request.form['dm'])
        al = float(request.form['al'])
        appet = float(request.form['appet'])
        rc = float(request.form['rc'])
        pc = float(request.form['pc'])

        # Simple rule-based logic for demonstration
        if hemo < 12 and al > 2 and htn == 1:
            prediction = 'Chronic Kidney Disease Detected'
        else:
            prediction = 'No Chronic Kidney Disease Detected'

        return render_template('result.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
