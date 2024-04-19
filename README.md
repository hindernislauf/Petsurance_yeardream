# _(이어드림 4기_온라인10조) LangChain을 이용한 App 개발 PJT_
## 주제 :  반려견 보험 비교 챗봇 
#### 반려견 보험 선택을 도와주는 4가지 보험사(현대해상다이렉트, 삼성화재, DB손해보험, KB손해보험)의 약관 및 가격 비교 챗봇

---
# 📋 contexts 
[2.상세 task](#2.상세-task)
## 1. 프로젝트 소개
### 반려견 보험 비교 챗봇
##### 반려견 양육가구 400만시대(2023년 한국 반려동물보고서) 반려견을 위한 보험을 위한 수요가 증가함.
##### 4개의 보험사의 보장내역과 가격을 비교하는 챗봇을 구현 
---
### 목표
#### 반려견을 보험 선택을 도와주는 4개 보험사 비교와 보장범위 축약
![image](https://github.com/hindernislauf/langlab/assets/166089376/4702b92b-40cf-44ed-8b06-a04aee0e3375)



---
### 수행 기간 및 팀원 :  
- 📆 수행기간: 2024.04.17 ~ 2024.04.19
- ⭐ 팀원
  
| 강상우  | 송유창  | 신윤재  | 이유진  | 이진선  | 이진아  |
|--------|--------|--------|--------|--------|--------|
| ![Avatar 1](https://avatars.githubusercontent.com/u/160104734?v=4)| ![Avatar 2](https://avatars.githubusercontent.com/u/87472756?v=4)| ![Avatar 3](https://avatars.githubusercontent.com/u/140726268?v=4) | ![Avatar 4](https://avatars.githubusercontent.com/u/95261468?v=4)| ![Avatar 5](https://avatars.githubusercontent.com/u/166676809?v=4)| ![GitHub Avatar](https://avatars.githubusercontent.com/u/166089376?v=4) |
| [Github](https://github.com/allenkang92) | [Github](https://github.com/hindernislauf) | [Github](https://github.com/yoonjaeo)| [Github](https://github.com/Developer-Yujin)| [Github](https://github.com/Jinsun577)| [Github](https://github.com/ssukddeok) |
---
### repo structure : 

---
### Project Workflow 
---
#### (→ 자동으로 서브 주제 생성 → 서브 주제 선택 → 최종 스크립트 생성 및 출력

## 2. 상세 task

#### LLM 선정 모델
- 목표
  - 원하는 내용/보장 범위/충분한 분량이 생성 가능한 LLM 모델 선정
  - LLM 모델에 맞는 최적 프롬프트 도출

- LLM 선정 모델 
  - gemini-1.5-pro-latest
    
-  주제 생성 랭체인 구축
    -  입력 받은 주제로 LLM 출력
    -  질문 입력 → LLM → 4개사 보험 비교와 보장내역 요약 출력

### Frontend
## ![스크린샷 2024-04-19 오후 4 29 18](https://github.com/hindernislauf/langlab/assets/166089376/eb5da97a-d207-4603-87a0-539832f74a38)

  - UI 기획
    - 사이드바 생성
    - 검색 창 생성 
    - 보험사 소개 표시 화면
    - 보험사 비교 및 요약 결과 출력 화면

### Backend
- Streamlit로 웹 애플리케이션 구축
  - 사용자의 입력을 받아 처리하며, 그 결과를 HTML 템플릿에 전달하여 동적인 웹 페이지를 생성
  - 보험 표시 버튼과 스크립트 생성 버튼이 눌렸을 때, 사용자의 입력 및 선택된 옵션에 따라 동적으로 서버 측 로직을 수행
    - 로직: 프롬프트와 LLM으로 구성된 LangChain을 invoke


### LangChain
- Chat model : gemini-1.5-pro-latest

- Selenium 라이브러리 활용.
  - ex) ‘webdriver’, ‘Keys’, ‘By’, ‘WebDriverWait’, ‘expected_conditions’, ‘ChromeOptions’
- Selenium 스크립트를 로컬에서 작성 후 BrowserStack에 전송하여 클라우드 서비스를 활용한 원격 웹드라이브 실행, 테스트 프로세스 구축
- BrowserStack 사용: 다양한 브라우저와 운영체제 환경에서의 호환성 테스트를 위함
- 보험 관련 랭체인 구축
  -  입력 받은 메인 주제로 LLM 출력
  -  메인 주제 입력 → LLM → 4개사 보험 비교와 보장내역 요약 출력


-
## 3. 결과 및 프로젝트 회고
![image](https://github.com/hindernislauf/langlab/assets/166089376/90f95c53-30f7-4ca6-b744-ad491a3d8879)
![image](https://github.com/hindernislauf/langlab/assets/166089376/3065b1cf-0fbe-4af2-a904-9579119f8caa)
![image](https://github.com/hindernislauf/langlab/assets/166089376/d0c83b1d-db37-4ae3-bd76-28bf27c2944c)
![image](https://github.com/hindernislauf/langlab/assets/166089376/e07a0303-6f45-483c-8357-4548102718a2)
![image](https://github.com/hindernislauf/langlab/assets/166089376/ed7cb4e2-8d90-4261-9026-d019f8c5fb38)
![image](https://github.com/hindernislauf/langlab/assets/166089376/7c110b02-db79-4725-a9b9-506a9f2580bb)
![image](https://github.com/hindernislauf/langlab/assets/166089376/7e300bc6-eee6-45a9-90fc-eec5ab9cd781)




---
## 4. 러닝포인트

#### ✅ 팀원들간의 레벨과 생각 등이 다른데, 사람언어로뿐만이 아니라 코드 및 문서 등으로 커뮤니케이션해야했던 점이 어려웠습니다. 
#### ✅ 처음 기획 단계에서 각자의 역할 및 전체 코드 구성 등을 명확히 할수록 이후 프로세스가 윤활 해짐을 배웠습니다.
#### ✅ main.py 디자인 정확도를 보안, 디벨롭 예정입니다. 
