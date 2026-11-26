import json, faiss, numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
jobs = json.load(open("jobs.json"))
texts = [f"{j['title']}. {j['skills']}. {j['description']}" for j in jobs]
emb = model.encode(texts, normalize_embeddings=True)
index = faiss.IndexFlatIP(emb.shape[1])
index.add(np.array(emb))

def search(q, k=3):
    qv = model.encode([q], normalize_embeddings=True)
    scores, ids = index.search(qv, k)
    return [jobs[i] for i in ids[0]]