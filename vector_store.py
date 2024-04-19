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
    def make_vector_db(self, text_list, directory_path = "./chroma_db"):

        vectordb = Chroma.from_texts(texts= text_list,
                                embedding= GoogleGenerativeAIEmbeddings(model= "models/embedding-001")
                                , persist_directory= directory_path)

        return vectordb
    
    def load_vectordb(self, directory_path = "./chroma_db"):
        vectordb = Chroma(persist_directory=directory_path, embedding_function = GoogleGenerativeAIEmbeddings(model= "models/embedding-001"))
        return vectordb
    
    
# if __name__ == "__main__":

#     if "GOOGLE_API_KEY" not in os.environ:
#         os.environ["GOOGLE_API_KEY"] = "AIzaSyDarfOpN-0E8Oa6uiI-etHkWfgWlOh9b-s"
#     P = Pdf_Proccessor()
#     text_list = P.pdf_load("/home/student/workspace/gemini/project/promy_petvely.pdf")
#     V_S = Vector_store()
#     directory_path = "/home/student/workspace/gemini/project/chroma_db"
#     if os.path.isdir(directory_path):
#         vectordb = V_S.load_vectordb(directory_path)
#     else:
#         vectordb = V_S.make_vector_db(text_list, directory_path)
#     print(vectordb)