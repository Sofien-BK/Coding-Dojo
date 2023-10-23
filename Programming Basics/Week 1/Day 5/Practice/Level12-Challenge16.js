function abc(num){
    var arr=[];
    for (vari=0;i<num;i++){
        if(i%2==0){
        arr.push(i);
        }
    }
    return arr;
}
dojo = abc(5);
console.log(dojo); //--> [0,2,4]