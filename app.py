import streamlit as st
import google.generativeai as genai

from sentence_transformers import SentenceTransformer
from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings
import os
from dotenv import load_dotenv


# ------------------------
# Gemini API
# ------------------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ------------------------
# Embedding Wrapper
# ------------------------

class SentenceTransformerEmbeddings(Embeddings):

    def __init__(self, model):
        self.model = model

    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    def embed_query(self, text):
        return self.model.encode(text).tolist()

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

embedding_function = SentenceTransformerEmbeddings(
    embedding_model
)

vector_db = Chroma(
    collection_name="langchain",
    persist_directory="./chroma_db",
    embedding_function=embedding_function,
)

# ------------------------
# Streamlit UI
# ------------------------

st.set_page_config(
    page_title="Python PDF Chatbot",
    layout="wide"
)

st.title("Domain-Specific RAG Chatbot")

st.write("Ask questions about the uploaded Python book.")

question = st.text_input("Ask your question")

if st.button("Generate Answer"):

    docs = vector_db.similarity_search(question, k=5)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer ONLY using the following context.

Context:

{context}

Question:

{question}
"""

    answer = model.generate_content(prompt)

    st.subheader("Answer")

    st.write(answer.text)

    st.subheader("Retrieved Context")

    for i, doc in enumerate(docs, 1):
        with st.expander(f"Chunk {i}"):
            st.write(doc.page_content)