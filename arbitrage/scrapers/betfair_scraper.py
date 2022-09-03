from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from arbitrage.classes.fixture import Fixture


class BetfairScraper:
    def get_bets_for_fixture(self, driver: WebDriver, fixture: Fixture):
        driver.find_elements(By.XPATH, "//ul[@class='section-list']")

