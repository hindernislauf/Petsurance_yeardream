from vector_store import *
from pdf_processor import *
import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

class Retrievers:
    def __init__(self) -> None:
        pass

    def retrieve_as_retriever(self, vectordb,  k = 4):
        retriever = vectordb.as_retriever(k = k)
        # docs  = retriever.get_relevant_documents(query)
        return retriever
    
    def format_docs(docs):
        return "\n\n".join([d.page_content for d in docs])

# if __name__ == "__main__":
#     if "GOOGLE_API_KEY" not in os.environ:
#         os.environ["GOOGLE_API_KEY"] = ""

#     # PDF 문서 처리 (pdf -> text)
#     P = Pdf_Proccessor()
#     text = P.pdf_load("/home/student/workspace/gemini/project/promy_petvely.pdf")

#     # text -> DB
#     V_S = Vector_store()
#     vectordb = V_S.make_vector_db(text)
#     docs = Retriever().retrieve_document(vectordb, "슬개골 알려줘")
#     print(docs)