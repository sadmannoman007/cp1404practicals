"""
CP1404
Count word occurrences in a string
"""

word_to_count = {}
# text = input("Text: ")
text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

max_length = max((len(word) for word in words))

for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")