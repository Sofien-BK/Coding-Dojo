// #1
  var arr1 = [8, 6, 7, 5, 3, 0, 9];
   for (var i= 0; i<=arr1.length-1;i++){
     console.log(arr1[i]);
 }
// #2
 var arr2 = [4, 7, 13, 13, 19, 37, -2];
 for(var i=0 ; i<=arr2.length-1; i++){
     console.log(arr2[i]+i);
 }
 // #3
var arr3 = [6, 2, 12, 14, -24, 5, 0];
for (i=0; i<=arr3.length-1; i++){
    if(arr3[i]>5){
        console.log(arr3[i]);
    } else {                     // -------> NO Dice Part 
        arr3[i] = "No dice";
    }
} 



