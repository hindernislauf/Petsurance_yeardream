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
    def make_and_load_vector_db(self, text_list, directory_path = "./chroma2_db"):
        if not os.path.isdir(directory_path):
            vectordb = Chroma.from_texts(texts= text_list,
                                embedding= GoogleGenerativeAIEmbeddings(model= "models/embedding-001")
                                , persist_directory= directory_path)
        else:
            vectordb = Chroma(persist_directory=directory_path, embedding_function = GoogleGenerativeAIEmbeddings(model= "models/embedding-001"))

        return vectordb
    
    
