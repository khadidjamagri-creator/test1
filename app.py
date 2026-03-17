from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# --- ENTRAÎNEMENT ---
df = pd.read_csv("emails_dataset.csv")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["email"])
y = df["label"]
model = MultinomialNB()
model.fit(X, y)

app = Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return "L'API de classification d'emails est active ! Utilisez le chemin /predict en POST."

# --- CHEMIN 2 : Prédiction (celui à tester avec curl) ---
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["email"]
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)
    return jsonify({"classe": str(prediction[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
