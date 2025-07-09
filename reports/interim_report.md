# Interim Report

## EDA Key Findings

After filtering the CFPB complaint dataset for the five target products (Credit card, Personal loan, Buy Now, Pay Later, Savings account, and Money transfers) and removing records with empty complaint narratives, we obtained a high-quality subset suitable for downstream analysis. All key columns required for the RAG pipeline—such as product type and consumer complaint narrative—are now complete, with no missing values.

Our exploratory analysis revealed that the distribution of complaints varies significantly across products, with some products receiving a much higher volume of complaints than others. The length of complaint narratives also varies widely, ranging from very brief statements to detailed multi-paragraph accounts. While most narratives are of moderate length, a small number of extremely short or long complaints were observed. Additionally, several columns in the dataset (such as Sub-product, Sub-issue, Tags, Company public response, and Consumer disputed?) contain substantial missing data. These columns may be less useful for automated analysis or may require special handling if included in future modeling efforts.

Overall, the cleaned and filtered dataset provides a robust foundation for building the RAG-based chatbot and conducting further analysis on complaint trends and customer concerns.

## Chunking Strategy and Embedding Model Choice

To prepare the complaint narratives for semantic search, we implemented a text chunking strategy using LangChain's RecursiveCharacterTextSplitter. We set the chunk size to 512 characters and the chunk overlap to 50 characters. This configuration was chosen to balance the need for sufficient context within each chunk (to preserve meaning) and the efficiency of the embedding and retrieval process. Larger chunks risk missing important details, while smaller chunks may lose necessary context. The overlap ensures that information at the boundaries of chunks is not lost.

For embedding, we selected the pre-trained model 'sentence-transformers/all-MiniLM-L6-v2'. This model offers a strong trade-off between semantic accuracy and computational efficiency, making it well-suited for large-scale retrieval tasks. It is widely used for semantic search applications and provides high-quality vector representations of text, enabling effective similarity search in the vector store.


