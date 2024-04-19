from vector_store import *
from pdf_processor import *


class Retriever:
    def __init__(self) -> None:
        pass

    def retrieve_as_retriever(self, vectordb,  k = 4):
        retriever = vectordb.as_retriever(k = k)
        return retriever
