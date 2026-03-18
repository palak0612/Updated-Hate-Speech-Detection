import tkinter as tk
from tkinter import messagebox
import pickle
from preprocessing import clean_text

# Load model & vectorizer
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# Prediction function
def predict_text():
    text = entry.get("1.0", tk.END).strip()
    
    if not text:
        messagebox.showwarning("Warning", "Please enter some text")
        return
    
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]

    if prediction == 1:
        result_label.config(text="🚫 Hate Speech Detected", fg="red")
    else:
        result_label.config(text="✅ Normal Speech", fg="green")

# Create window
root = tk.Tk()
root.title("Hate Speech Detector")
root.geometry("500x400")
root.config(bg="#f0f0f0")

# Title
title = tk.Label(root, text="Hate Speech Detection", 
                 font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Text box
entry = tk.Text(root, height=8, width=50, font=("Arial", 12))
entry.pack(pady=10)

# Button
predict_btn = tk.Button(root, text="Predict", 
                        font=("Arial", 12, "bold"),
                        bg="#4CAF50", fg="white",
                        command=predict_text)
predict_btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", 
                        font=("Arial", 14, "bold"),
                        bg="#f0f0f0")
result_label.pack(pady=20)

# Run app
root.mainloop()