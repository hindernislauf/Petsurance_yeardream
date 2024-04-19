import streamlit as st
from pdf_processor import *
from vector_store import *
from retriever import *
from chain_response import Chain_Response
from vis import *
from crawler import * 
from PIL import Image
from front_end import streamlit_run



# 절대경로로 지정해주기
pdf_path = "/home/student/workspace/gemini/project/data/pdf/{}"
directory_path = "/home/student/workspace/gemini/project/data/db/{}_db"
img_path = '/home/student/workspace/gemini/project/data/logo_all_companies.png'
pont_path = '/home/student/workspace/gemini/project/NanumFontSetup_TTF_BARUNGOTHIC/NanumBarunGothic.ttf'

# 회사 dict 만들기
company_dict = {
    "현대해상다이렉트" : ["굿앤굿우리펫보험", "(무)현대해상다이렉트굿앤굿우리펫보험(Hi2404)_스탠다드플랜.pdf", "hddirect"],
    "삼성화재" : ["착한펫보험(강아지)", "무배당_삼성화재_다이렉트_착한펫보험(강아지)(2404.1)(자동갱신형).pdf", "samsungfire"],
    "DB손해보험" : ["반려견보험", "프로미라이프_펫블리_반려견보험2404.pdf", "idbins"],
    "KB다이렉트" : ["금쪽같은펫보험", "KB_다이렉트_금쪽같은펫보험(강아지)(무배당)(24.04).pdf", "kbinsure"]
}
#폰트 설정
V = Vis()
V.pont_path(pont_path)


api = ""
Chain_r = Chain_Response(api)

streamlit_run(Chain_r, company_dict,pdf_path,directory_path, img_path, V )
