function howMuchLeftOverCake (numberOfPieces,numberOfPeople){ //Construct a function using modulo that returns a remainder.
    var numberOfPieces = 0; // Set the number of pieces 
    var numberOfPeople = 0; // set the number of people
    var restOfPieces =0;
    restOfPieces = numberOfPieces % numberOfPeople; 
    if (restOfPieces == 0){
        console.log("No leftovers for you!");
    } else if (restOfPieces > 0 && restOfPieces <=2){
        console.log("You have some leftovers");
    } else if (restOfPieces == 3 || restOfPieces == 4 || restOfPieces == 5){
        console.log("You have leftovers to share");
    }else if (restOfPieces > 5){
        console.log("Hold another party!");
    }

}
// show a specfic message for every situation  
// "No leftovers for you!" if there aren't any leftovers
// "You have some leftovers" if there are 2 pieces of cake or less
// "You have leftovers to share" if there are 3 - 5 pieces of cake left over
// "Hold another party!" if there are more than 5 pieces of cake left over.