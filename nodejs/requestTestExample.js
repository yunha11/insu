var request = require('request');
var parseString = require('xml2js').parseString;

request('http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=109', function (error, response, body) {
    // console.log('error:', error); // Print the error if one occurred
    // console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
    // console.log('body:', body); // Print the HTML for the Google homepage.
    parseString(body, function (err, result) {
        // console.dir(result.rss.channel[0].title);
        // console.dir(result.rss.channel[0].link);
        // console.dir(result.rss.channel[0]);
        console.dir(result.rss.channel[0].item[0].description[0].header[0].title);
        console.dir(result.rss.channel[0].item[0].description[0].header[0].wf);
        console.dir(result.rss.channel[0].item[0].description[0].body[0].location[0].city);
    });
});

