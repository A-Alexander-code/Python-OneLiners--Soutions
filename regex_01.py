# Dependencies
import re

# Data
text1 = "crypto-bot that is trading Bitcoin and other currencies"
text2 = "cryptography encryption methods that can be cracked easily with quentum computers"

# One-liner
pattern = re.compile("crypto(.{1,30})coin")

# Result
print(pattern.match(text1))
print(pattern.match(text2))