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
from retriever import Retriever
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
    # ]Answer the question based only on the following context: 
    # )
        template = """{context} 에 있는 것으로만 답하고, 한국어로만 답해줘.
                
                Question: {question}
                """
        
        prompt = ChatPromptTemplate.from_template(template)
        return prompt
    
    def create_prompt_sum(self):
        # template = """ 테이블 형식으로 만들수 있게 간결하게 대답해야해.
        #         """
        
        prompt = ChatPromptTemplate.from_messages(
    [
        ('system' , "테이블 형식으로 만들수 있게 간결하게 대답해야해.") ,# 답변을 yes 아니면 no로만 해라 - System이
        MessagesPlaceholder(variable_name ='message') #위의 것을 어떤 변수로서 쓰겠다를 지정한 것 -> 그냥 이런식으로 사용됨

    ]
    )
        # prompt = ChatPromptTemplate.from_template(template)
        return prompt
    
