function swap(arr){
    var Y = arr[0];
    arr [0] = arr[arr.length -1];
    arr [arr.length - 1] = Y;
    return arr; 
}