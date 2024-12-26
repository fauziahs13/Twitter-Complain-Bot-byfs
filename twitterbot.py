from selenium import webdriver

INTERNET_CHECKER_URL = "https://www.speedtest.net/"
class InternetSpeedTwitterBot:
    def __init__(self):
        # self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        # self.driver.get(url=INTERNET_CHECKER_URL)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass