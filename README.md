# AI ChatBot RAG System
This is a Retrieval-Augmented Generation (RAG) chatbot that allows users to chat with PDF documents. It retrieves relevant document chunks using embeddings and generates answers using a local LLM (Phi-3 via Ollama). Fully offline, no API cost, privacy-focused, and resume-ready.

## Input
User-provided PDFs stored in `data/` folder (example: sample.pdf). These documents act as the knowledge base.

## System Pipeline
PDF → Text Extraction → Chunking → Embeddings → ChromaDB → Retriever → LLM → Answer

## Core Technologies
LangChain, ChromaDB, Sentence Transformers, Ollama (Phi-3), Gradio

## How It Works
1. PDF (data/sample.pdf) is loaded and split into chunks  
2. Chunks are converted into embeddings  
3. Stored in ChromaDB  
4. User query is embedded  
5. Similar chunks retrieved  
6. Context sent to LLM  
7. Final answer generated  

##  Model Used
Phi-3 (via Ollama), fully local inference, no API dependency

## Project Structure
AI_ChatBot_RAG/
├── chatbot.py
├── loading_document.py
├── requirements.txt
├── chroma_db/
└── data/
    └── sample.pdf

##  Setup Instructions
```bash
pip install -r requirements.txt
```
  
Place PDFs inside data/ folder  
```bash
python loading_document.py  
```

Install Ollama: 
```bash 
https://ollama.com/download/windows
```
#open cmd and run
```bash
ollama run phi3
```
#go to project folder and run the chatbot.py and Open browser link
```bash
python chatbot.py
```
# As we use our CPU to load answers into our chatbot, It takes time to give answers.
## Input to chatbot
Explain conclusion  
What is this PDF about?  

## 🔁 Internal Flow
PDF → Chunking → Embeddings → ChromaDB → Retriever → Phi-3 LLM → Answer  

## ⭐ Why This Project Stands Out
Free: Yes  
Offline: Yes  
No API: Yes  
Privacy: High  
Resume Value: Strong  

## 🚀 Git Commands
```bash 
git init  
git config --global user.name "YourName"  
git config --global user.email "youremail@example.com"  
git remote add origin https://github.com/your-username/AI_ChatBot_RAG.git  
git add .  
git commit -m "Initial RAG chatbot project"  
git branch -M main  
git push -u origin main
```
#pull if we have done changes in git
```bash
git pull origin main 
```

## LIVE DEMO
```bash

```

## Outcome
Shows RAG architecture, vector DB usage, local LLM integration, and full AI system design.
