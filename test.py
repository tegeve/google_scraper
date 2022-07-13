i = 0
# link4 = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/span[2]/span[2]/span[1]'
# lista = list(link4)
# lista[77] = f'{i}'
# link4 = "".join(lista)
# print(4)
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.google.com/maps/place/Napoca+15/@46.7711622,23.5773069,'
            '15z/data=!4m9!1m2!2m1!1srestaurant+Cluj-Napoca!3m5!1s0x47490e82bb2c96d7:0x65464b8eaa159f8d!8m2!3d46'
            '.7678612!4d23.5881427'
            '!15sChZyZXN0YXVyYW50IENsdWotTmFwb2NhWhgiFnJlc3RhdXJhbnQgY2x1aiBuYXBvY2GSAQpyZXN0YXVyYW50mgEjQ2haRFNVaE5NRzluUzBWSlEwRm5TVU00Y1dSRFlrMTNFQUU')
telefon = browser.find_element(by=By.CSS_SELECTOR, value='jstcache="468"').text
print(telefon)
