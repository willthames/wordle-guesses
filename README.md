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


# Character scores

This is a an interesting aside prompted by a [friend's tweet that the most
common letters are `ETAINOSHRDLU`](https://twitter.com/nefarioustim/status/1478537147363643392)
- this is true across all English words,
but not for 5 letter words - whether Wordle words or otherwise.

The count of words that a letter appears in on valid Wordle words looks like:

```
s: 5936
e: 5705
a: 5330
o: 3911
r: 3909
i: 3589
l: 3114
t: 3033
n: 2787
u: 2436
d: 2298
y: 2031
c: 1920
p: 1885
m: 1868
h: 1708
g: 1543
b: 1519
k: 1444
w: 1028
f: 990
v: 674
z: 391
j: 289
x: 287
q: 111
```

(this is reproducible using `python scores.py words`)

Note that scoring based on the number of times a letter appears rather than the number of words it
appears in seems to have almost no impact on the order of the scores or the suggestions made.
