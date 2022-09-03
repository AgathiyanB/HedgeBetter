from arbitrage.classes.bookie import Bookie
from arbitrage.classes.event import Event


class Bet:
    def __init__(self, a: int, b: int, event: Event, bookie: Bookie):
        self.a = a
        self.b = b
        self.event = event
        self.bookie = bookie

    @property
    def payout(self) -> float:
        return (self.a+self.b)/self.b

    def __str__(self):
        return f"{self.a}/{self.b} {self.event.name} {self.bookie.name}"

    def __repr__(self):
        return f"{self.a}/{self.b} {self.event.name} {self.bookie.name}"
