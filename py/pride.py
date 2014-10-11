#!/usr/bin/env python

# see http://hyperstition.abstractdynamics.org/archives/003609.html
from string import ascii_lowercase
from random import choice, getrandbits
from cStringIO import StringIO

gematria = dict(zip((a for a in ascii_lowercase), (i for i in xrange(10, 36))))
gematria.update(dict(((str(i), i) for i in xrange(0, 10))))
gematria[' '] = 0

def numogram(phrase):
    letters = phrase.lower()
    return sum(gematria[l] for l in letters if l.isalnum())

def reeduce(phrase):
    return numogram(phrase) % 9 or 9

with open('corpus/PrideAndPrejudice.txt') as f:
    lines = [line.strip() for line in f]

mapping = dict(([i, []] for i in xrange(1, 10)))
for line in lines:
    reduction = reeduce(line)
    mapping[reduction].append(line)

with open('output/CrappedDidIreJune.txt', 'w') as d:
        new_line = choice(mapping[reduction])
        d.write(new_line + "\n") 
