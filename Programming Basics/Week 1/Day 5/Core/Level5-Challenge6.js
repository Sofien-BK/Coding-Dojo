var x = [1,3,5,8];
for (i=0; i<x.length; i++){
    if(x[i] >4){
        x[i=0];
    }
}
console.log(x); // --> [1,3,0,0]