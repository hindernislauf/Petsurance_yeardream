import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm  # 폰트 관리를 위해 추가
# matplotlib의 설정을 기본 값으로 초기화합니다.

class Vis:
    def __init__(self) -> None:
        pass

    def pont_path(self, font_path):
        plt.rcdefaults()
        # 폰트 경로 설정
        # font_path = '/home/student/workspace/gemini/project/NanumFontSetup_TTF_BARUNGOTHIC/NanumBarunGothic.ttf'
        # 폰트 이름 설정을 위해 fm 모듈 사용
        fe = fm.FontEntry(
            fname=font_path, # ttf 파일이 저장되어 있는 경로
            name='NanumBarunGothic')                        # 이 폰트의 원하는 이름 설정
        fm.fontManager.ttflist.insert(0, fe)              # Matplotlib에 폰트 추가
        plt.rcParams.update({'font.size': 12, 'font.family': 'NanumBarunGothic'}) # 폰트 설정
        font_name = fm.FontProperties(fname=font_path).get_name()
        plt.rc('font', family=font_name)

    
# 보험 약관 데이터
    def get_insurance_data_fig(self):
        data = {
            "보험사": ["현대해상", "삼성화재", "DB손해보험", "KB손해보험"],
            "치료비(보장금액)": ["O", "X", "O", "X"],
            "보험료 비중": [47070, 5565, 47041, 10505],
            '보험료' : ["47,070원", "5,565원", "47,041원", "10,505원"]
        }
        pd.DataFrame(data)
        # fig, ax = plt.subplots()
        # ax.pie(data['보험료 비중'], labels=data['보험사'], autopct='%1.1f%%', startangle=90, colors=['#FF9999','#66B3FF','#99FF99','#FFCC99'])
        # ax.axis('equal')

        fig = plt.figure(figsize=(8,8)) ## 캔버스 생성
        ax = fig.add_subplot() ## 프레임 생성
        
        pie =  ax.pie(data['보험료 비중'], ## 파이차트 출력
            labels=data['보험료'], ## 라벨 출력
            startangle=90, ## 시작점을 90도(degree)로 지정
            #    counterclock=False, ## 시계 방향으로 그린다.
            autopct="%1.1f%%", ## 퍼센티지 출력,
            colors=['#FF9999','#66B3FF','#99FF99','#FFCC99']
            )
        
        plt.legend(pie[0],labels = data['보험사']) 
        # plt.show()
        return fig
    

    def make_markdown(self, st):
        # 이용자를 위한 안내사항
        st.markdown("##### 반려동물을 위한 보험에 관심이 많으신 분들을 위해 만들어진 챗봇입니다. 많은 이용 부탁드리겠습니다.")
        st.markdown("##### 아래에 대한 사항은 여러분들이 관심을 가질만한 내용이라 소개합니다. 상세 약관과 보험료 정보를 알 수 있는 링크와 반려동물 건강관리 가이드라인을 참고해주세요.")
        # 보험사별 상세 약관 보기 링크 제공
        st.markdown("### 보험사별 상세 반려동물 약관 확인하러 가기")
        st.markdown("- [현대해상 약관](https://www.hi.co.kr/FileActionServlet/preview/0/data/202404/0c710e19f5254bac3fbe384dfc6a71e4.pdf)")
        st.markdown("- [삼성화재 약관](https://www.samsungfire.com/publication/pdf/ZPB320040_0_20240401_file1.pdf)")
        st.markdown("- [DB손해보험 약관](https://www.idbins.com/cYakgwanDown.do?FilePath=InsProduct/%EC%95%BD%EA%B4%80_31049(02)_%ED%8E%AB%EB%B8%94%EB%A6%AC%EB%B0%98%EB%A0%A4%EA%B2%AC%EB%B3%B4%ED%97%982404_20240401.pdf)")
        st.markdown("- [KB손해보험 약관](https://www.kbinsure.co.kr/CG802030003.ec?fileNm=24458_1_1.pdf)")
        # 보험료 정보 페이지 링크 제공
        st.markdown("### 보험료 정보 확인하러 가기")
        st.markdown("- [현대해상 보험료 정보](https://www.e-insmarket.or.kr/search.knia)")
        st.markdown("- [삼성화재 보험료 정보](https://www.e-insmarket.or.kr/search.knia)")
        st.markdown("- [DB손해보험 보험료 정보](https://www.e-insmarket.or.kr/search.knia)")
        st.markdown("- [KB손해보험 보험료 정보](https://www.e-insmarket.or.kr/search.knia)")
        # 반려동물 건강관리 가이드라인
        st.markdown("### 반려동물 건강관리 가이드라인")
        st.markdown('''###### 손해보험협회의 반려동물 건강관리 가이드라인 링크를 걸어드리겠습니다.
                    강아지들이 주의해야 할 질환과 일반적인 품종에 대한 성격 소개에, 연령별 건강관리까지....!
                    이 가이드라인을 확인하신다면 여러분들의 동반자의 건강관리에 도움이 되었으면 좋겠습니다..!''')
        st.markdown("- [반려동물 건강관리 가이드라인](https://www.knia.or.kr/consumer/pet/pet_healthcare01)")
        # FAQ
        # 휴먼휴먼 러닝러닝
        st.markdown("### FAQ")
        st.markdown('''
            Q1. 보험료는 어떻게 계산하는 것인가요?
            A1. 보험 상품, 보장 범위 등 여러 요소에 따라서 달라지기 때문에
                명확한 보험료에 대한 답변을 드리기는 어렵습니다. ''')
        st.markdown('''
            Q2. 보험료 청구는 어떻게 하나요?
            A2. 보험금 청구 절차 또한 보험료와 마찬가지로 보험사마다 다를 수 있어서
                명확한 답변을 드릴 수는 없으나, 일반적으로 보험금 청구 사유가 발생한 경우에 관련 서류를 준비하여 보험사에 제출하는 과정이 있습니다.
        ''')
        st.markdown('''
                        Q3. 보험 가입 시에 유의할 점은 무엇인가요?
            A3. 보험 가입 시에 약관을 보시고 보장 내용, 보험료, 면책 사항, 계약 전에 반드시 해야 할 의무, 계약 후에 반드시 해야할 의무를 확인해야 합니다.
                또한 자신의 상황과 반려동물의 상황에 맞는 보험 상품을 선택하는 것이 중요합니다.
        ''')
        st.markdown('''
            Q4. 보험 가입 절차는 어떻게 되나요?
            A4. 보험 상품을 선택하신 이후, 필요한 개인정보를 보험사에 제공 및 보험 계약에 대해서 신청하는 과정이 있습니다.
                이후 보험사의 심사 과정을 거쳐서 가입 여부가 결정됩니다.
        ''')
        st.markdown('''
            Q5. 약관이 무엇인가요?
            A5. 간단하게 말씀드리면, 계약 당사자 일방이 빠른 계약을 체결하기 위해서 미리 마련한 계약문서라고 보시면 됩니다.
                일반적으로 계약은 당사자들이 협의하여 문서를 작성하지만,약관의 경우, 당사자 일방이 미리 만들어 놓았기 때문에 계약 당사자 상대방이 불이익을 받을 가능성이 있어서 약관을 조심히 읽어봐야 합니다.
                                                        ''')
        st.markdown("##### 2024년 4월 18일 기준: 판매처 4곳(출처: 금융감독원 파인 페이지)")
        st.markdown("###### 현대해상 - 다이렉트굿앤굿우리펫보험,월 보험료 : 47,070원")
        st.markdown("###### 삼성화재 - 다이렉트 착한펫보험, 월 보험료 : 5,565원")
        st.markdown("###### DB손해보험 - 프로미라이프 펫블리 반려견 보험, 월 보험료 : 47,041원")
        st.markdown("###### KB손해보험 - 다이렉트 금쪽같은펫보험(강아지), 월 보험료 : 10,505원")
        st.markdown("""
            <style>
            .highlight {
                background-color: yellow;
            }
            </style>
            <span class="highlight">변동가능성이 있으니 선택시 유의하시길 바랍니다.</span>
            """, unsafe_allow_html=True)
        
    def company_link(self,st):
        user_input = st.markdown("### 보험사별 상세 반려동물 약관 확인하러 가기")
        # 보험사별 상세 약관 보기 링크 제공
        st.markdown("- [현대해상 약관](https://www.hi.co.kr/FileActionServlet/preview/0/data/202404/0c710e19f5254bac3fbe384dfc6a71e4.pdf)")
        st.markdown("- [삼성화재 약관](https://www.samsungfire.com/publication/pdf/ZPB320040_0_20240401_file1.pdf)")
        st.markdown("- [DB손해보험 약관](https://www.idbins.com/cYakgwanDown.do?FilePath=InsProduct/%EC%95%BD%EA%B4%80_31049(02)_%ED%8E%AB%EB%B8%94%EB%A6%AC%EB%B0%98%EB%A0%A4%EA%B2%AC%EB%B3%B4%ED%97%982404_20240401.pdf)")
        st.markdown("- [KB손해보험 약관](https://www.kbinsure.co.kr/CG802030003.ec?fileNm=24458_1_1.pdf)")
        st.markdown("---")

    def info_link(self, st):
        st.markdown("### 보험료 정보 확인하러 가기")
        st.markdown("- [현대해상 보험료 정보](https://www.e-insmarket.or.kr/search.knia)")
        st.markdown("- [삼성화재 보험료 정보](https://www.e-insmarket.or.kr/search.knia)")
        st.markdown("- [DB손해보험 보험료 정보](https://www.e-insmarket.or.kr/search.knia)")
        st.markdown("- [KB손해보험 보험료 정보](https://www.e-insmarket.or.kr/search.knia)")
        st.markdown("---")

        st.markdown("##### 2024년 4월 18일 기준: 판매처 4곳(출처: 금융감독원 파인 페이지)")
        st.markdown("")
        st.markdown("###### 현대해상 - 다이렉트굿앤굿우리펫보험,월 보험료 : 47,070원")
        st.markdown("###### 삼성화재 - 다이렉트 착한펫보험, 월 보험료 : 5,565원")
        st.markdown("###### DB손해보험 - 프로미라이프 펫블리 반려견 보험, 월 보험료 : 47,041원")
        st.markdown("###### KB손해보험 - 다이렉트 금쪽같은펫보험(강아지), 월 보험료 : 10,505원")
        st.markdown("""
                <style>
                .highlight {
                    background-color: yellow;
                }
                        
                </style>
                <span class="highlight">변동가능성이 있으니 선택시 유의하시길 바랍니다.</span>
                """, unsafe_allow_html=True)
        st.markdown("")
        
    def Q_A(self, st):
        st.markdown("### FAQ")
        st.markdown('''
            Q1. 보험료는 어떻게 계산하는 것인가요? 
                
            A1. 보험 상품, 보장 범위 등 여러 요소에 따라서 달라지기 때문에
                명확한 보험료에 대한 답변을 드리기는 어렵습니다. ''')
        st.markdown("---")
        st.markdown('''
            Q2. 보험료 청구는 어떻게 하나요?
                    
            A2. 보험금 청구 절차 또한 보험료와 마찬가지로 보험사마다 다를 수 있어서
                명확한 답변을 드릴 수는 없으나, 일반적으로 보험금 청구 사유가 발생한 경우에 관련 서류를 준비하여 보험사에 제출하는 과정이 있습니다.
        ''')
        st.markdown("---")
        st.markdown('''
                        Q3. 보험 가입 시에 유의할 점은 무엇인가요?
                    
            A3. 보험 가입 시에 약관을 보시고 보장 내용, 보험료, 면책 사항, 계약 전에 반드시 해야 할 의무, 계약 후에 반드시 해야할 의무를 확인해야 합니다.
                또한 자신의 상황과 반려동물의 상황에 맞는 보험 상품을 선택하는 것이 중요합니다.
        ''')
        st.markdown("---")
        st.markdown('''
            Q4. 보험 가입 절차는 어떻게 되나요?
                    
            A4. 보험 상품을 선택하신 이후, 필요한 개인정보를 보험사에 제공 및 보험 계약에 대해서 신청하는 과정이 있습니다.
                이후 보험사의 심사 과정을 거쳐서 가입 여부가 결정됩니다.
        ''')
        st.markdown("---")
        st.markdown('''
            Q5. 약관이 무엇인가요?
                   
            A5. 간단하게 말씀드리면, 계약 당사자 일방이 빠른 계약을 체결하기 위해서 미리 마련한 계약문서라고 보시면 됩니다.
                일반적으로 계약은 당사자들이 협의하여 문서를 작성하지만,약관의 경우, 당사자 일방이 미리 만들어 놓았기 때문에 계약 당사자 상대방이 불이익을 받을 가능성이 있어서 약관을 조심히 읽어봐야 합니다.
                                                        ''')
        st.markdown("---")

    def guide(self, st):
        st.markdown("### 반려동물 건강관리 가이드라인")
        st.markdown('''###### 손해보험협회의 반려동물 건강관리 가이드라인 링크를 걸어드리겠습니다.
                        강아지들이 주의해야 할 질환과 일반적인 품종에 대한 성격 소개에, 연령별 건강관리까지....!
                        이 가이드라인을 확인하신다면 여러분들의 동반자의 건강관리에 도움이 되었으면 좋겠습니다..!''')
        st.markdown("- [반려동물 건강관리 가이드라인](https://www.knia.or.kr/consumer/pet/pet_healthcare01)")
        st.markdown("---")

