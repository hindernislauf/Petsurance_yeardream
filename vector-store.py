# 수집된 데이터를 처리하고, 검색 가능한 형태로 변환하여 데이터베이스에 저장합니다. 
import gemini
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_ai21 import AI21SemanticTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
from langchain_community.embeddings import HuggingFaceEmbeddings


def vectorize_save():
    loader = PyMuPDFLoader(pdf())
    data = loader.load()
    semantic_text_splitter = AI21SemanticTextSplitter()
    chunks = semantic_text_splitter.split_text(loader)


    embeddings_model = HuggingFaceEmbeddings(
        model_name='jhgan/ko-sbert-nli',
        model_kwargs={'device':'cpu'},
        encode_kwargs={'normalize_embeddings':True},
    )


    vectorstore = FAISS.from_documents(chunks,
                                    embedding = embeddings_model,
                                    distance_strategy = DistanceStrategy.COSINE  
                                    )
    
    return vectorstore