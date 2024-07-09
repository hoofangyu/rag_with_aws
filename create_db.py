from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from helpers.embedding_function import get_embedding_function
import defaults
import os
import shutil

CHROMA_PATH = defaults.CHROMA_PATH

def load_documents():
    loader = PyPDFLoader("data/hpp_policy_2024.pdf")
    pages = loader.load_and_split()
    return pages

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=300,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)

def save_to_chroma(chunks, CHROMA_PATH, embeddings):
    if os.path.exists(CHROMA_PATH):
        print("Path exists, proceeding to empty contents!")
        shutil.rmtree(CHROMA_PATH)
        print("Contents emptied, proceeding to create DB :D")

    db = Chroma.from_documents(
        chunks, embeddings, persist_directory=CHROMA_PATH)

    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

if __name__ == "__main__":
    documents = load_documents()
    chunks = split_documents(documents)
    embeddings = get_embedding_function()
    save_to_chroma(chunks,CHROMA_PATH, embeddings)
    print("Database has been created successfully :)")