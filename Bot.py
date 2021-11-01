from time import sleep
from selenium import webdriver



class InstaBot:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\'username\']")\
            .send_keys(user_id)
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\'password\']  ")\
            .send_keys(password)
        sleep(2)
        self.driver.find_element_by_xpath("//button[@type=\'submit\']").click()
        sleep(10)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(2)
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href='/{}')]".format(self.user_id)).click()



my_bot = InstaBot(user_id='subodh_band',password='Subodh@123')
my_bot.get_unfollowers()
