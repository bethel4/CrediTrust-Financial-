import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Paths
INDEX_PATH = 'vector_store/faiss_index.bin'
METADATA_PATH = 'vector_store/metadata.pkl'
EMBEDDING_MODEL_NAME = 'all-MiniLM-L6-v2'

# Load FAISS index and metadata
def load_vector_store():
    index = faiss.read_index(INDEX_PATH)
    with open(METADATA_PATH, 'rb') as f:
        metadata = pickle.load(f)
    return index, metadata

# Load embedding model
def load_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL_NAME)

# Embed a query
def embed_query(model, query):
    return model.encode([query])[0].astype('float32')

# Retrieve top-k relevant chunks
def retrieve_chunks(query, k=5):
    index, metadata = load_vector_store()
    embed_model = load_embedding_model()
    query_vec = embed_query(embed_model, query)
    D, I = index.search(np.array([query_vec]), k)
    retrieved = [metadata[i] for i in I[0]]
    return retrieved

# Prompt template
def build_prompt(context_chunks, question):
    context = '\n---\n'.join([c['chunk'] for c in context_chunks])
    prompt = (
        "You are a financial analyst assistant for CrediTrust. "
        "Your task is to answer questions about customer complaints. "
        "Use the following retrieved complaint excerpts to formulate your answer. "
        "If the context doesn't contain the answer, state that you don't have enough information.\n"
        f"Context:\n{context}\n"
        f"Question: {question}\n"
        "Answer:"
    )
    return prompt

# Generator (LLM) - using Hugging Face pipeline (default: distilbert-base-uncased, can be replaced)
def load_generator():
    return pipeline('text-generation', model='distilgpt2', max_length=256)

# RAG pipeline function
def answer_question(question, k=5):
    retrieved_chunks = retrieve_chunks(question, k)
    prompt = build_prompt(retrieved_chunks, question)
    generator = load_generator()
    response = generator(prompt, num_return_sequences=1)[0]['generated_text']
    # Extract only the answer part (after 'Answer:')
    answer = response.split('Answer:')[-1].strip()
    return {
        'question': question,
        'answer': answer,
        'retrieved_sources': [c['chunk'] for c in retrieved_chunks]
    }

# Example usage (uncomment to test)
# if __name__ == '__main__':
#     q = "What are common issues with money transfers?"
#     result = answer_question(q)
#     print("Question:", result['question'])
#     print("Answer:", result['answer'])
#     print("Sources:", result['retrieved_sources'])
