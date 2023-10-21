var x=10;
function abc(x){
    console.log(x);
    return x*10;
}
var z=abc(x)+abc(x);
console.log(z); //--> 10,10,200