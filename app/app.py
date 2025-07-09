import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from rag_pipeline import answer_question

st.set_page_config(page_title="CrediTrust Complaint Chatbot", layout="centered")
st.title("CrediTrust Financial Complaint Assistant")
st.write("Ask any question about customer complaints. The AI will answer and show supporting sources.")

if 'history' not in st.session_state:
    st.session_state['history'] = []

with st.form(key='chat_form'):
    user_input = st.text_input("Your question:", "")
    submit = st.form_submit_button("Ask")
    clear = st.form_submit_button("Clear")

if clear:
    st.session_state['history'] = []
    st.experimental_rerun()

if submit and user_input.strip():
    with st.spinner('Retrieving answer...'):
        result = answer_question(user_input, k=5)
        st.session_state['history'].append({
            'question': user_input,
            'answer': result['answer'],
            'sources': result['retrieved_sources']
        })

for entry in reversed(st.session_state['history']):
    st.markdown(f"**You:** {entry['question']}")
    st.markdown(f"**AI:** {entry['answer']}")
    with st.expander("Show sources"):
        for i, src in enumerate(entry['sources'][:2]):
            st.markdown(f"**Source {i+1}:**\n> {src[:500]}{'...' if len(src) > 500 else ''}")
    st.markdown("---")
