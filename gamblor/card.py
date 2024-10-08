# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_card.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ../nbs/00_card.ipynb 3
from fastcore.test import *
from fastcore.utils import *

# %% ../nbs/00_card.ipynb 5
suits = ["♣", "♦", "♥", "♠"]
ranks = [None, "A"] + [str(x) for x in range(2, 11)] + ["J", "Q", "K"]

# %% ../nbs/00_card.ipynb 14
class Card:
    "A playing card."
    def __init__(
            self,
            suit: int,  # An index into `suits`
            rank: int,  # An index into `ranks`
    ):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{ranks[self.rank]}{suits[self.suit]}"
    def __repr__(self):
        return f"Card({self.suit}, {self.rank})"

# %% ../nbs/00_card.ipynb 19
@patch
def __eq__(self: Card, other: Card):
    return (self.suit, self.rank) == (other.suit, other.rank)

# %% ../nbs/00_card.ipynb 21
@patch
def __lt__(self: Card, other: Card):
    return (self.suit, self.rank) < (other.suit, other.rank)

# %% ../nbs/00_card.ipynb 23
@patch
def __gt__(self: Card, other: Card):
    return (self.suit, self.rank) > (other.suit, other.rank)
