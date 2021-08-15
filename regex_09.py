# Dependencies
import re

# Data
text = 'if you use words to often words become used'

# One-liner
style_problems = re.search('\s(?P<x>[a-z]+)\s+([a-z]+\s+){0,10}(?P=x)\s',''+text)

# Result
print(style_problems)