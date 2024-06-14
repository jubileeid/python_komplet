import re

text = "I have a cat and a dog"
pattern = r"cat"
match = re.search(pattern, text)

if match:
    print(match.group())  # Output: cat
