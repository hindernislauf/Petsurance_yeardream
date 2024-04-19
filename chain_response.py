import streamlit as st
from pdf_processor import *
from vector_store import *
from retriever import Retriever
from gemini import Gemini_create
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

class Chain_Response:
    def __init__(self, api) -> None:
        # api = "AIzaSyDarfOpN-0E8Oa6uiI-etHkWfgWlOh9b-s"
        self.G = Gemini_create()
        self.G.load_api(api)

        self.P = Pdf_Proccessor()
        self.V_S = Vector_store()

    def make_response(self,vectordb, input):
        R = Retriever()
        retriever = R.retrieve_as_retriever(vectordb, k = 4 )

        chat = self.G .create_chat()
        prompt = self.G .create_prompt()

        def format_docs(docs):
            return "\n\n".join([d.page_content for d in docs])

        chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | chat
            | StrOutputParser()
        )
        
        response = chain.invoke( input)
        return response
    
    def make_response_sum(self , input):
        chat = self.G.create_chat()
        prompt = self.G.create_prompt_sum()

        chain = (prompt| chat| StrOutputParser())
        response = chain.invoke(
            {'message' : [HumanMessage(input)] }
        )
        return response
    
    def all_company_response(self, company_dict, input , pdf_path, directory_path):
        output_string = ""
        for k,v in company_dict.items():
            print(k)
            output_string += f'{k}의 회사는 '
            text_list = self.P.pdf_load(pdf_path.format(v[1]))
            vectordb = self.V_S.make_and_load_vector_db(text_list, directory_path.format(v[-1]))
            response = self.make_response(vectordb,input )
            print(response)
            output_string += f'{response}의 내용이야. '
            print()
        return output_string

    def each_company_response(self,company_name, input , pdf_path, directory_path ,company_dict):
        text_list = self.P.pdf_load(pdf_path.format(company_dict[company_name][1]))
        vectordb = self.V_S.make_and_load_vector_db(text_list, directory_path.format(company_dict[company_name][-1]))
        output_string = self.make_response(vectordb,input )
        return output_string