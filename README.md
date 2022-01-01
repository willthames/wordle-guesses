# Wordle first two guesses

wordle.py generates the first two guesses for wordle based on Wordle's word list

The algorithm used to score words is:
* score all letters based on the number of eligible words they appear in
* score all eligible words based on the sum of the scores of the *distinct* letters in the words
* choose the best

For each combination of letters in the best word, we then choose the next words based on the
scores of words containing that combination of letters but none of the other letters from the word
(e.g. if the best word was alert, and we had an 'a', we'd find the next best word without 'l', 'e', r' or 't')

The usefulness of the results probably diminish once you have three or more letters, but the results
remain for completion

# Results

First line is the best guess, second line is if no letters match, and the other lines are what to choose if letters match
```
aeros
: until
a: tidal
e: elint
r: trild
o: doilt
s: lints
a,e: telia
a,r: trial
a,o: aloin
a,s: tails
e,r: relit
e,o: teloi
e,s: steil
r,o: lirot
r,s: tirls
o,s: toils
a,e,r: ariel
a,e,o: alone
a,e,s: aisle
a,r,o: ratio
a,r,s: lairs
a,o,s: iotas
e,r,o: oriel
e,r,s: liers
e,o,s: solei
r,o,s: roils
a,e,r,o: realo
a,e,r,s: aesir
a,e,o,s: aloes
a,r,o,s: soral
e,r,o,s: osier
```

# Generating the wordlist

This command just extracts all five letter quoted words. This means that it gathers html tags
at times (e.g. "event", "click") but we remove duplicates so it shouldn't matter.

```
curl https://www.powerlanguage.co.uk/wordle/main.db1931a8.js | \
  grep -o '"[a-z][a-z][a-z][a-z][a-z]"' | sort -u | cut -c2-6 > words
```


# Running it

The wordle.py script takes a word list (generated above or included in the source) as first argument
```
./wordle.py words
```
