# 라이브러리 설치
우선 이번에 필요한 다음 라이브러리를 설치 해주세요.

### pypdf
파이썬으로 pdf를 읽어 오기 위함입니다. 그러나, pdf에서도 읽을수 없는 이미지형 텍스트는 불가합니다.
(테스트 해보려면 마우스로 드래그가 가능하면 됩니다.)
### chromadb
오픈소스 벡터 데이터 베이스입니다. 최근에 부상하고 있는 벡터 DB를 오픈소스로 제공합니다. 
참고로 현시점(2023-12-17)에서는 파이썬 3.10이 가장 적합합니다.
3.11에서는 설치가 안되고, 3.9에서는 streamlit과의 호환이 되지 않습니다.
### tiktoken
파이썬에서 사용할 수 있는 자연어 처리 라이브러리. pdf를 읽어오고 토큰화 시켜서 학습하기 위해 사용됩니다.
### langchain
LLM을 기반으로 하는 애플리케이션을 개발하기 위한 프레임워크.
공식문서에서 다양한 기능을 제공하기 때문에 필요하면 이곳에서 여러가지고 참고 하면 됩니다.
공식문서: www.langchain.com

```
pip install pypdf 
pip install chromadb
pip install tiktoken
pip install langchain
pip install langchain langchain-google-genai langchain-community langchainhub langchain-chroma bs4
```
# 라이브러리 로드

# langlab
