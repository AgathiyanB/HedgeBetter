import itertools
from enum import Enum
from operator import attrgetter

from arbitrage.classes.bet import Bet
from arbitrage.classes.betslip import Betslip


class Fixture:
    def __init__(self, home: str, away: str, enum: type[Enum], bets: list[Bet] = None):
        self.home = home
        self.away = away
        self.bets = bets or []
        self.enum = enum

    @property
    def event_bets(self) -> dict[Enum, list[Bet]]:
        event_bets = {}
        for event in self.enum:
            event_bets[event] = []
        for bet in self.bets:
            event_bets[bet.event].append(bet)
        return event_bets

    @property
    def covering_bets(self) -> list[Betslip]:
        arg_list = []
        event_bets = self.event_bets
        for event in self.enum:
            arg_list.append(event_bets[event])
        return [Betslip(combination) for combination in itertools.product(*arg_list)]

    @property
    def optimal_covering_bet(self) -> Betslip:
        bets = []
        event_bets = self.event_bets
        for event in self.enum:
            bets.append(max(event_bets[event], key=attrgetter("payout")))
        return Betslip(bets)
