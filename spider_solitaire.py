from card import *

class Game:
  def __init__(self, name):
    self.name = name
    self.cards = set()
    self.create_decks()

  def create_decks(self):
    for _ in range(8):
      for c in Deck().cards:
        self.cards.add(c)

  def __repr__(self):
    s = "Cards in deck: "
    for c in self.cards:
      s += str(c)
    return s


def play_game():
  name = input("Please enter your name: ")
  game = Game(name)
  print("Rules: Cards can only be put in slots that are either\n\
    empty or contains a card of higher value\n\
    The goal of the game is to create complete decks in\n\
    descending order or cards")
  
