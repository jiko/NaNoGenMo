var fs = require('fs'),
    text = '../corpus/SenseAndSensibility.txt';

var pos = require('pos'),
    lexer = new pos.Lexer(),
    tagger = new pos.Tagger();

var markov = require('markov'),
    m = markov(9);

var _ = require('underscore');


m.seed(fs.createReadStream(text), function () {

    filename = 'taggedSenseAndSensibility.json';
    taggedLines = fs.readFile(filename, 'utf8', function (err, data) {

        if (err) {
          console.log('Error: ' + err);
          return;
        }
         
        data = JSON.parse(data);
        data.forEach(function (taggedSentence) {
            
            var newTaggedMarkov = function () {
              return tagger.tag(
                lexer.lex(
                  m.fill(
                    m.pick())
                  .join(' ')));
            };
            var taggedMarkov = newTaggedMarkov(); 

            var potentialMatches = function (pair) {
                var maybeMatches = _.find(taggedMarkov, function (p) { return (p[1] === pair[1]) });

                taggedMarkov = maybeMatches ?
                              _.without(taggedMarkov, maybeMatches) :
                              newTaggedMarkov();

                return maybeMatches ? maybeMatches[0] :
                                      potentialMatches(pair);
            };

            var newSentence = taggedSentence.map(potentialMatches);
            console.log(newSentence.join(' '));

        });

    });

});

