# Gen Austen

I got all six of Austen's novels from [Project Gutenberg's Jane Austen collection](http://www.gutenberg.org/ebooks/author/68). I have included the Project Gutenberg license, which says, in short, that you can use their works however you want if you strip their front- and back-matter from the text, but if you give them any credit at all you have to include their full license. So, thanks Project Gutenberg.

## Distraction and Distractability

Hat tip to [Steve Inskeep and NPR](http://www.npr.org/blogs/health/2012/10/09/162401053/a-lively-mind-your-brain-on-jane-austen) for my working title. For this piece, which you can find in the `output` directory, I used the `go-markov` executable, compiled from [markov.go](http://golang.org/doc/codewalk/markov/) on Linux x86-64, with a 3-gram model and _Sense and Sensibility_ for input.

    go-markov -prefix=3 -words=50000 < corpus/SenseAndSensibility.txt > output/DistractionAndDistractability.txt

The _Distractable_ pieces were made with `GenAusten.js`, which badly integrates Part-of-Speech models with Markov generated text. 

### Wordcounts
- 99967 output/DistractionAndDistractables.txt
- 136286 output/DistractionAndDistractable.txt
- 50000 output/DistractionAndDistractibility.txt

## Deference and Destitution

Hat tip to [Kevin Dalton](https://github.com/kmdalton) for the working title. I've used a crazy numerological approach to create some even less readable output. Find the horror in the `py` folder. _Pride and Prejudice_ served as the corpus. I've never read it. Science beats superstition every time, eh Sherlock?

### Wordcount
- 1039281 output/DeferenceAndDestitution.txt

## Inflamed Parks

Next on the list is _Mansfield Park_. Working title courtesy of an anagram generator. Output courtesy of a crude bash script.

### Wordcount
- 50005 output/InflamedParks.txt

## Mena

Using Leonard Richardson's [In-Dialogue](https://github.com/leonardr/In-Dialogue) project, I replaced the dialogue of _Mansfield Park_ with that of _Emma_.  

### Wordcount

- 156717 output/Mena.html 

## Abby

Using the same approach as before, I replaced the dialogue of _Northanger Abbey_ with that of _Emma_.

### Wordcount

- 94474 output/Abby.html

## Nana Grammy

I plugged "Northanger Abbey" into [an anagram generator](http://www.wordsmith.org/anagram/advanced.html) and copy/pasted the results into a file. It's a doozy.

### Wordcount

- 838483 output/Nanagrammy.txt

## Convincing

Ah yes, fan fiction. What the hell. Lots of Austen fanfic out there, so I went with [Archive of Our Own](http://archiveofourown.org/tags/Persuasion%20-%20Jane%20Austen/works?commit=Sort+and+Filter&page=1&utf8=%E2%9C%93&work_search%5Bcomplete%5D=0&work_search%5Blanguage_id%5D=1&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=revised_at), copying and pasting by hand. I compiled a list of links to the works I copied in `corpus/fanfic/sources.txt`. Once again, I have used `go-markov -prefix=3` &c.

### Wordcount

- 50000 output/Convincing.txt

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
