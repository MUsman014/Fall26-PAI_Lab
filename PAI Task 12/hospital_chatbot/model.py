import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

df = pd.read_csv("data.csv")

model = SentenceTransformer('all-MiniLM-L6-v2')

questions = df["question"].tolist()

embeddings = model.encode(questions)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

faiss.write_index(index, "hospital.index")

print("Model ready ✔")