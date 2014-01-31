# example.py
#
# Ustala słowa najczęściej występujące na liście

words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# Zwraca [('eyes', 8), ('the', 5), ('look', 4)]

# Przykład pokazujący, jak dołączyć dodatkowe słowa

morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)
print(word_counts.most_common(3))



