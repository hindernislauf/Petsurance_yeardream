import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyDoXQh75wHDJV4S3is1WqniPzCjzqwPwSU"

# web document를 가져오는 함수.
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
text = loader.load() # raw text

# 500글자씩 자르는데, 안겹치게 자름.
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
splits = text_splitter.split_documents(text)
#print(len(splits))

# split 해놓은 텍스트 데이터를 embedding한 VectorDB를 생성
vectordb = Chroma.from_documents(documents=splits,
                                 embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))

# 사용자 입력(질문)과 비교해서 가까운 K개의 결과 찾기
retriever = vectordb.as_retriever(k=1)

# 검색
input_prompt = input("User : ")
response = retriever.invoke(input=input_prompt)
print(response)
