define(function(require, exports, module) {
"use strict";

var oop = require("../lib/oop");
var TextHighlightRules = require("./text_highlight_rules").TextHighlightRules;

var SynthHighlightRules = function() {

    // regexp must not have capturing parentheses. Use (?:) instead.
    // regexps are ordered -> the first match is used
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
            /*{
                token: ["entity.name.function", "markup.heading", "entity.name.function"], // String, Array, or Function: the CSS token to apply
                regex: /(\{.*?\})(.*)(\{\/.*?\})/, // String or RegExp: the regexp to match
            },*/
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
