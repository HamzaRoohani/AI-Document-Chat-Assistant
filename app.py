from PyPDF2 import PdfReader
import gradio as gr
from dotenv import load_dotenv
import os
from google import genai
import faiss
import numpy as np
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

def process(pdf):
    reader = PdfReader(pdf)
    pages = [page.extract_text() for page in reader.pages[:100]]
    
    chunks = []
    for i in range(0, len(pages), 5):
        chunks.append(" ".join(pages[i:i+5]))
    
    embeddings = []
    for chunk in chunks:
        response = client.models.embed_content(
            model="models/gemini-embedding-001",
            contents=chunk
        )
        embeddings.append(response.embeddings[0].values)
        time.sleep(1)
    
    vectors = np.array(embeddings).astype("float32")
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    return index, chunks
    
def search(question, index, chunks):
    response = client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=question
    )
    question_vector = np.array(response.embeddings[0].values).astype("float32").reshape(1, -1) 
    _, indices = index.search(question_vector, k=10)
    return [chunks[i] for i in indices[0]]

def answer(pdf, question):
    index, chunks = process(pdf)
    relevant_chunks = search(question, index, chunks)
    context = "\n".join(relevant_chunks)
    prompt = "Answer the question based only on the following context:\n" + context + "\nQuestion: " + question
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

app = gr.Interface(fn=answer, inputs=[gr.File(label="Upload PDF"), gr.Textbox(label="Question")], outputs=gr.Textbox(label="Answer"), title="AI Document Chat Assistant", description="Upload any PDF and ask questions about it!")
app.launch()