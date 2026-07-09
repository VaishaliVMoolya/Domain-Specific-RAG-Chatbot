# Project Results

## Objective

The objective of this project was to build a domain-specific chatbot capable of answering questions from a custom PDF document using Retrieval-Augmented Generation (RAG).

Instead of relying only on the language model's internal knowledge, the chatbot retrieves relevant information from the uploaded document before generating responses.

---

# Corpus Statistics

| Metric | Value |
|---------|------:|
| Total Pages | 241 |
| Total Characters | 430,998 |
| Total Chunks | 715 |
| Chunk Size | 800 |
| Chunk Overlap | 200 |

---

# Technologies Used

- Python
- Streamlit
- LangChain
- ChromaDB
- Google Gemini 2.5 Flash
- Sentence Transformers
- PyPDF
- Python Dotenv

---

# Pipeline

1. PDF Loading
2. Text Extraction
3. Recursive Text Chunking
4. Sentence Embedding Generation
5. Chroma Vector Database Storage
6. Semantic Similarity Search
7. Context Retrieval
8. Google Gemini Response Generation
9. Streamlit Deployment

---

# Functional Evaluation

## Test Case 1

**Question**

```
Explain Python dictionaries.
```

**Result**

The chatbot successfully retrieved the relevant document chunks and generated a correct explanation using the uploaded document.

---

## Test Case 2

**Question**

```
What is Object-Oriented Programming?
```

**Result**

The chatbot accurately retrieved the corresponding section from the document and produced a context-grounded answer.

---

## Test Case 3

**Question**

```
What is Quantum Physics?
```

**Expected Behaviour**

```
I couldn't find this information in the uploaded document.
```

This demonstrates that the chatbot avoids generating unsupported responses for topics outside the uploaded knowledge base.

---

# Achievements

- Successfully implemented Retrieval-Augmented Generation (RAG)
- Created semantic embeddings for 715 text chunks
- Integrated ChromaDB for efficient similarity search
- Used Google Gemini for grounded answer generation
- Built an interactive Streamlit application
- Successfully deployed the chatbot as a web application

---

# Conclusion

The developed chatbot successfully demonstrates the practical implementation of Retrieval-Augmented Generation using modern AI technologies.

By combining semantic embeddings, vector databases, similarity search, and Google's Gemini model, the system produces reliable, context-aware responses while reducing hallucinations through document-grounded retrieval.

The project satisfies the objectives of building a domain-specific AI assistant over a custom PDF knowledge base.