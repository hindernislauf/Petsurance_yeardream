import streamlit as st
from crawler import * 
from PIL import Image

def streamlit_run(Chain_r, company_dict,pdf_path,directory_path, img_path, V ):
    option = st.sidebar.selectbox(
    "보험 정보를 어떻게 도와드릴까요?",
    ("펫 보험 비교", "보험 약관 검색","보험사 소개","보험사별 상세 약관 링크","보험료 정보","반려동물 건강관리 가이드라인" ,"FAQ")
)

    if option == "펫 보험 비교":
        # Streamlit 애플리케이션 타이틀 설정
        st.title(f'마이펫 헬스 DB - {option}')
        user_input = st.text_input("어떤 펫 보험에 대해서 알고싶으신가요?  호윽시 강아지 보험?")
        if st.button('보험사 간단 비교하기'):   
            print("crawling start")   
            # 크롤링
            C = Crawler()
            C.set_browserstack()
            crawling_response = C.crawerling(user_input)
            st.table(crawling_response)

    elif option == "보험 약관 검색":
        st.title(f'마이펫 헬스 DB - {option}')
        user_input = st.text_input("보험 약관에 대해서 질문해 주세요:")
        radio_option = st.radio(label = '보험사를 선택할 수 있어요', options = ['ALL', '현대해상다이렉트', '삼성화재', 'DB손해보험', 'KB다이렉트'])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        
        if radio_option == "ALL":
            st.write(f"회사별로 요약된 정보만 제공합니다.\n더 자세한 내용을 원하신다면 보험사를 선택해주세요\n\n\n\n\n ")
            if user_input == "":
                st.write("검색어를 입력해주세요")
            else:
                st.write("답변을 찾는 중입니다 조금만 기다려주세요")
                output_response = Chain_r.all_company_response(company_dict, user_input, pdf_path, directory_path)
                last_respose = Chain_r.make_response_sum(f"{output_response} 을 가지고 회사별로 내용을 200자 이하로 짧게 요약해주라.")
                st.empty().write("")
                st.write(f"답변되었습니다.\n {last_respose}")
        else :
            if user_input == "":
                st.write("검색어를 입력해주세요")
            else:
                print(radio_option)
                st.write("답변을 찾는 중입니다 조금만 기다려주세요")
                output_response = Chain_r.each_company_response(radio_option, user_input, pdf_path, directory_path ,company_dict)
                st.empty().write("")
                st.write(f"답변되었습니다. {radio_option} \n \n {output_response}")

    elif option == "보험사 소개":
        st.title(f'마이펫 헬스 DB - {option}')
        def load_image(image_file): # 참고 링크: https://kyeonghyeon86.tistory.com/22
            img = Image.open(image_file)
            return img
        
        img = load_image(img_path)
        st.image(img, width=800)

    elif option == "보험사별 상세 약관 링크":
        st.title(f'마이펫 헬스 DB - {option}')
        V.company_link(st)

    elif option == "보험료 정보":
        st.title(f'마이펫 헬스 DB - {option}')
        V.info_link(st)
        fig = V.get_insurance_data_fig()
        st.pyplot(fig)

    elif option ==  "FAQ":
        st.title(f'마이펫 헬스 DB - {option}')
        V.Q_A(st)

    elif option == "반려동물 건강관리 가이드라인":
        st.title(f'마이펫 헬스 DB - {option}')
        V.guide(st)
