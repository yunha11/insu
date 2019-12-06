var parseString = require('xml2js').parseString;
var xml = "<root>Hello xml2js!</root>"
console.log(xml)
parseString(xml, function (err, result) {
    console.dir(result);
});