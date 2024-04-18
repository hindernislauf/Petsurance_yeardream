from PyPDF2 import PdfReader
from langchain_community.document_loaders import PyPDFLoader

class Pdf_Proccessor:
    def __init__(self) -> None:
        pass
    
    def pdf_load(self, pdf_path):
        try:
            loader = PyPDFLoader(pdf_path)
            text = loader.load_and_split()  #raw text

            return text
        except:
            return -1

if __name__ == "__main__":
    P = Pdf_Proccessor()
    text = P.pdf_load("/home/student/workspace/langlab/pet.pdf")
    print(text)