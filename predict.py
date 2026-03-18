import pickle
from preprocessing import clean_text

# Load model
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

def predict_text(text):
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)
    return prediction[0]

# Run loop
while True:
    text = input("Enter text (or 'exit'): ")
    
    if text.lower() == 'exit':
        break
    
    result = predict_text(text)
    
    if result == 1:
        print("🚫 Hate Speech Detected")
    else:
        print("✅ Normal Speech")