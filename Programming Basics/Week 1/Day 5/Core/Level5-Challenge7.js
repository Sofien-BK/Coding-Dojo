var x = [-1,3,2,7];
for (var i=0;i<x.length;i++){
    if (x[i]<i){
        x[i]=-10;
    }
} 
console.log(x); //--> [-10,3,2,7]

