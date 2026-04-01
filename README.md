---
title: AI Document Chat Assistant
emoji: 📉
colorFrom: green
colorTo: gray
sdk: gradio
sdk_version: 6.10.0
app_file: app.py
pinned: false
license: mit
short_description: Chat Assistant Built to Answer Question Related to a PDF
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

AI Document Chat Assistant

An intelligent RAG-powered app that lets you upload any PDF and ask questions about it, getting precise answers directly from the document!

Try it on Hugging Face Spaces: huggingface.co/spaces/HamzaRoohani/AI-Document-Chat-Assistant 

Workflow
- Reads your PDF and splits it into chunks
- Converts chunks into vectors (embeddings) for semantic search
- Finds the most relevant chunks based on your question
- Sends only relevant content to Gemini for a precise answer

This means the AI answers only from your document, not from its own memory!

What It Does
- Upload any PDF document (up to 100 pages)
- Ask any question about the document
- Get precise answers based only on the document content
- Powered by Google Gemini + FAISS vector search

Tech Stack
- Google Gemini 2.5 FlashLLM 
- Google Gemini Embeddings
- FAISS
- PyPDF2
- NumPy
- Gradio 
- Hugging Face

How It Works
- User uploads PDF
- PDF split into chunks (5 pages each)
- Chunks converted to vectors (Gemini Embeddings)
- Vectors stored in FAISS index
- User asks a question
- Question converted to vector
- FAISS finds top 3 most similar chunks
- Relevant chunks sent to Gemini
- Precise answer returned!

Limitations
- Processes first 200 pages of PDF (free tier limitation)
- Response time ~40-60 seconds on free tier API
- For production use, a paid API key would remove these limits

Author: Hamza Roohani

Hugging Face: HamzaRoohani

License: This project is licensed under the MIT License.