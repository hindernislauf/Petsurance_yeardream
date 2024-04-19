from PyPDF2 import PdfReader
from langchain_community.document_loaders import PyPDFLoader
import re
from kss import split_sentences

class Pdf_Proccessor:
    def __init__(self) -> None:
        pass
    
    def pdf_load(self, pdf_path):
        try:
            loader = PyPDFLoader(pdf_path)
            text_list = loader.load_and_split()   #raw text
            text_all = ''
            for text in text_list:
                text_all += re.sub('[·\U000f02b1\U000f02b2\U000f02b3\U000f02b4\U000f02b5\U000f02b6\U000f02b7\U000f02b8\U000f02b9\U000f02b0.]','',text.page_content.replace("\n",""))
            text_list = split_sentences(text_all, backend='punct')

            return text_list
        except:
            return -1

# if __name__ == "__main__":
#     P = Pdf_Proccessor()
#     text = P.pdf_load("")
#     print(text)