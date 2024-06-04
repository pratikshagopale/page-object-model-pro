from POM.test_data import Test_Data
from POM.setup import driver_setup
from POM.page_obj.login import login
from.selenium import webdriver
class Test_001_login:
    email=Test_Data.email
    password=Test_Data.password
    url=Test_Data.url

    def test_001_login_case(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        self.ln= login(self.driver)
        self.ln= set_username(self.email)
        self.ln



