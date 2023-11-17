var arr2 = [1,5,4,7]

function seperat (arr , separetor){
    for (var i = 0; i<= arr.length-1; i++){
        var expected = "";
        var separetor = ", "
        expected += (arr[i] + separetor) ;
    }
    return expected;
}
var x = seperat(arr2);
console.log(x);