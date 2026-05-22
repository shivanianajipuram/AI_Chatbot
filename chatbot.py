import gradio as gr

from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# =========================
# CONFIG
# =========================

CHROMA_PATH = "chroma_db"

# =========================
# EMBEDDINGS
# =========================

embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =========================
# LOAD VECTOR DB
# =========================

vector_store = Chroma(
    collection_name="rag_collection",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

# =========================
# LOCAL LLM
# =========================

llm = ChatOllama(
    model="phi3"
)

# =========================
# CHAT FUNCTION
# =========================

def chat_function(message, history):

    docs = retriever.invoke(message)

    knowledge = ""

    for doc in docs:
        knowledge += doc.page_content + "\n\n"

    prompt = f"""
You are an intelligent AI assistant.

If the user gives greetings like:
hi, hello, hey
then respond naturally.

If the question is related to the document,
answer ONLY from the provided knowledge.

If the answer is not available in the document,
say:
"I could not find that in the document."

Question:
{message}

Knowledge:
{knowledge}
"""

    response = llm.invoke(prompt)

    return response.content

# =========================
# GRADIO UI
# =========================

demo = gr.ChatInterface(
    fn=chat_function,
    title="AI PDF Chatbot",
    description="Ask questions from your PDF"
)

demo.launch(server_name="127.0.0.1", server_port=7861)