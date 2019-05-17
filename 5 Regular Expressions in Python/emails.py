import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r''' #<-- Wrap in multiline quote. Remove leading caret (^)
    (?P<email>[-\w\d.+]+@[-\w\d.]+) 
     ,\s
     (?P<phone>\d{3}-\d{3}-\d{4})''' #<-- Add closing paren. Remove extra backslashes. Remove trailing $
     , string, re.X | re.M) #<-- Add verbose (for multiline quote), and multiline (for muliple lines in string) flags

twitters = re.search(r'''
    (?P<twitter>@[\w]+$)
''', string, re.X|re.M)

print(contacts.groupdict())
print(twitters.groupdict())
