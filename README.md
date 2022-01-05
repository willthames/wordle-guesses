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

First line has the best guesses, second line is if no letters match, and the other lines are what are the suggested
choices if letters match (which is best may depend on where the matches occur):

```
aeros, arose, soare
: unlit, until
a: dital, tidal
e: elint, enlit, inlet, intel, lenti
r: trild
o: doilt
s: lints
a,e: telia
a,r: liart, trail, trial
a,o: aloin
a,s: alist, litas, tails
e,r: liter, litre, relit, tiler
e,o: teloi, toile
e,s: islet, istle, lites, steil, stile, teils, tiles
r,o: lirot, triol
r,s: tirls
o,s: toils
a,e,r: ariel, raile
a,e,o: alone, anole
a,e,s: aisle
a,r,o: ariot, ratio
a,r,s: arils, lairs, laris, liars, liras, rails, rials
a,o,s: iotas, ostia, stoai
e,r,o: oiler, oriel, reoil
e,r,s: leirs, liers, riels, riles, siler, slier
e,o,s: solei
r,o,s: loirs, loris, roils
a,e,r,o: realo
a,e,r,s: aesir, arise, raise, reais, serai
a,e,o,s: aloes
a,r,o,s: orals, solar, soral
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
