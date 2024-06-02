# Heat Stroke Detection System

This project aims to predict the risk of heat stroke based on various environmental and personal factors using a machine learning model. The project includes a Flask web application that takes user input, fetches weather data, and provides a prediction on the likelihood of heat stroke.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Training](#model-training)
- [Web Application](#web-application)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Heat stroke is a serious condition caused by the body overheating, usually as a result of prolonged exposure to or physical exertion in high temperatures. This project uses a machine learning model to predict the risk of heat stroke based on input factors such as age, body temperature, environmental temperature, humidity, sun exposure, and physical activity.

## Features

- Predict heat stroke risk using a Logistic Regression model.
- Web interface for easy input and result display.
- Integration with OpenWeatherMap API to fetch real-time weather data.
- Validation of user input to ensure accurate predictions.

## Installation

### Prerequisites

- Python 3.6+
- Flask
- scikit-learn
- pandas
- joblib

### Steps
###Clone the repository:
   ```bash
   git clone https://github.com/yourusername/heat-stroke-detection.git
   cd heat-stroke-detection
