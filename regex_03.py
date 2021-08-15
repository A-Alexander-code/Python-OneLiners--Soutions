# Dependencies
import re

# Data
page = """
<!DOCTYPE html>
<html>
<body>

<h1>My Programming Links</h1>
<a href="https://app.finxter.com/">test ypur Python skills</a>
<a href="https://blog.finxter.com/recursion/">Learn recursion</a>
<a href="https://nostarch.com/"Great books from NoStarchPress<a/>
<a href="http://finxter.com/">Solve more Python puzzles</a>

</body>
</html>
"""

## Onel-liner
practice_test = re.findall("(<a.*?finxter.*?(test|puzzle).*?>)",page)

# Result
print(practice_test)