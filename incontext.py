# incontext-learning을 위한 모듈. 기존에 누적된 내용을 학습하는 기능을 담당합니다.
# 부연 설명이 필요할 듯합니다!
# 

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory




def memory(chat):
    conversation = ConversationChain(llm=chat, memory=ConversationBufferMemory())
    conversation.run(enter())