from flask import Flask, request
from flask_cors import CORS

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*", "methods": ["GET","POST","OPTIONS"]}})

# Load model and vectorizer from disk
# clf = pickle.load(open('model.pkl', 'rb'))
try:
    with open('model.pkl', 'rb') as f:
        clf = pickle.load(f)
    print("Model loaded successfully")
except Exception as e:
    print(f"An error occurred: {e}")
vectorizer = TfidfVectorizer()
# @app.route('/api/login', methods=['POST'])
# def login():
#     # Handle login

@app.route('/api/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        # this will send a 200 OK response, and let the browser know the CORS headers
        return ('', 200)
    else:
        # Get the data from the POST request
        data = request.get_json(force=True)
        print(data)
        # Preprocess input
        input_string = data['input'].lower().strip()

        # Convert input to features
        input_features = vectorizer.transform([input_string])

        # Make prediction
        prediction = clf.predict(input_features)[0]
        print(prediction)
        # Send back the result
        return {'result': prediction}

if __name__ == '__main__':
    app.run(port=5000, debug=True)
