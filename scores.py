#!/usr/bin/env python

from wordle import score_chars, read_words
import sys


def main(args):
    chars = [chr(c) for c in range(ord('a'), ord('z')+1)]
    words = read_words(args[0])
    char_scores = score_chars(chars, words)
    best = sorted(char_scores.items(), key=lambda x: x[1], reverse=True)
    for item in best:
        print(f'{item[0]}: {item[1]}')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

