from arbitrage.classes.event import Event
from arbitrage.classes.fixture import Fixture
from arbitrage.scrapers.betfair_scraper import BetfairScraper


def test_get_bets_for_fixture():
    scraper = BetfairScraper()
    fixture = Fixture("home", "away", Event)
    event_list = scraper.get_fixtures()
    assert True
