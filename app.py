from flask import Flask, request, render_template
import joblib
import requests
import numpy as np
import math

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('heat_stroke_model.pkl')
scaler = joblib.load('scaler.pkl')

# Define feature names
feature_names = [
    'Heat Index (HI)',
    'Environmental temperature (C)',
    'Patient temperature',
    'Relative Humidity',
    'Exposure to sun',
    'Exertional (1) vs classic (0)',
    'Age',
    'Strenuous exercise'
]

API_KEY = 'b4aaed42e8a920c5adc527b5219d38fa'

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit


def calculate_relative_humidity(temperature_celsius, humidity_percentage):
    # Calculate vapor pressure (e)
    saturation_vapor_pressure = 6.112 * math.exp((17.62 * temperature_celsius) / (243.12 + temperature_celsius))
    vapor_pressure = (humidity_percentage / 100) * saturation_vapor_pressure

    # Calculate relative humidity
    relative_humidity = (vapor_pressure / saturation_vapor_pressure) * 100
    return relative_humidity

def getWeatherData(location):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + location + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        temp = celsius_to_fahrenheit(main["temp"])
        humidity = main["humidity"]
        hi = celsius_to_fahrenheit(main["feels_like"])
        rh = calculate_relative_humidity(main["temp"], humidity) / 100
        return hi, temp, rh
    else:
        return None, None, None


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        location = request.form['location']
        hi, temp, relativeHumidity = getWeatherData(location)
        if hi is None:
            return render_template('result.html', prediction_text="Invalid location. Please try again.")

        # Get user input for other features
        patient_temp = float(request.form['Patient temperature'])
        exposure_to_sun = float(request.form['Exposure to sun'])
        exertional = float(request.form['Exertional (1) vs classic (0)'])
        age = float(request.form['Age'])
        strenuous_exercise = float(request.form['Strenuous exercise'])

        # Collect all features in the correct order
        features = [hi,temp,patient_temp,relativeHumidity, exposure_to_sun, exertional, age, strenuous_exercise]
        # Convert to numpy array and reshape for the scaler
        features_array = np.array(features).reshape(1, -1)
        # Scale the features
        scaled_features = scaler.transform(features_array)
        # Predict using the model
        prediction = model.predict(scaled_features)
        # Return the result
        result = 'Heat Stroke' if prediction[0] == 1 else 'No Heat Stroke'
        return render_template('result.html', prediction_text=f'Result: {result}')


if __name__ == "__main__":
    app.run(debug=True)
