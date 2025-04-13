from flask import Flask, request, render_template
import pickle
import numpy as np

# Load model and scalers
model = pickle.load(open('salary_model.pkl', 'rb'))
x_scaler = pickle.load(open('x_scaler.pkl', 'rb'))
y_scaler = pickle.load(open('y_scaler.pkl', 'rb'))

# Same encodings as used during training
gender_map = {'Male': 1, 'Female': 0}
education_map = {
    "High School": 0,
    "Bachelor's": 1,
    "Master's": 2,
    "PhD": 3
}
job_title_map = {
    "Software Engineer": 0,
    "Data Scientist": 1,
    "Project Manager": 2,
    "Business Analyst": 3,
    "HR Manager": 4
}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        gender = gender_map[request.form['gender']]
        experience = float(request.form['experience'])
        education = education_map[request.form['education']]
        job_title = job_title_map[request.form['job_title']]

        input_data = np.array([[age, gender, experience, education, job_title]])
        input_scaled = x_scaler.transform(input_data)
        prediction_scaled = model.predict(input_scaled).reshape(-1, 1)
        prediction = y_scaler.inverse_transform(prediction_scaled)

        return render_template('index.html', prediction_text=f"Predicted Salary: ₹{prediction[0][0]:,.2f} per month")

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
