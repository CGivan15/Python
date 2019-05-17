import re

string = 'Perotto, Pier Giorgio'

names = re.match(r'''
    ^(?P<last_name>[\w]*),\s                # Last name
    (?P<first_name>[\w\s\w]*)$           # First name
''', string, re.X)

print(names.groupdict())