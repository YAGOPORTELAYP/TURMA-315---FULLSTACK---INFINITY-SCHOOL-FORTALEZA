#pip install selenium
#pip install pyttsx3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyttsx3

opcoes = Options()
opcoes.add_experimental_option("detach", True)

browser = webdriver.Chrome(options = opcoes)
browser.maximize_window()
browser.get("https://www.contosdeterror.site/")

readmore = browser.find_element(By.XPATH,'//*[@id="Blog1"]/div[1]/article[9]/div/div/div[4]/div[2]/a')

readmore.click()

texto_final = ""

for i in range(5,13):
    paragraph = browser.find_element(By.XPATH,f'//*[@id="post-body-7270502306614685553"]/div[2]/p{i}/span')
    texto_final = texto_final + paragraph.text

narrador = pyttsx3.init()
narrador.setProperty("rate",150)
narrador(paragraph.text)
narrador.runAndWait()