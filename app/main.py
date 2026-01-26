from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

# ----------------------------
# FastAPI App
# ----------------------------
app = FastAPI(title="Amazon Home Semantic Search 🚀")

# ----------------------------
# Load Data & Model
# ----------------------------
DATA_PATH = os.path.join("artifacts", "amazon_home.csv")
INDEX_PATH = os.path.join("artifacts", "amazon_home_index.faiss")

amazon_home = pd.read_csv(DATA_PATH)

# Load FAISS index
index = faiss.read_index(INDEX_PATH)


# Option 2: Use pre-downloaded local folder (safer)
model = SentenceTransformer("./all-MiniLM-L6-v2")

# Pydantic Model
class Product(BaseModel):
    title: str
    image: str | None
    category: str
    similarity: float

# Semantic Search Logic
def semantic_search(query: str, top_k: int = 5) -> List[Product]:
    query_embedding = model.encode([query])
    faiss.normalize_L2(query_embedding)

    scores, indices = index.search(query_embedding, top_k)

    results = []
    for idx, score in zip(indices[0], scores[0]):
        product = amazon_home.iloc[idx]

        image = None
        if "image" in product and isinstance(product["image"], str):
            image = product["image"]

        results.append(Product(
            title=product["title"],
            image=image,
            category=product["main_category"],
            similarity=float(score)
        ))

    return results

# API Endpoint
@app.get("/search", response_model=List[Product])
def search(
    query: str = Query(..., description="Search query"),
    top_k: int = Query(5, ge=1, le=20)
):
    return semantic_search(query, top_k)
