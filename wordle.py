from collections import defaultdict
from itertools import combinations
import sys


def read_words(filename):
    with open(filename) as fp:
        return [word.strip() for word in fp.readlines()
                if len(word.strip()) == 5 and
                word[0] == word[0].lower()]


def score_chars(chars, words):
    scores = defaultdict(int)
    for word in words:
        for char in chars:
            if char in word:
                scores[char] += 1
    return scores


def score_words(words, char_scores):
    scores = defaultdict(int)
    for word in words:
        for char in set(word):
            scores[word] += char_scores[char]
    return scores


def main(args):
    chars = [chr(c) for c in range(ord('a'), ord('z')+1)]
    words = read_words(args[0])
    char_scores = score_chars(chars, words)
    word_scores = score_words(words, char_scores)
    best = max(word_scores, key=word_scores.get)
    print(best)
    for i in range(0, 5):
        for exclusions in combinations(best, i):
            next_chars = set(chars) - (set(best) - set(exclusions))
            char_scores = score_chars(next_chars, words)
            next_choices = score_words(words, char_scores)
            print(",".join(exclusions), ": ", max(next_choices, key=next_choices.get))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
