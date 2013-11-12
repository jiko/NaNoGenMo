// based on https://gist.github.com/dariusk/7154705

var fs = require('fs');
var text = process.argv[2];

var lbl = require('line-by-line'),
    lr = new lbl('corpus/'+ text + '.txt'),
    lineNum = 0;

var pos = require('pos'),
    lexer = new pos.Lexer(),
    tagger = new pos.Tagger(),
    taggedLines = [];

lr.on('error', function (err) {
    console.log('Error!', err);
});

lr.on('line', function (line) {
    lr.pause();
    console.log(++lineNum);
    var taggedLine = tagger.tag(lexer.lex(line));
    taggedLines.push(taggedLine);
    console.log(JSON.stringify(taggedLine));
    lr.resume();
});

lr.on('end', function () {
    console.log("All lines are read, file is closed now.");
    posFileName = 'tagged' + text + '.json';
    fs.writeFile(posFileName, JSON.stringify(taggedLines), function (err) {
        if (err) throw err;
        console.log('Saved PoS tagged lines to ' + posFileName);
    });
});
