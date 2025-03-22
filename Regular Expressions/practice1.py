import re 

pattern = r"\b\d{2}\b"

text = "I am 20 years old. My friend is 300 years old"

match = re.findall(pattern, text)

print(match)
