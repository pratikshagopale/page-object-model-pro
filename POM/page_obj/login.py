from selenium import webdriver

class login:
    text_user_name="email"
    text_pass_name="pass"
    btn_login="login"
    #initulize webdrivwe
    def __init__(self,driver):
        self.driver=driver

        #set the data for usr name field
    def set_username(self,name):
        self.driver.find_element(By.Name,self.text_user_name).clear()
        self.driver.find_element(By.Name, self.text_user_name).send_keys(name)

        #set password field
    def setpassword(self,password):
        self.driver.find_element(By.Name,self.text_pass_name).clear()
        self.driver.find_element(By.Name,self.text_pass_name).send_keys(password)

    def btn_click(self):
        self.driver.find_element(By.Name,self.btn_login)


