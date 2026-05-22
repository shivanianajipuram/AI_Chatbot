from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from uuid import uuid4

# =========================
# CONFIG
# =========================

DATA_PATH = "data"
CHROMA_PATH = "chroma_db"

# =========================
# LOAD PDF FILES
# =========================

loader = PyPDFDirectoryLoader(DATA_PATH)

documents = loader.load()

print(f"\nLoaded {len(documents)} pages\n")

# =========================
# SPLIT TEXT
# =========================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks\n")

# =========================
# EMBEDDINGS
# =========================

embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =========================
# CREATE CHROMA DB
# =========================

vector_store = Chroma(
    collection_name="rag_collection",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH
)

# unique ids
ids = [str(uuid4()) for _ in range(len(chunks))]

# store embeddings
vector_store.add_documents(
    documents=chunks,
    ids=ids
)

print("Documents stored in ChromaDB successfully!")