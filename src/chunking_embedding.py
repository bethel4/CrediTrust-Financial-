import pandas as pd
import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# Paths
DATA_PATH = 'data/processed/filtered_complaints.csv'
VECTOR_STORE_DIR = 'vector_store'
INDEX_PATH = os.path.join(VECTOR_STORE_DIR, 'faiss_index.bin')
METADATA_PATH = os.path.join(VECTOR_STORE_DIR, 'metadata.pkl')

# Ensure output directory exists
os.makedirs(VECTOR_STORE_DIR, exist_ok=True)

# 1. Load cleaned data
df = pd.read_csv(DATA_PATH)

# 2. Chunking strategy
chunk_size = 512
chunk_overlap = 50
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

chunks = []
for idx, row in df.iterrows():
    for chunk in text_splitter.split_text(str(row['cleaned_narrative'])):
        chunks.append({
            'complaint_id': row['Complaint ID'],
            'product': row['Product'],
            'chunk': chunk
        })

# 3. Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# 4. Generate embeddings
texts = [c['chunk'] for c in chunks]
embeddings = model.encode(texts, show_progress_bar=True, batch_size=64)
embeddings = np.array(embeddings).astype('float32')

# 5. Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# 6. Save index and metadata
faiss.write_index(index, INDEX_PATH)
with open(METADATA_PATH, 'wb') as f:
    pickle.dump([
        {'complaint_id': c['complaint_id'], 'product': c['product'], 'chunk': c['chunk']} for c in chunks
    ], f)

print(f"FAISS index saved to {INDEX_PATH}")
print(f"Metadata saved to {METADATA_PATH}")
