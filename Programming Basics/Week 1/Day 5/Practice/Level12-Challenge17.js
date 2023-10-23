function abc(arr){
    for (var i=0;i<arr.length;i++){
        if(arr[i]<0){
            arr[i]="dojo";
        }
    }
    return arr;
}
output=abc([-3,0,3,-5]);
console.log(output); //--> [dojo,0,3,dojo]