from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

df = pd.read_csv("data.csv")

model = SentenceTransformer('all-MiniLM-L6-v2')

index = faiss.read_index("hospital.index")

def get_reply(msg):
    vec = model.encode([msg])
    D, I = index.search(np.array(vec), 1)
    return df["answer"].iloc[I[0][0]]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.form["message"]
    reply = get_reply(msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)