from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
from dotenv import load_dotenv
import os
import time

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv("ACCOUNT_EMAIL")
TWITTER_PASSWORD = os.getenv("ACCOUNT_PASSWORD")
# CHROME_DRIVER_PATH = pass
INTERNET_CHECKER_URL = "https://www.speedtest.net/"
TWITTER_SIGNUP_URL = "https://twitter.com/i/flow/signup"
TWITTER_LOGIN_URL = "https://twitter.com/login"
TWITTER_USERNAME = "Naraprojec82671"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.download = 0
        self.upload = 0

    def get_internet_speed(self):
        self.driver.get(url=INTERNET_CHECKER_URL)

        def check_correct():
            try:
                time.sleep(3)
                # Depending on your location, you might need to accept the GDPR pop-up.
                accept_button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
                accept_button.click()
            except NoSuchElementException:
                return False
            else:
                return True

        while not check_correct():
            self.driver = webdriver.Chrome(options=self.chrome_options)
            self.driver.get(url=INTERNET_CHECKER_URL)

        time.sleep(3)
        # go_button = self.driver.find_element(By.CSS_SELECTOR, "a .js-start-test span .start-text")
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        
        time.sleep(60)
        self.download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.download_text = self.download.text
        self.upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.upload_text = self.upload.text

        print(f"download = {self.download_text} Mbps")
        print(f"upload = {self.upload_text} Mbps")

    def tweet_at_provider(self):
        self.driver.get(url=TWITTER_LOGIN_URL)
        time.sleep(30)
        email_bar = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email_bar.click()
        email_bar.send_keys(TWITTER_EMAIL)
        time.sleep(3)
        email_bar.send_keys(Keys.ENTER)
        time.sleep(3)
        username_bar = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username_bar.click()
        username_bar.send_keys(TWITTER_USERNAME)
        username_bar.send_keys(Keys.ENTER)
        time.sleep(3)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.click()
        password_field.send_keys(TWITTER_PASSWORD)
        time.sleep(3)
        password_field.send_keys(Keys.ENTER)

        # try:
        #     time.sleep(20)
        #     term_policy = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/button')
        #     term_policy.click()
        # except NoSuchElementException:
        #     pass
        # else:
        time.sleep(30)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.click()
        # COMPLAIN_TEXT = f"Hey, Internet Provider, why is my internet speed {self.download_text} down/ {self.upload_text} up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        COMPLAIN_TEXT = f"Hey, Internet Provider, why is my internet speed 11 down/ 5 up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet.send_keys(COMPLAIN_TEXT)

        time.sleep(3)
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post_button.click()

        # time.sleep(2)
        # self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

