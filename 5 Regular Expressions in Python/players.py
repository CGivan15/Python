import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
    (?P<last_name>[\w ]*)  # Last name
    ,\s
    (?P<first_name>[\w ]*)   # First name
    :\s
    (?P<score>[\d]*)   # scores
''', string, re.X|re.M)

class Player:
  def __init__(self, last_name, first_name, score):
    self.last_name = last_name
    self.first_name = first_name
    self.score = score

print(players.groupdict())

