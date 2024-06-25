from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

WEB_CHECK_SUCCESS = 0

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
bool = True
driver.get('http://127.0.0.1:8777')
score=driver.find_element(By.ID, "score")
print(score.text)
"""
This func will test the score that is saved in txt file from the web page
"""
def test_scores_service():
    bool = True
    driver.get('http://127.0.0.1:5000')
    score=driver.find_element(By.ID, "score")
    if score < 0 or score > 1000:
        bool=False
    return bool

"""
This func will get output of the web check and generate OS exit or declere a success
"""
def main():
    res=test_scores_service()
    if res == False:
        os.exit(-1)
    else:
        return WEB_CHECK_SUCCESS

if __name__ == "__main__":
    main()
