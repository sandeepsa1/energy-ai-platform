# Energy AI Platform

## Overview
The Energy AI Platform is an end-to-end, production-oriented AI system designed to analyze, forecast, and explain energy consumption patterns using modern machine learning and generative AI techniques.

The project combines:
- Time-series forecasting
- Anomaly detection
- Deep learning
- Retrieval-Augmented Generation (RAG) 
- API-based model serving

The goal is to move beyond notebooks and build a real, deployable AI product.

---

## Problem Statement
Accurate energy forecasting and early detection of abnormal consumption are critical for energy providers, facility managers, and sustainability teams. However, energy data is often large, noisy, and difficult to analyze, and valuable insights are scattered across reports and documents.

This project addresses these challenges by building an AI-powered platform that:
- Forecasts short-term energy consumption
- Detects unusual usage patterns
- Answers natural-language questions using domain-specific data
- Provides explainable insights backed by data

---

## Key Features (Planned)
- 📈 Energy consumption forecasting using deep learning (LSTM/GRU)
- 🚨 Anomaly detection using autoencoders
- 🧠 Feature engineering on high-frequency time-series data
- 🔍 Retrieval-Augmented Generation (RAG) for document-based Q&A
- 🌐 REST APIs for inference using FastAPI
- 📊 Simple UI for interaction and visualization
- 🐳 Containerized deployment with Docker
- 📉 Experiment tracking and monitoring using MLflow

---

## Dataset
**Individual Household Electric Power Consumption Dataset (UCI)**

- Time granularity: 1 minute
- Duration: Multiple years
- Target variable: `Global_active_power`
- Data includes voltage, current, and sub-metered energy usage

The raw dataset is not committed to the repository. See `docs/data_notes.md` for exploration details.

---

## Project Structure
energy-ai-platform/
├── data/
│ ├── raw/ # Raw datasets (ignored by git)
│ ├── processed/ # Cleaned & resampled data (ignored)
│ └── external/
├── src/
│ ├── ingestion/ # Data loading and validation
│ ├── preprocessing/ # Cleaning, resampling, feature engineering
│ ├── models/ # Model definitions
│ ├── training/ # Training pipelines
│ ├── inference/ # Inference logic
│ ├── rag/ # RAG & LLM integration
│ └── evaluation/ # Metrics and evaluation
├── backend/ # FastAPI backend
├── frontend/ # UI (Streamlit / Web)
├── experiments/ # Experiment configs
├── notebooks/ # Exploratory notebooks
├── docs/ # Architecture & data notes
├── docker/ # Docker and deployment files
├── requirements.txt
├── .gitignore
└── README.md


---

## Tech Stack
- **Language:** Python
- **Deep Learning:** TensorFlow / Keras
- **Data Processing:** Pandas, NumPy
- **Time-Series & ML:** Scikit-learn
- **LLMs & RAG:** SentenceTransformers, FAISS, local LLMs
- **Backend:** FastAPI
- **Frontend:** Streamlit (initial)
- **MLOps:** MLflow
- **Containerization:** Docker

All tools and libraries used are free and open-source.

---

## Setup Instructions

```bash
## 1. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

## Install Dependencies
pip install -r requirements.txt

## Data Ingestion
Place the dataset in:
- data/raw/
Then Run:
- python src/ingestion/load_energy_data.py