import joblib
import numpy as np

# Load the model and scaler
model = joblib.load('heat_stroke_model.pkl')
scaler = joblib.load('scaler.pkl')

def predict_heat_stroke(features):
    # Convert features to numpy array and reshape for the scaler
    features_array = np.array(features).reshape(1, -1)
    # Scale the features
    scaled_features = scaler.transform(features_array)
    # Predict using the model
    prediction = model.predict(scaled_features)
    # Return the result
    result = 'Heat Stroke' if prediction[0] == 1 else 'No Heat Stroke'
    return result

def main():
    print("Enter the following features to predict heat stroke:")

    # Assuming you have three features for simplicity. Add or remove based on your dataset.

    feature1 = float(input("Feature 1: "))
    feature2 = float(input("Feature 2: "))
    feature3 = float(input("Feature 3: "))
    feature4 = float(input("Feature 4: "))
    feature5 = float(input("Feature 5: "))
    feature6 = float(input("Feature 6: "))
    feature7 = float(input("Feature 7: "))
    feature8 = float(input("Feature 8: "))
    # Add more features as required

    # Collect all features in a list
    features = [feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8]

    # Predict heat stroke
    result = predict_heat_stroke(features)
    print(f'Result: {result}')

if __name__ == "__main__":
    main()
