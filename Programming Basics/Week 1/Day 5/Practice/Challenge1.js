//  a function that returns an array with all the numbers from 1 to 255 
function get_array(){
    var arr= [];
    for (var i=1; i<=255;i++){
        arr.push(i);
    }
    console.log(arr);
    return arr;
}
get_array();