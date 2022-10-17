from arbitrage.scrapers.scraper import Scraper


class BetfairScraper(Scraper):
    in_play_url = "https://www.betfair.com/sport/inplay"
    fixture_in_play_css_selector = ".ui-inplay.event-information"
    home_team_name = ".home-team-name"
    away_team_name = ".away-team-name"


