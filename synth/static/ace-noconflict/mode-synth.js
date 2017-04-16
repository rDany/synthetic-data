ace.define("ace/mode/matching_brace_outdent",["require","exports","module","ace/range"], function(require, exports, module) {
"use strict";

var Range = require("../range").Range;

var MatchingBraceOutdent = function() {};

(function() {

    this.checkOutdent = function(line, input) {
        if (! /^\s+$/.test(line))
            return false;

        return /^\s*\}/.test(input);
    };

    this.autoOutdent = function(doc, row) {
        var line = doc.getLine(row);
        var match = line.match(/^(\s*\})/);

        if (!match) return 0;

        var column = match[1].length;
        var openBracePos = doc.findMatchingBracket({row: row, column: column});

        if (!openBracePos || openBracePos.row == row) return 0;

        var indent = this.$getIndent(doc.getLine(openBracePos.row));
        doc.replace(new Range(row, 0, row, column-1), indent);
    };

    this.$getIndent = function(line) {
        return line.match(/^\s*/)[0];
    };

}).call(MatchingBraceOutdent.prototype);

exports.MatchingBraceOutdent = MatchingBraceOutdent;
});

ace.define("ace/mode/synth_highlight_rules",["require","exports","module","ace/lib/oop","ace/mode/text_highlight_rules"], function(require, exports, module) {
"use strict";

var oop = require("../lib/oop");
var TextHighlightRules = require("./text_highlight_rules").TextHighlightRules;

var SynthHighlightRules = function() {
   this.$rules = {
        "start" : [
            {
                token: "comment", // String, Array, or Function: the CSS token to apply
                regex: /^\s*#.*/, // String or RegExp: the regexp to match
            },
            {
                token: "string", // String, Array, or Function: the CSS token to apply
                regex: /H(\(\d+\))?:/, // String or RegExp: the regexp to match
            },
            {
                token: "variable", // String, Array, or Function: the CSS token to apply
                regex: /R(\(\d+\))?:/, // String or RegExp: the regexp to match
            },
            {
                token: "entity.name.function", // String, Array, or Function: the CSS token to apply
                regex: /\{.*?\}/, // String or RegExp: the regexp to match
            },
        ]
    };
};

oop.inherits(SynthHighlightRules, TextHighlightRules);

exports.SynthHighlightRules = SynthHighlightRules;

});

ace.define("ace/mode/folding/synth",["require","exports","module","ace/lib/oop","ace/range","ace/mode/folding/fold_mode"], function(require, exports, module) {
"use strict";

var oop = require("../../lib/oop");
var Range = require("../../range").Range;
var BaseFoldMode = require("./fold_mode").FoldMode;

var FoldMode = exports.FoldMode = function() {};
oop.inherits(FoldMode, BaseFoldMode);

(function() {
    this.foldingStartMarker = /(\{|\[)[^\}\]]*$|^\s*(\/\*)/;
    this.foldingStopMarker = /^[^\[\{]*(\}|\])|^[\s\*]*(\*\/)/;

    this.getFoldWidgetRange = function(session, foldStyle, row) {
        var line = session.getLine(row);
        var match = line.match(this.foldingStartMarker);
        if (match) {
            var i = match.index;

            if (match[1])
                return this.openingBracketBlock(session, match[1], row, i);

            var range = session.getCommentFoldRange(row, i + match[0].length);
            range.end.column -= 2;
            return range;
        }

    };

}).call(FoldMode.prototype);

});

ace.define("ace/mode/synth",["require","exports","module","ace/lib/oop","ace/mode/text","ace/tokenizer","ace/mode/matching_brace_outdent","ace/mode/synth_highlight_rules","ace/mode/folding/synth"], function(require, exports, module) {
"use strict";

var oop = require("../lib/oop");
var TextMode = require("./text").Mode;
var Tokenizer = require("../tokenizer").Tokenizer;
var MatchingBraceOutdent = require("./matching_brace_outdent").MatchingBraceOutdent;
var MyNewHighlightRules = require("./synth_highlight_rules").SynthHighlightRules;
var MyNewFoldMode = require("./folding/synth").SynthFoldMode;

var Mode = function() {
    this.HighlightRules = MyNewHighlightRules;
    this.$outdent = new MatchingBraceOutdent();
};
oop.inherits(Mode, TextMode);

(function() {
    this.lineCommentStart = "//";
    this.blockComment = {start: "/*", end: "*/"};
    this.getNextLineIndent = function(state, line, tab) {
        var indent = this.$getIndent(line);
        return indent;
    };

    this.checkOutdent = function(state, line, input) {
        return this.$outdent.checkOutdent(line, input);
    };

    this.autoOutdent = function(state, doc, row) {
        this.$outdent.autoOutdent(doc, row);
    };

}).call(Mode.prototype);

exports.Mode = Mode;
});
