# from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import os
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
import pickle
from pdf_processor import *


class Vector_store:
    def __init__(self) -> None:
        pass
    
    #vecto
    def make_vector_db(self, text, chunk_size = 1000, chunk_overlap = 200):

        text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap) 
        split = text_splitter.split_documents(text)
        vectordb = Chroma.from_documents(documents= split,
                                        embedding= GoogleGenerativeAIEmbeddings(model= "models/embedding-001")
                                        )
        return vectordb
    
    # def save_vectordb(self, vectordb, vector_name = "vector"):
    #     with open(f'{vector_name}.pickle', 'wb') as f:
    #         pickle.dump(vectordb, f, pickle.HIGHEST_PROTOCOL)

    # def load_vectordb(self, vector_name = 'vector'):
    #     with open('try.pickle', 'rb') as f:
    #         vectordb = pickle.load(f)
    #     return vectordb
    
if __name__ == "__main__":

    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = "AIzaSyCx5DAM5VTvRqYwsyQWTaq9FB-GmLNkeys"
    P = Pdf_Proccessor()
    text = P.pdf_load("/home/student/workspace/langlab/pet.pdf")
    V_S = Vector_store()
    vectordb = V_S.make_vector_db(text)
    print(vectordb)