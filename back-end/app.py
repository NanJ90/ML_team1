from flask import Flask, request
from flask_cors import CORS

# from sklearn.ensemble import RandomForestClassifier
# from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*", "methods": ["GET","POST","OPTIONS"]}})

# Load model and vectorizer from disk
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
clf = pickle.load(open('model.pkl', 'rb'))

@app.route('/api/predict', methods=['POST', 'OPTIONS'])
def predict():
    print("inside predict")
    if request.method == 'OPTIONS':
        # this will send a 200 OK response, and let the browser know the CORS headers
        return ('', 200)
    else:
        # Get the data from the POST request
        data = request.get_json(force=True)
        # print(data)
        # Preprocess input
        # input_string = data['input'].lower().strip()
        # Preprocess input
        email = data['email']
        print(email)
        password = data['password']
        # Convert input to features
        input_features = vectorizer.transform([email])

        # Make prediction
        prediction = clf.predict(input_features.toarray())[0]  # convert to dense array here
        print(prediction)
        # Send back the result
        return {'result': int(prediction)}

if __name__ == '__main__':
    app.run(port=5000, debug=True)
