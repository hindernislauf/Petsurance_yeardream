import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from pdf_processor import *
from vector_store import *
from retriever import Retrievers
from gemini import *

class Gemini_create:
    def __init__(self) -> None:
        pass

    def load_api(self,api):
        if "GOOGLE_API_KEY" not in os.environ:
            os.environ["GOOGLE_API_KEY"] = api
    
    def create_chat(self):
        chat = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest', temperature= 0.5, top_k = 2)
        return chat

    def create_prompt(self):
    #     prompt = ChatPromptTemplate.from_messages(
    # [
    #     ('system' , '{context} 안에서 답을 찾아줘') ,# 답변을 yes 아니면 no로만 해라 - System이
    #     MessagesPlaceholder(variable_name ='message') #위의 것을 어떤 변수로서 쓰겠다를 지정한 것 -> 그냥 이런식으로 사용됨
    # ]
    # )
        template = """Answer the question based only on the following context: {context}

                Question: {question}
                """
        
        prompt = ChatPromptTemplate.from_template(template)
        return prompt
    

# if __name__ == "__main__":
#     G = Gemini_create()
#     api = ""
#     G.load_api(api)

#     chat = G.create_chat()
#     prompt = G.create_prompt()
#     chain = prompt | chat | StrOutputParser()

#     # PDF 문서 처리 (pdf -> text)
#     P = Pdf_Proccessor()
#     text = P.pdf_load("/home/student/workspace/gemini/project/promy_petvely.pdf")

#     # text -> DB
#     V_S = Vector_store()
#     vectordb = V_S.make_vector_db(text)
#     docs = Retriever().retrieve_document(vectordb, "슬개골 알려줘")
#     print(docs)

#     try:
#         response = chain.invoke(
#             {   'context' : docs,
#                 'message' : [HumanMessage("슬개골 알려줘")] }
#         )

#         print(response)
#     except:
#         response = chat.invoke(input="슬개골 알려줘")
#         print(response.content)