# 🔍 Semantic Product Search Engine

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Cosine_Similarity-orange?style=for-the-badge)
![APIs](https://img.shields.io/badge/Data-REST_APIs-green?style=for-the-badge)
![Deployment](https://img.shields.io/badge/Deployed-Heroku-purple?style=for-the-badge&logo=heroku)
![pandas](https://img.shields.io/badge/Data-pandas-yellow?style=for-the-badge&logo=pandas)

**Search smarter, not harder. Find products by meaning — not just keywords.**

[Overview](#-overview) • [Architecture](#-architecture) • [How It Works](#-how-it-works) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack)

</div>

---

## 🎯 Overview

A production-grade **semantic search engine for e-commerce products** — built as a complete ETL pipeline that ingests large-scale product data via REST APIs, applies NLP-based similarity transformation, and returns the most contextually relevant results for any natural language query.

> **The difference:** Keyword search finds products that *contain* your words.
> Semantic search finds products that *match your intent* — even when the words don't match exactly.

**Deployed live on Heroku** — not just a local demo.

---

## ✨ Features

- 🌐 **API-driven data ingestion** — Extracts product data via parameterised REST API calls with full JSON parsing and rate-limit error handling
- 🧹 **Data quality governance** — Top-K filtering removes low-relevance records during the loading stage, improving downstream search accuracy
- 🔍 **Semantic similarity search** — Cosine similarity matching surfaces contextually relevant products beyond simple keyword matching
- 📊 **Scalable ETL pipeline** — Multi-stage: Extract → Transform (similarity scoring) → Load (queryable index)
- 🚀 **Deployed on Heroku** — Live, publicly accessible web application
- ⚡ **Fast query handling** — Optimised for low-latency search responses

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                     INGESTION PIPELINE                        │
│                                                              │
│  E-Commerce API                                              │
│       │                                                      │
│       ▼                                                      │
│  API Extraction ──► Data Cleaning ──► Text Vectorization     │
│  (GET requests,     (pandas:           (TF-IDF /             │
│   JSON parsing,      normalise,         Cosine Similarity     │
│   error handling)    deduplicate)       scoring)             │
│                                              │               │
│                                              ▼               │
│                                    Top-K Filtered Index      │
│                                    (low-relevance removed)   │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                      QUERY PIPELINE                           │
│                                                              │
│  User Query                                                  │
│       │                                                      │
│       ▼                                                      │
│  Vectorize Query ──► Cosine Similarity ──► Ranked Results    │
│                       Search                  │             │
│                      (vs product index)       ▼             │
│                                        Top-K Products ✅     │
└──────────────────────────────────────────────────────────────┘
```

---

## ⚙️ How It Works

### Step 1 — Data Extraction
Product data is pulled from an e-commerce API using parameterised `GET` requests. The pipeline handles:
- JSON response parsing
- Error handling for failed or rate-limited calls
- Paginated data retrieval for large catalogues

### Step 2 — Transformation & Quality Filtering
```python
# Apply similarity-based transformation
# Filter out low-relevance records using Top-K threshold
# Result: clean, high-quality product dataset
```
This mirrors **schema-level data governance** — only products meeting a relevance threshold pass through to the index.

### Step 3 — Vectorization
Each product description is converted into a **numerical vector representation** using TF-IDF (Term Frequency-Inverse Document Frequency). This captures the *semantic importance* of words across the entire catalogue.

### Step 4 — Semantic Search
```python
# User types: "lightweight laptop for travel"
# Pipeline vectorizes the query
# Computes cosine similarity against all product vectors
# Returns Top-K most similar products ranked by relevance score
```

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| **Language** | Python 3.10+ | Core development |
| **Data Processing** | pandas | Cleaning, transformation, filtering |
| **NLP / Search** | cosine similarity, TF-IDF | Semantic matching |
| **API Integration** | requests, JSON | Product data ingestion |
| **Web Framework** | Flask / Streamlit | Application interface |
| **Deployment** | Heroku | Live production deployment |
| **Config** | Procfile, runtime.txt | Heroku deployment setup |

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/FarhanUllah382/Machine-Learning-and-NLP.git
cd Machine-Learning-and-NLP
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run locally
```bash
python app/app.py
```

---

## 💻 Usage

```python
# Enter a natural language product search query
query = "comfortable running shoes for marathon training"

# The engine returns the most semantically relevant products
# — even if exact words don't appear in product descriptions
```

**Example queries that work well:**
- `"budget smartphone with good camera"`
- `"warm jacket for cold weather hiking"`
- `"ergonomic office chair for back pain"`

---

## 📁 Project Structure

```
Machine-Learning-and-NLP/
│
├── app/
│   └── app.py                      # Main application, search logic & UI
│
├── artifacts/                      # Saved model/index artifacts
│
├── Semantic Product Search Demo    # Demo walkthrough
│
├── Procfile                        # Heroku process config
├── runtime.txt                     # Python runtime version (Heroku)
└── requirements.txt                # Project dependencies
```

---

## 🔑 Key Engineering Decisions

| Decision | Reasoning |
|---|---|
| **Top-K filtering during load** | Removes low-relevance records early — better data quality downstream |
| **Cosine similarity over keyword search** | Captures semantic meaning, handles synonyms and paraphrasing |
| **API-driven ingestion** | Scalable, real-world data source — not just a static CSV |
| **Heroku deployment** | Publicly accessible — demonstrates end-to-end deployment skills |
| **Modular ETL design** | Each stage (extract, transform, load) is independently testable |

---

## 🔮 Future Improvements

- [ ] Upgrade to BERT/sentence-transformer embeddings for deeper semantic understanding
- [ ] Add product category filtering alongside semantic search
- [ ] Implement user query history and personalised ranking
- [ ] REST API endpoint for programmatic search access
- [ ] Docker containerization for portable deployment
- [ ] Performance benchmarking: keyword vs semantic search accuracy

---

## 👨‍💻 Author

**Farhan Ullah**
BS Software Engineering — GIKI (Ghulam Ishaq Khan Institute)
Specialization: AI, Generative AI & Agentic Systems

[![GitHub](https://img.shields.io/badge/GitHub-FarhanUllah382-black?style=flat&logo=github)](https://github.com/FarhanUllah382)
[![Email](https://img.shields.io/badge/Email-u2024170@giki.edu.pk-blue?style=flat&logo=gmail)](mailto:u2024170@giki.edu.pk)

---

<div align="center">
⭐ If you found this project useful, please consider giving it a star!
</div>

