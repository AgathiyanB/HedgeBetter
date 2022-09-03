from selenium.webdriver.chrome import webdriver


class Scraper:
    def __init__(self, homepage: str):
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir=C:\Users\agath\AppData\Local\Google\Chrome\User Data")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(homepage)

    def shutdown(self):
        self.driver.close()
