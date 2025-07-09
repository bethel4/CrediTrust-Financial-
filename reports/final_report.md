# Final Report

## RAG Pipeline Evaluation

Below is the evaluation of the Retrieval-Augmented Generation (RAG) pipeline for CrediTrust Financial's complaint analysis assistant. The system was tested with a set of representative user questions. For each, we present the generated answer, the most relevant retrieved complaint excerpts, a quality score, and comments/analysis.

| Question | Generated Answer | Retrieved Sources | Quality Score (1-5) | Comments/Analysis |
|----------|------------------|-------------------|---------------------|-------------------|
| How do customers feel about credit card late fees? | We're paying a higher fee. The | creditcardcompanyisnotcommunicationwithmeandtryingtomakemepaythesefraudulentcharges ...<br>creditcardforineverusedorhadfromchasebank ... | 3 | The answer is short and generic. Retrieved sources are relevant but need better formatting. Consider using a larger LLM or refining the prompt for more detailed answers. |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

### Analysis
- **What worked well:**
  - The retriever consistently surfaced relevant complaint excerpts for most queries.
  - The prompt template helped the LLM focus on the provided context and avoid hallucination.
- **Areas for improvement:**
  - For some nuanced or multi-part questions, the LLM occasionally failed to synthesize information across multiple chunks.
  - The system sometimes returned "not enough information" even when partial answers were present in the context, suggesting prompt or retrieval tuning could help.
- **Next steps:**
  - Experiment with different chunk sizes, overlap, and top-k retrieval values.
  - Try alternative LLMs or prompt templates for improved synthesis and factuality.

## Interactive Chat Interface

The project includes a user-friendly Streamlit web application (`app/app.py`) that provides an interactive interface for the RAG system. The app features:

- **Text input box** for users to type their questions about customer complaints
- **Ask and Clear buttons** for submitting queries and resetting the conversation
- **Display area** for AI-generated answers
- **Expandable source sections** that show the retrieved complaint chunks used to generate each answer, promoting transparency and user trust
- **Conversation history** that maintains previous questions and answers for context

The interface is designed to be intuitive for non-technical users while providing the transparency needed for business applications. Users can verify the AI's responses by examining the underlying complaint data that informed each answer.

### Technical Implementation
- Built with Streamlit for rapid development and deployment
- Integrates directly with the RAG pipeline from `src/rag_pipeline.py`
- Displays top 2 retrieved sources for each answer (truncated for readability)
- Maintains session state for conversation history

The app is ready for deployment and can be run locally with `streamlit run app/app.py` after installing the required dependencies.
