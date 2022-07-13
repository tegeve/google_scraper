from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class GoogleMapScraper:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.business_list = []
        self.business_info = {"name": "NA", "rating": "NA", "reviews_count": "NA", "address": "NA", "contact": "NA",
                              "website": "NA"}

    def get_business_info(self, url):
        self.driver.get(url)
        # Parse data out of the page
        self.business_info["name"] = self.driver.find_element(by=By.CLASS_NAME, value='w6VYqd').text.split('\n')[0]
        self.business_info["rating"] = self.driver.find_element(by=By.CLASS_NAME, value='w6VYqd').text.split('\n')[1]
        self.business_info["reviews_count"] = self.driver.find_element(by=By.CLASS_NAME, value='w6VYqd').text.split('\n'
                                                                                                                    )[2]
        self.business_info["address"] = self.driver.find_element(by=By.CLASS_NAME, value='w6VYqd').text.split('\n')[18]
        self.business_info["contact"] = self.driver.find_element(by=By.XPATH, value='//*[@id="QA0Szd"]/div/div/div['
                                                                                    '1]/div[2]/div/div['
                                                                                    '1]/div/div/div[13]/div['
                                                                                    '7]/button/div[1]/div[2]/div['
                                                                                    '1]').text.split('\n')[0]
        self.business_info["website"] = self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[9]/div['
                                                                                    '9]/div/div/div[1]/div['
                                                                                    '2]/div/div[1]/div/div/div['
                                                                                    '13]/div[6]/a/div[1]/div[2]/div['
                                                                                    '1]').text.split('\n')[0]
        self.business_list.append(self.business_info)


urls = ["https://www.google.com/maps/place/Casa+Vikingilor/@46.7699701,23.5582582,"
        "17z/data=!4m5!3m4!1s0x47490ef4a5e651df:0x9f4d2fc3ecbad2f6!8m2!3d46.7698255!4d23.5580382", ]
BusinessScraper = GoogleMapScraper()
for url in urls:
    BusinessScraper.get_business_info(url)
print(BusinessScraper.business_info)
