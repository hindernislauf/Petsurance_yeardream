import streamlit as st
from pdf_processor import *
from vector_store import *
from retriever import Retrievers
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
from langchain_core.runnables import RunnablePassthrough

#
G = Gemini_create()
api = "AIzaSyDarfOpN-0E8Oa6uiI-etHkWfgWlOh9b-s"
G.load_api(api)


# PDF 문서 처리 (pdf -> text)
P = Pdf_Proccessor()
pdf_path = "/home/student/workspace/gemini/project/promy_petvely.pdf"
text_list = P.pdf_load(pdf_path)

# text -> DB

V_S = Vector_store()
directory_path = "/home/student/workspace/gemini/project/chroma_db"
new_directory_path = "./chroma_db"
# 폴더(백터디비 저장한 폴더)가 있으면, 새로 생성하는 작업을 하지 않음  없으면 새로 생성


# print(chain.invoke(input = "술에 대한 법 알려줘"))


st.title('강아지 보험 비교 챗봇')
# 펫보험 약관 검색 챗봇
user_input = st.text_input("보험에 대해 궁금한 점을 입력하세요:")

if st.button('질문하기'):
    # try:
    if os.path.isdir(directory_path):
        vectordb = V_S.load_vectordb(directory_path)
    else:
        vectordb = V_S.make_vector_db(text_list, new_directory_path)

    # 리트리버 생성
    R = Retrievers()
    retriever = R.retrieve_as_retriever(vectordb, k = 4 )

    # 챗봇 히스토리 초기화
    initialize_history()


    chat = G.create_chat()
    prompt = G.create_prompt()

    def format_docs(docs):
        return "\n\n".join([d.page_content for d in docs])

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | chat
        | StrOutputParser()
    )
    response = chain.invoke( user_input)

    print(response)
    # except:
    #     response_c = chat.invoke(input=user_input)
    #     response = response_c.content
    #     print(response)

    st.write(f"답변되었습니다. {response}")
    