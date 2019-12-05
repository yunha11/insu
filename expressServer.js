const express = require('express')
const app = express()

app.use(express.static(__dirname + '/public')); //디자인, 프론트앤드js, 이미지 파일 등 정적파일 저장
app.set('views', __dirname + '/views'); //렌더링할 파일(html, ejs)은 views 폴더에 저장
app.set('view engine', 'ejs');

app.get('/', function (req, res) {
    var greetingMsg = "HI"
    res.send("<html><h1>Hello " + greetingMsg+ " World</h1></html>")
})
 
app.get('/main', function (req, res) {
    res.render('main')
})

app.get('/result', function (req, res) {
    res.send('result')
})

// app.get('/prac', function (req, res) {
//     res.render('ejs')
// })

// app.get('/prac01', function (req, res) {
//     res.render('ejs01')
// })

// app.get('/prac02', function (req, res) {
//     res.render('ejs02')
// })

app.listen(3000)
