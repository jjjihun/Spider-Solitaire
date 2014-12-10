# create a class for an individual Card
class Card:
  def __init__(self, num):
    if num > 13 or num < 1:
      while num < 0 or num > 13:
        num = eval(input("Please enter a valid card value (1-13): "))

    self.num = num

  def __repr__(self):
    c = "+--+\n|"
    if self.num < 10:
      c += " " + str(self.num)
    else:
      c += str(self.num)
    c += "|\n+--+\n"
    return c

# create a class for a deck
class Deck:
  def __init__(self):
    self.cards = set()
    for n in range(1, 14):
      self.cards.add(Card(n))

  def __repr__(self):
    s = "Cards in deck: \n"
    for c in self.cards:
      s += str(c)
    return s