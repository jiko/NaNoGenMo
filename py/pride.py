#!/usr/bin/env python

# see http://hyperstition.abstractdynamics.org/archives/003609.html
from string import ascii_lowercase
from random import choice, getrandbits
import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

gematria = dict(zip((a for a in ascii_lowercase), (i for i in xrange(10, 36))))
gematria.update(dict(((str(i), i) for i in xrange(0, 10))))
gematria[' '] = 0

def numogram(phrase):
    letters = phrase.lower()
    return sum(gematria[l] for l in letters if l.isalnum())

def reeduce(phrase):
    return numogram(phrase) % 9 or 9

with open('corpus/PrideAndPrejudice.txt') as f:
    sentences = tokenizer.tokenize(f.read())

mapping = dict(([i, []] for i in xrange(1, 10)))
for sentence in sentences:
    reduction = reeduce(sentence)
    mapping[reduction].append(sentence)

with open('output/JeerRiddenAcidPup.txt', 'w') as d:
    for sentence in sentences:
        reduction = reeduce(sentence)
        new_line = choice(mapping[reduction])
        d.write(new_line.replace("\r\n"," ") + "\n")
