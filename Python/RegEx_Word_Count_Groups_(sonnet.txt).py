"""
Word Count Text Analysis
Open, sort, count, group, and print top words in a text document  
by Rick Gosalvez 022120
"""

from collections import Counter
import re

def process_words_from_file(filename, word_len):
    """
        Arguments:
            filename - str
            word_len - int
        Returns:
            word_counts - dict: word (str) -> count (int)
        Read file and create dictionary of word -> count
    """
    regex = f"\\b[a-z]{ {word_len} }\\b"

    word_counts = Counter()
    with open(filename) as f:
        for line in f:
            words = re.findall(regex, line.lower())
            word_counts.update(words)

    return word_counts

########################

filename = 'sonnet.txt'

word_len = int(input("Enter length of words to count: "))
top_count = int(input("Enter # terms to print: "))

word_counts = process_words_from_file(filename, word_len)
for k, v in word_counts.most_common(top_count):
    print(k,v)