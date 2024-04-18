# 애플리케이션의 메인 실행 흐름을 제어하는 모듈.

import streamlit as st
from pdf_processor import *
from vector_store import *
from retriever import Retriever
from gemini import Gemini_create
from logger import *
import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser

#
G = Gemini_create()
api = "AIzaSyCx5DAM5VTvRqYwsyQWTaq9FB-GmLNkeys"
G.load_api(api)

chat = G.create_chat()
prompt = G.create_prompt()
chain = prompt | chat | StrOutputParser()

# PDF 문서 처리 (pdf -> text)
P = Pdf_Proccessor()
text = P.pdf_load("/home/student/workspace/langlab/pet.pdf")

# text -> DB
V_S = Vector_store()
vectordb = V_S.make_vector_db(text) #pdf의 텍스트를 벡터화 시켜서 db에 저장된 것을 불러오는 것
#docs = Retriever().retrieve_document(vectordb, "슬개골 알려줘") # 
# print(docs)

# try:
#     response = chain.invoke(
#         {   'context' : docs,
#             'message' : [HumanMessage("슬개골 알려줘")] }
#     )

#     print(response)
# except:
#     response = chat.invoke(input="슬개골 알려줘")
#     print(response.content)



# 챗봇 히스토리 초기화
#initialize_history()



# st.title('강아지 보험 비교 챗봇')
# user_input = st.text_input("보험에 대해 궁금한 점을 입력하세요:")

# if st.button('질문하기'):
docs = Retriever().retrieve_document(vectordb, "쓸개골 탈구에는 어떤 보험 혜택을 받을 수 있을까?")

try:
    response = chain.invoke(
        {   'context' : docs,
            'message' : [HumanMessage("쓸개골 탈구에는 어떤 보험 혜택을 받을 수 있을까?")] }
    )

    print(response)
except:
    response_c = chat.invoke(input="쓸개골 탈구에는 어떤 보험 혜택을 받을 수 있을까?")
    response = response_c.content
    print(response)

    #st.write(f"답변되었습니다. {response}")
    