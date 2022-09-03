from arbitrage.classes.bet import Bet


class Betslip:
    def __init__(self, bets: list[Bet]):
        self.bets = bets

    def __str__(self):
        return str(self.bets)

    def __repr__(self):
        return repr(self.bets)

    @property
    def optimum_spread(self) -> dict[Bet, float]:
        spread = {}
        normalising_constant = 0
        for bet in self.bets:
            init_bet_amount = 1/bet.payout
            spread[bet] = init_bet_amount
            normalising_constant += init_bet_amount
        for bet in spread:
            spread[bet] /= normalising_constant
        return spread

    @property
    def expected_payout(self) -> float:
        # All bets should return same value
        bet = self.bets[0]
        return self.optimum_spread[bet] * bet.payout
