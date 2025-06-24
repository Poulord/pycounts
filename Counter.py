from collections import Counter

words = ["a", "happy", "hello", "a", "world", "happy"]
word_counts = Counter(words)
print (word_counts)
# Output: Counter({'a': 2, 'happy': 2, 'hello': 1, 'world': 1})
