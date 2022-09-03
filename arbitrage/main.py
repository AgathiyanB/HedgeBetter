from arbitrage.classes.bet import Bet
from arbitrage.classes.bookie import Bookie
from arbitrage.classes.event import Event
from arbitrage.classes.fixture import Fixture

fixture = Fixture("Southampton", "Chelsea", Event)

bets = [
    Bet(9, 2, Event.HOME, Bookie.LADBROKES),
    Bet(3, 1, Event.DRAW, Bookie.LADBROKES),
    Bet(4, 7, Event.AWAY, Bookie.LADBROKES),
    Bet(5, 1, Event.HOME, Bookie.BETFRED),
    Bet(10, 3, Event.DRAW, Bookie.BETFRED),
    Bet(3, 5, Event.AWAY, Bookie.BETFRED),
    Bet(17, 4, Event.HOME, Bookie.BETWAY),
    Bet(16, 5, Event.DRAW, Bookie.BETWAY),
    Bet(3, 5, Event.AWAY, Bookie.BETWAY),
    Bet(23, 5, Event.HOME, Bookie.UNIBET),
    Bet(16, 5, Event.DRAW, Bookie.UNIBET),
    Bet(3, 5, Event.AWAY, Bookie.UNIBET),
]

fixture.bets = bets

print(*[(betslip, betslip.expected_payout) for betslip in fixture.covering_bets], sep="\n")
print(fixture.optimal_covering_bet, fixture.optimal_covering_bet.expected_payout)

fixture = Fixture("Barnet", "Eastleigh", Event)

bets = [
    Bet(21, 10, Event.HOME, Bookie.PADDYPOWER),
    Bet(15, 8, Event.DRAW, Bookie.PADDYPOWER),
    Bet(6, 5, Event.AWAY, Bookie.PADDYPOWER),
    Bet(21, 10, Event.HOME, Bookie.WILLIAMHILL),
    Bet(21, 10, Event.DRAW, Bookie.WILLIAMHILL),
    Bet(6, 5, Event.AWAY, Bookie.WILLIAMHILL),
    Bet(2, 1, Event.HOME, Bookie.BETWAY),
    Bet(21, 10, Event.DRAW, Bookie.BETWAY),
    Bet(5, 4, Event.AWAY, Bookie.BETWAY),
    Bet(9, 4, Event.HOME, Bookie.BETFAIR),
    Bet(15, 8, Event.DRAW, Bookie.BETFAIR),
    Bet(13, 10, Event.AWAY, Bookie.BETFAIR),
    Bet(11, 5, Event.HOME, Bookie.UNIBET),
    Bet(39, 20, Event.DRAW, Bookie.UNIBET),
    Bet(5, 4, Event.AWAY, Bookie.UNIBET),
    Bet(9, 4, Event.HOME, Bookie.LADBROKES),
    Bet(2, 1, Event.DRAW, Bookie.LADBROKES),
    Bet(5, 4, Event.AWAY, Bookie.LADBROKES),
    Bet(9, 4, Event.HOME, Bookie.BETFRED),
    Bet(2, 1, Event.DRAW, Bookie.BETFRED),
    Bet(5, 4, Event.AWAY, Bookie.BETFRED),
]

fixture.bets = bets

print(*[(betslip, betslip.expected_payout) for betslip in fixture.covering_bets], sep="\n")
print(fixture.optimal_covering_bet, fixture.optimal_covering_bet.expected_payout)