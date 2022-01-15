# Wordle first two guesses

wordle.py generates the first two guesses for wordle based on Wordle's word list

The algorithm used to score words is:
* score all letters based on the number of likely words they appear in
* score all eligible words based on the sum of the scores of the *distinct* letters in the words
* choose the best

Likely words exclude words ending in a single 's' - plurals and third person singular verb forms,
as these don't seem to come up in answers - however, they can still be useful as guesses.

For each combination of letters in the best word, we then choose the next words based on the
scores of words containing that combination of letters but none of the other letters from the word
(e.g. if the best word was alert, and we had an 'a', we'd find the next best word without 'l', 'e', r' or 't')

The usefulness of the results probably diminish once you have three or more letters, but the results
remain for completion

# Results

First line has the best guesses, second line is if no letters match, and the other lines are what are the suggested
choices if letters match (which is best may depend on where the matches occur):

```
realo
: dints, tinds
r: snirt, trins
e: inset, neist, nites, senti, sient, stein, teins, tines
a: antis, natis, saint, satin, stain, tains, tians, tinas
l: lints
o: oints
r,e: inert, inter, niter, nitre, trine
r,a: intra, riant, train
r,l: tirls
r,o: intro, nitro
e,a: entia, tenia, tinea
e,l: elint, enlit, inlet, intel, lenti
e,o: toise
a,l: alist, litas, tails
a,o: iotas, ostia, stoai
l,o: toils
r,e,a: irate, retia, terai
r,e,l: liter, litre, relit, tiler
r,e,o: irone
r,a,l: liart, trail, trial
r,a,o: ariot, ratio
r,l,o: lirot, triol
e,a,l: telia
e,a,o: atone, oaten
e,l,o: teloi, toile
a,l,o: aloin
r,e,a,l: ariel, raile
r,e,a,o: oater, orate, roate
r,e,l,o: oiler, oriel, reoil
r,a,l,o: ariot, ratio
e,a,l,o: alone, anole
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

The count of words that a letter appears in on likely Wordle words looks like:

```
e: 4274
a: 3865
r: 2969
o: 2805
i: 2633
l: 2257
t: 2243
n: 2084
s: 2013
d: 1762
y: 1761
u: 1722
c: 1471
p: 1344
m: 1320
h: 1317
g: 1136
b: 1087
k: 900
w: 709
f: 657
v: 513
z: 309
x: 216
j: 188
q: 90
```

(this is reproducible using `python scores.py words`)

Note that scoring based on the number of times a letter appears rather than the number of words it
appears in seems to have almost no impact on the order of the scores or the suggestions made.

Again we now ignore words ending in a single 's' in these scores.
