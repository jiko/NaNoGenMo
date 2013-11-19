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

mapping = dict(([i, []] for i in xrange(1, 10)))
with open('corpus/PrideAndPrejudice.txt') as f:
    with open('output/DeferenceAndDestitution.txt', 'a') as d:
        io = StringIO(f.read())
        for line in io:
            new_line = ''
            for word in line.split():
                reduction = reeduce(word)
                if word not in mapping[reduction]:
                    mapping[reduction].append(word)
                new_line += choice(mapping[reduction]) + " "
            d.write(new_line + "\n") 
