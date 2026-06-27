# 📄 PDF RAG Assistant

A Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and ask natural language questions about their contents.

The application uses **LangChain**, **Google Gemini Embeddings**, and **ChromaDB** to retrieve the most relevant document chunks before generating an answer with **Gemini 2.5 Flash**, reducing hallucinations by grounding responses in the uploaded document.

---

## 🚀 Features

* 📄 Upload any PDF document
* 🔍 Semantic document search using vector embeddings
* 🧩 Automatic document chunking with overlap
* 🗂️ ChromaDB vector store for efficient retrieval
* 🤖 Grounded question answering using Gemini 2.5 Flash
* ⚡ Cached vector store for improved performance
* 🌐 Clean Streamlit web interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Google Gemini API
* ChromaDB
* PyPDFLoader
* python-dotenv

---

## 📂 Project Structure

```text
pdf-rag-assistant/
│
├── app.py
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## ⚙️ Installation

```bash
git clone https://github.com/diwakar7619/pdf-rag-assistant.git

cd pdf-rag-assistant

uv sync
```

Create a `.env` file:

```text
GOOGLE_API_KEY=your_api_key
```

Run the application:

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. Upload a PDF document.
2. Extract text using PyPDFLoader.
3. Split the document into overlapping chunks.
4. Generate embeddings using Gemini Embeddings.
5. Store embeddings in ChromaDB.
6. Embed the user's query.
7. Retrieve the most relevant chunks using similarity search.
8. Pass the retrieved context to Gemini 2.5 Flash.
9. Display a grounded answer.

---

## 💡 Example Questions

* Summarize this document.
* What is the PNR number?
* Who are the passengers?
* Explain the main topic of this report.
* What are the key recommendations?

---

## 📚 Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Vector Databases
* Document Chunking
* Prompt Engineering
* LangChain Pipelines
* Streamlit Application Development

---

## 🔮 Future Improvements

* Multi-document support
* Persistent vector database
* Source citations with page numbers
* Conversation memory
* Streaming responses
* Docker deployment

---

## 👨‍💻 Author

**Pratham Diwakar**

GitHub: https://github.com/diwakar7619
