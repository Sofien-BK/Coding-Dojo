//? 1:
console.log(hello);                                   
var hello = 'world';                                 
//* var hello
//* console.log(hello); // logs undefined
//* hello = 'world';
//? 2:
var needle;
test();
function test(){
    var needle;
    console.log(needle);
    needle = 'magnet'
}
needle = 'haystack'
//* empty output
//? 3: 
var brendan;
function print(){
    var brendan;
    console.log(brendan);
    brendan = 'only okay'
}
brendan = 'super cool'
console.log(brendan);
//* undifiend / super cool
//? 4:
var food;
console.log(food);
eat();
function eat(){
    var food;
    food = 'half-chicken';
    console.log(food);
    food = 'gone';
}
food = 'chicken'
//* undifiend / half-chiken
//? 5:
var mean;
mean();
console.log(food);
mean = function() {
    var food;
    food = "chicken";
    console.log(food);
    food = "fish";
    console.log(food);
}
console.log(food);
//* undifiend 
//? 6:
var genre; 
console.log(genre);
genre = "disco";
rewind();
function rewind() {
    var genre;
    genre = "rock";
    console.log(genre);
    genre = "r&b";
    console.log(genre);
}
console.log(genre);
//* undifiend / rock / r&b / disco
//? 7:
dojo = "san jose";
console.log(dojo);
learn();
function learn() {
    var dojo;
    dojo = "seattle";
    console.log(dojo);
    dojo = "burbank";
    console.log(dojo);
}
console.log(dojo);
//* undifiend / seattle / burbank / undifiend 
//? 8: 
console.log(makeDojo("Chicago", 65));
console.log(makeDojo("Berkeley", 0));
function makeDojo(name, students){
    const dojo = {};
    dojo.name = name;
    dojo.students = students;
    if(dojo.students > 50){
        dojo.hiring = true;
    }
    else if(dojo.students <= 0){
        dojo = "closed for now";
    }
    return dojo;
}










