import re

with open ('text.txt', encoding='utf8') as text_string:
    text = text_string.read().lower()
frequency = {}
match_retries = re.findall(r'\w+', text)

for word in match_retries:
    count = frequency.get(word,0)
    frequency[word] = count + 1

for word, count in frequency.items():
    print(word, count) 

