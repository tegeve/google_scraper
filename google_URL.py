from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from cautare_google import CautareGoogle
from time import sleep


class SearchURL:

    def __init__(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(f'https://www.google.com/maps/')
        list_results = f'{CautareGoogle("restaurante Cluj-Napoca")}'
        for i in range(0, 20):
            get_url = self.browser.find_element(by=By.ID, value='searchboxinput')
            get_url.send_keys(f'{list_results[i]}')
            get_enter = self.browser.find_element(by=By.ID, value='searchbox-searchbutton')
            get_enter.click()
            sleep(5)
            # get_url.rezultat = self.browser.find_element(by=By.XPATH, value=)


var = SearchURL()
print(var)
