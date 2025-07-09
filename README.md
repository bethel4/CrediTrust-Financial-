# CrediTrust-Financial

## Project Structure

```
├── data/                        # Raw and processed data
│   ├── raw/                    # Original complaint data (read-only)
│   └── processed/              # Cleaned and filtered datasets
│       └── filtered_complaints.csv
│
├── notebooks/                  # Jupyter notebooks for EDA and testing
│   ├── 01_eda_preprocessing.ipynb
│   └── 02_evaluation.ipynb
│
├── src/                        # Core Python modules
│   ├── __init__.py
│   ├── data_processing.py      # Data cleaning, filtering functions
│   ├── chunking_embedding.py   # Text chunking and embedding logic
│   ├── rag_pipeline.py         # Core RAG logic: retriever + generator
│   └── utils.py                # Helper functions
│
├── vector_store/               # Saved vector index (FAISS or ChromaDB)
│   └── faiss_index.bin or chromadb/...
│
├── app/                        # Streamlit or Gradio app
│   ├── app.py                  # Main chat interface code
│   └── ui_helpers.py           # Layout or UI-specific logic (optional)
│
├── reports/                    # Documentation and final report
│   ├── interim_report.md
│   ├── final_report.md
│   └── screenshots/            # UI demo images or GIFs
│
├── tests/                      # Unit tests for your modules
│   ├── test_data_processing.py
│   └── test_rag_pipeline.py
│
├── .gitignore                  # Files and folders to ignore in git
├── README.md                   # Project overview and usage guide
├── requirements.txt            # Python dependencies
└── LICENSE                     # Choose an open-source license (e.g., MIT)
```

## Usage

- Place raw data in `data/raw/`.
- Processed data will be saved in `data/processed/`.
- Notebooks for EDA and evaluation are in `notebooks/`.
- Core logic is in `src/`.
- The app interface is in `app/`.
- Reports and documentation are in `reports/`.
- Unit tests are in `tests/`.
