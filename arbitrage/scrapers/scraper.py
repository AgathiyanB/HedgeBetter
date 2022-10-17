from selenium import webdriver
from selenium.webdriver.common.by import By

from arbitrage.classes.event import Event
from arbitrage.classes.fixture import Fixture


class Scraper:
    in_play_url = None
    fixture_in_play_css_selector = None
    home_team_name = None
    away_team_name = None

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.in_play_url)

    def get_fixtures(self):
        fixtures = []
        events = self.driver.find_elements(By.CSS_SELECTOR, self.fixture_in_play_css_selector)[0]
        for event in events:
            home = events.find_element(By.CSS_SELECTOR, self.home_team_name).text
            away = events.find_element(By.CSS_SELECTOR, self.away_team_name).text
            home_bet_text = events.find_element(By.CSS_SELECTOR).text
            draw_bet_text = events.find_element(By.CSS_SELECTOR).text
            away_bet_text = events.find_element(By.CSS_SELECTOR).text
            fixture = Fixture(home, away, Event)
        return fixtures

    def shutdown(self):
        self.driver.close()
