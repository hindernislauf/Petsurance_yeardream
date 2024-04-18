


#from langchain_community.document_loaders import PyMuPDFLoader
from langchain_ai21 import AI21SemanticTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
from tqdm import tqdm
from langchain_community.document_loaders import PyPDFLoader
#from pdf_processor import Pdf_Processor




loader = PyPDFLoader("/home/student/workspace/langlabprac/pet.pdf")
text_list = loader.load()  #raw text
doc = ''
for raw_text in tqdm(text_list):
    text = raw_text.page_content
    doc += text

print(type(doc))

if "AI21_API_KEY" not in os.environ:
    os.environ["AI21_API_KEY"] = "A6qUrfvykak5ziIdrxqtuBG9uOtaTluf"  # 실제 API 키로 교체


def vectorize_save(doc):
    #print(text_list)
    #total_chunks = []

    # 30글자 이상 100,000 글자 이하 
    
    splitted = []
    flag = True
    i = 0

    while True :
        try:
            splitted.append([doc[i:i+100000]])
            i += 100000
            break
        except:
            splitted.append([doc[i:]])
            break

    print(splitted[0])
    print(i)
    # while flag:
    #     try:
    #         split_item = doc[i*100000:(i+1)*100000]
    #         splitted.append(split_item)
    #         i +=1
    #     except IndexError:
    #         splitted.append(split_item)
    #         flag = False



   
    semantic_text_splitter = AI21SemanticTextSplitter(
        1000,
        0,
        None,
        "A6qUrfvykak5ziIdrxqtuBG9uOtaTluf",
    )


    
    chunks = semantic_text_splitter.split_text(doc)
    print(chunks)
            
    embeddings_model = HuggingFaceEmbeddings(
        model_name='jhgan/ko-sbert-nli',
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True},
    )
        
    vectorstore = FAISS.from_texts(chunks,
                                    embedding=embeddings_model,
                                    distance_strategy=DistanceStrategy.COSINE
                                    )
    print(vectorstore)
        

vectorize_save(doc)