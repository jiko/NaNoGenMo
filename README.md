# Gen Austen

I got all six of Austen's novels from [Project Gutenberg's Jane Austen collection](http://www.gutenberg.org/ebooks/author/68). I have included the Project Gutenberg license, which says, in short, that you can use their works however you want if you strip their front- and back-matter from the text, but if you give them any credit at all you have to include their full license. So, thanks Project Gutenberg.

## Distraction and Distractability

Hat tip to [Steve Inskeep and NPR](http://www.npr.org/blogs/health/2012/10/09/162401053/a-lively-mind-your-brain-on-jane-austen) for my working title. For this piece, which you can find in the output directory, I used the go-markov executable, compiled from markov.go on Linux x86-64, with a 3-gram model and Sense and Sensibility for input. The Distractable pieces were made with GenAusten.js, which badly integrates Part-of-Speech models with Markov generated text. 

### Wordcounts
- 99967 output/DistractionAndDistractables.txt
- 136286 output/DistractionAndDistractable.txt
- 50000 output/DistractionAndDistractibility.txt

## Deference and Destitution

Hat tip to [Kevin Dalton](https://github.com/kmdalton) for the working title. I've used a crazy numerological approach to create some even less readable output. Find the horror in the py folder. Pride and Prejudice served as the corpus. I've never read it. Science beats superstition every time, eh Sherlock?

### Wordcount
- 1039281 output/DeferenceAndDestitution.txt

## Inflamed Parks

Next on the list is Mansfield Park. Working title courtesy of an anagram generator. Output courtesy of a crude bash script.

### Wordcount
- 50005 output/InflamedParks.txt

## Blerg

---

# NaNoGenMo
National Novel Generation Month - based on [an idea I tweeted on a whim](https://twitter.com/tinysubversions/status/396305662000775168)

## The Goal

Spend the month of November writing code that generates a novel of 50k+ words.

## The Rules

The only rule is that you share at least one novel and also your source code at the end.

The source code does not have to be licensed in a particular way, so long as you share it. The code itself does not need to be on Github, either. I'm just using this repo as a place to organize the community.

The "novel" is defined however you want. It could be 50,000 repetitions of the word "meow". It could literally grab a random novel from Project Gutenberg. It doesn't matter, as long as it's 50k+ words.

_Please try to respect copyright._ I'm not going to police it, as ultimately it's on your head if you want to just copy/paste a Stephen King novel or whatever, but the most useful/interesting implementations are going to be ones that don't engender lawsuits.

This activity ends at 12:01am GMT Dec 1st.

## How to Participate

Open an issue on this repo and declare your intent to participate. You may continually update the issue as you work over the course of the month. Feel free to post dev diaries, sample output, etc.

Also feel free to comment on other participants' issues.

## Resources

There's [an open issue](https://github.com/dariusk/NaNoGenMo/issues/11) where you can add resources (libraries, corpuses, APIs, techniques, etc).

## That's It

So yeah. Have fun with this!
