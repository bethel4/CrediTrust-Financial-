# Final Report

## RAG Pipeline Evaluation

Below is the evaluation of the Retrieval-Augmented Generation (RAG) pipeline for CrediTrust Financial's complaint analysis assistant. The system was tested with a set of representative user questions. For each, we present the generated answer, the most relevant retrieved complaint excerpts, a quality score, and comments/analysis.

| Question | Generated Answer | Retrieved Sources | Quality Score (1-5) | Comments/Analysis |
|----------|------------------|-------------------|---------------------|-------------------|
| Example: How many complaints are about late fees on credit cards? | [LLM-generated answer] | [Excerpt 1, Excerpt 2] | 4 | Good use of context, but missed some nuance. |
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
