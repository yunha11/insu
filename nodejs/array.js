var cars = ["bmw","volvo","saab","ford","fiat","audi"];
var txt = ""
var i;

for (i = 0; i<cars.length; i++) {
    txt += cars[i];
    if(cars[i]=='bmw') {
        console.log("!!")
    }
    else {
        console.log('--')
    }
}

console.log(txt);