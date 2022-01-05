#!/usr/bin/env python

from collections import defaultdict
from itertools import combinations
import sys


def maxes(scores):
    top = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    result = [top[0][0]]
    for item in top[1:]:
        if item[1] != top[0][1]:
            break
        result.append(item[0])
    return result


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
    best = maxes(word_scores)
    print(", ".join(best))
    for i in range(0, 5):
        for exclusions in combinations(best[0], i):
            next_chars = set(chars) - (set(best[0]) - set(exclusions))
            char_scores = score_chars(next_chars, words)
            next_choices = score_words(words, char_scores)
            print("{}: {}".format(",".join(exclusions), ", ".join(maxes(next_choices))))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
