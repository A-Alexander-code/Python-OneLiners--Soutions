is_anagram = lambda x1, x2: sorted(x1) == sorted(x2)

print(is_anagram("elvis", "lives"))
print(is_anagram("elvise", "livees"))
print(is_anagram("elvis", "dead"))

is_palindrome = lambda phrase: phrase == phrase[::-1]

print(is_palindrome("anna"))
print(is_palindrome("kdljfasjf"))
print(is_palindrome("rats live on no evil star"))