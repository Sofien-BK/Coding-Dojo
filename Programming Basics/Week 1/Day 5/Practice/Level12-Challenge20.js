function abc(number){
    var sum=0;
    for (var i=0; i<=number; i++){
        sum=sum+i;
    }
    console.log(sum);
    return sum+10;
}
output=abc(2)+abc(3);
console.log(output); //--> 3,6,29