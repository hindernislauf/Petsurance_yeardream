# 아래 코드는 헤드리스 모드로 크롬 브라우저 창을 열지 않고 백그라운드에서 작업을 수행합니다.
# crawler.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import re
import pandas as pd


class Crawler:

    def __init__(self):
        pass

    def set_browserstack(self, os = 'Windows', osVersion = '10',
                        resolution = '1920x1080', sessionName = 'Bstack-[Python] langlab',
                        userName = 'hindernislauf_RaUqDL', accessKey = '9CLc9A2Whb1V2CzEuzxi', debug = 'true'):
        self.options = ChromeOptions()
    
        # BrowserStack에서 사용할 설정 추가
        self.options.set_capability('bstack:options', {
            'os': os,
            'osVersion':osVersion,
            'resolution': resolution,
            'sessionName': sessionName,  # 테스트 이름 지정
            'userName': userName,  # 사용자 이름
            'accessKey': accessKey,  # 액세스 키
            'debug': debug  # 디버그 모드 활성화
        })
        self.driver = webdriver.Remote(
            command_executor='https://hub-cloud.browserstack.com/wd/hub',
            options=self.options
            )
        
    def crawerling(self, user_input):
        response = ""
        df = pd.DataFrame(columns=['보험사','보험구분','보험항목','보험이름','가격'])

        try:
            self.driver.get("https://www.e-insmarket.or.kr/")
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/ul/li[3]/dl/dd[1]/button'))
            )
            search_button.click()

            search_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="query"]'))
            )
            search_input.send_keys(user_input)
            search_input.send_keys(Keys.ENTER)

            results = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="contents"]/div[3]/ul/li'))
            )

            for index, result in enumerate(results, start=1):
                # response += "\n"
                company_response = []
                insurance_type = result.find_element(By.XPATH, './div[1]/a/span[1]').text
                insurance_category = result.find_element(By.XPATH, './div[2]/span[3]').text
                insurance_company = result.find_element(By.XPATH, './div[1]/a/span[2]').text.strip('[]')
                insurance_name = result.find_element(By.XPATH, './div[1]/a/span[3]').text
                price_info_text = result.find_element(By.XPATH, './div[2]/span[1]').text
                price = re.search(r'[\d,]+', price_info_text).group()

                # response += f"보험사: [{insurance_company}]\n"
                # response += f"보험 구분: {insurance_type}\n"
                # response += f"보험 항목: {insurance_category}\n"
                # response += f"보험 이름: {insurance_name}\n"
                # response += f"가격: {price}원\n"


                company_response.append(insurance_company)
                company_response.append(insurance_type)
                company_response.append(insurance_category)
                company_response.append(insurance_name)
                company_response.append(f"{price}원")
                df.loc[len(df)] = company_response
            df.set_index(df['보험사'])


                # response.append(company_response)
                
                # print(f"{index}. {insurance_company}")
                # print(f"보험 구분: {insurance_type}")
                # print(f"보험 항목: {insurance_category}")
                # print(f"보험사: [{insurance_company}]")
                # print(f"보험 이름: {insurance_name}")
                # print(f"가격: {price}원\n")
            return df

        except Exception as e:
            print(f"검색된 자료가 없습니다. 다른 검색어로 검색하시기 바랍니다. : {e}")
        
        finally:
            self.driver.quit()

# # 사용자 입력 받기
# user_query = input("검색어를 입력하세요. : ")
# fetch_insurance_price(user_query)