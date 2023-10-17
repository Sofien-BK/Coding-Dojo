var x = [1,3,5,8,2,-5,-8];
var temp = x[x.length-1];
x[x.length-1]=x[0];
x[0]=temp;
console.log(x); //--> [-8,3,5,8,2,-5,1]