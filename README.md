# Salary Prediction ML App

This is a web-based machine learning application that predicts salaries based on various input features such as education level, job title, experience, etc. The app is built using **Flask** for the backend and **machine learning models** to make predictions.

## Features

- **Flask Web App**: A simple interface to input data and receive salary predictions.
- **Machine Learning Model**: The model is trained using historical salary data and saved as a `.pkl` file for reuse.
- **Data Preprocessing**: The app includes scaling of input features and output salary using **MinMaxScaler**.
- **Deployment Ready**: The app can be easily deployed on any web server supporting Python and Flask.

## Project Structure

```
salary-prediction-app/
│
├── app.py                    # Flask backend
├── index.html                # Frontend template
├── salary_model.pkl          # Saved ML model
├── x_scaler.pkl              # Scaler for input features
├── y_scaler.pkl              # Scaler for output salary
├── dataset/                  # Folder with raw CSV
│   └── Salary Data.csv       # Dataset used for training the model
├── static/                   # (Optional) for CSS/JS if needed
│   └── style.css             # CSS file for styling the front-end
├── templates/
│   └── index.html            # Main HTML template rendered by Flask
├── README.md                 # Project overview and instructions
```

## Prerequisites

Before running the app, make sure you have **Python 3.x** installed on your machine. You will also need to install the required dependencies.

### Install Dependencies

1. Clone the repository:

   ```bash
   git clone https://github.com/MrRamraje/Salary-prediction-ml.git
   cd Salary-prediction-ml
   ```

2. Create and activate a **virtual environment** (optional but recommended):

   On **Windows**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   On **macOS/Linux**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required Python packages from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Application

1. Ensure the required files (`salary_model.pkl`, `x_scaler.pkl`, `y_scaler.pkl`, `Salary Data.csv`) are in place.

2. Run the Flask application:

   ```bash
   python app.py
   ```

3. Open your browser and go to `http://127.0.0.1:5000/` to access the application.

4. Fill in the form with the required details, and the app will predict the salary.

## Machine Learning Model

The machine learning model used for salary prediction is trained on the dataset located in the `dataset/` folder (`Salary Data.csv`). The model is serialized using `pickle` and saved as `salary_model.pkl` to be used in the Flask app for predictions.

The model uses **XGBoost** (or another appropriate algorithm) and is designed to predict the salary based on input features such as:
- Job title
- Education level
- Years of experience
- Other relevant features

### Scaling

The app uses **MinMaxScaler** to scale both input features and output salary values to improve the model’s accuracy. The scalers are saved as `x_scaler.pkl` and `y_scaler.pkl`.

## File Descriptions

- **`app.py`**: Main backend file running the Flask app. It handles data processing and serves predictions.
- **`salary_model.pkl`**: The trained machine learning model file used to predict salaries.
- **`x_scaler.pkl`**: Scaler for input features (to scale them before prediction).
- **`y_scaler.pkl`**: Scaler for the predicted salary output (to reverse the scaling).
- **`dataset/Salary Data.csv`**: The dataset used to train the model.
- **`static/`**: Contains the CSS file `style.css` for styling the app.
- **`templates/`**: Contains the `index.html` template for rendering the frontend in Flask.
- **`README.md`**: Project description, instructions for setup and usage.

## Future Improvements

- **Enhance Frontend**: Improve UI/UX with better design and interactivity.
- **Model Optimization**: Experiment with different machine learning models and hyperparameters to improve prediction accuracy.
- **Deploy to Production**: Deploy the app to a cloud service like Heroku or AWS for public access.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This `README.md` provides a clear overview of your project, including setup instructions, features, and how to run the app. You can customize or expand this as needed for your specific project!
