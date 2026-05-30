# 🤖 Machine Learning & NLP Projects

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-scikit--learn-orange?style=for-the-badge)
![Similarity](https://img.shields.io/badge/Search-Cosine_Similarity-green?style=for-the-badge)
![Deployment](https://img.shields.io/badge/Deployed-Heroku-purple?style=for-the-badge&logo=heroku)
![ML](https://img.shields.io/badge/ML-Fraud_Detection-red?style=for-the-badge)

**A collection of end-to-end Machine Learning and NLP pipelines — from raw data to deployed applications.**

[Projects](#-projects) • [Architecture](#-architecture) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack)

</div>

---

## 📦 Projects

This repository contains two production-grade ML/NLP systems:

| # | Project | Tech | Description |
|---|---------|------|-------------|
| 1 | 🔍 **Semantic Product Search Engine** | Python, cosine similarity, REST APIs | AI-powered product search using semantic similarity |
| 2 | 🚨 **Fraud Detection Text Classifier** | scikit-learn, NLP, pandas | SMS/text fraud detection using probabilistic NLP |

---

## 🔍 Project 1 — Semantic Product Search Engine

### What It Does
A multi-stage **ETL + semantic search pipeline** that ingests large-scale e-commerce product data via API, applies similarity-based transformation, and returns the most relevant products for any natural language query — going far beyond simple keyword matching.

### The Problem It Solves
Traditional keyword search returns results that *contain* the search term. Semantic search understands *meaning* — searching "comfortable running shoes" returns relevant athletic footwear even if the exact words don't match.

### Architecture
```
┌──────────────────────────────────────────────────────────┐
│                    INGESTION PIPELINE                     │
│                                                          │
│  E-Commerce API                                          │
│       │                                                  │
│       ▼                                                  │
│  API Extraction ──► Data Cleaning ──► Text Vectorization │
│  (GET requests)    (pandas)           (TF-IDF / Cosine)  │
│                                              │           │
│                                              ▼           │
│                                       Queryable Index    │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│                     QUERY PIPELINE                        │
│                                                          │
│  User Query ──► Vectorize ──► Cosine Similarity Search   │
│                                       │                  │
│                                       ▼                  │
│                               Top-K Results ✅            │
│                         (filtered by relevance score)    │
└──────────────────────────────────────────────────────────┘
```

### Key Features
- 🌐 **API-driven ingestion** — Extracts product data via parameterised REST API calls with JSON parsing and error handling for rate-limited responses
- 🧹 **Data quality governance** — Top-K filtering removes low-relevance records, ensuring downstream data quality
- 🔍 **Semantic similarity** — Cosine similarity matching returns contextually relevant results, not just keyword matches
- 📊 **Scalable pipeline** — Designed to handle large product catalogues efficiently
- 🚀 **Deployed on Heroku** — Live, accessible web application

### Live Demo
> Check `Semantic Product Search Demo` file in repo for demo walkthrough

---

## 🚨 Project 2 — Fraud Detection Text Classifier

### What It Does
An end-to-end **NLP classification pipeline** that ingests raw SMS/text message data, applies probabilistic NLP transformations, and classifies messages as fraudulent or legitimate — with a real-time GUI for live inference.

### The Problem It Solves
SMS fraud and phishing attacks cost billions globally. This classifier provides an automated, scalable solution to detect and flag suspicious messages before they reach end users.

### Architecture
```
┌──────────────────────────────────────────────────────────┐
│                   TRAINING PIPELINE                       │
│                                                          │
│  Raw Messages                                            │
│       │                                                  │
│       ▼                                                  │
│  Text Cleaning ──► Feature Extraction ──► Model Training │
│  (normalise,       (TF-IDF / Bag        (Naive Bayes /   │
│   remove noise)     of Words)            scikit-learn)   │
│                                              │           │
│                                              ▼           │
│                                    Saved Model Artifact  │
│                                    (artifacts/)          │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│                   INFERENCE PIPELINE                      │
│                                                          │
│  Live Input ──► Preprocess ──► Model Predict ──► Result  │
│  (GUI)          (same as         (load from      (FRAUD  │
│                  training)        artifact)    / LEGIT)  │
└──────────────────────────────────────────────────────────┘
```

### Key Features
- 🧠 **Probabilistic NLP** — Uses statistical text features for robust classification
- 💾 **Model persistence** — Trained model saved as artifact for instant reloading (no retraining)
- 📊 **Structured output schema** — Classification results stored in queryable format for monitoring and reporting
- 🖥️ **Real-time GUI** — Live text input, instant prediction, pipeline health visibility
- 📈 **Performance monitoring** — Error analysis and classification metrics built in

---

## 🛠️ Tech Stack

| Component | Technology | Used For |
|---|---|---|
| **Language** | Python 3.10+ | Core development |
| **ML Framework** | scikit-learn | Model training & evaluation |
| **Data Processing** | pandas, numpy | Data cleaning & transformation |
| **NLP** | TF-IDF, Bag of Words, cosine similarity | Text feature extraction |
| **API Integration** | requests, JSON parsing | Data ingestion |
| **Model Persistence** | pickle (artifacts/) | Save/load trained models |
| **Deployment** | Heroku (Procfile) | Live web deployment |
| **Runtime** | Python 3.10 (runtime.txt) | Heroku runtime config |

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

### 3. Run the application
```bash
python app/app.py
```

---

## 💻 Usage

### Semantic Search
```python
# Enter a natural language product query
query = "comfortable running shoes for marathon"
# Returns top-K most semantically similar products
```

### Fraud Detection
```python
# Enter any SMS/text message in the GUI
message = "Congratulations! You've won a free iPhone. Click here to claim."
# Returns: FRAUD ⚠️ or LEGITIMATE ✅
```

---

## 📁 Project Structure

```
Machine-Learning-and-NLP/
│
├── app/
│   └── app.py                    # Main application & GUI
│
├── artifacts/                    # Saved trained model files
│   └── *.pkl                     # Pickled model artifacts
│
├── Semantic Product Search Demo  # Demo walkthrough file
│
├── Procfile                      # Heroku deployment config
├── runtime.txt                   # Python runtime version
└── requirements.txt              # Project dependencies
```

---

## 🔑 Key Engineering Decisions

| Decision | Reasoning |
|---|---|
| **Model artifacts saved to disk** | Avoids expensive retraining on every run |
| **Top-K filtering in search** | Improves result quality — data governance at query level |
| **Modular pipeline design** | Training and inference pipelines are independent and reusable |
| **Heroku deployment** | Makes project publicly accessible — not just local demos |
| **Structured output schema** | Enables downstream monitoring, reporting, and querying of results |

---

## 🔮 Future Improvements

- [ ] Add BERT/transformer-based embeddings for improved semantic search accuracy
- [ ] Expand fraud detection to email and social media text
- [ ] Add explainability — highlight which words triggered fraud classification
- [ ] REST API wrapper for both models
- [ ] Docker containerization for portable deployment
- [ ] A/B testing framework for model comparison

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

