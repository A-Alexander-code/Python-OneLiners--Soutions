import re

text  = """
"One can never have enough socks", said Dumbledore.
"Another Christimas has come and gone and I didn't
get a simple pair. People will insist on giving me books."
Christmas Quote
"""

regex = "Christ"

print(re.match(regex, text))
print(re.search(regex, text))
print(re.findall(regex, text))