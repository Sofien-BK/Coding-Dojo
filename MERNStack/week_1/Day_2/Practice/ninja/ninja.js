class Ninja {
    constructor(name){
        this.name = name;
        this.health = 90;
        this.speed = 3;
        this.strength = 3;
    }
    sayName(){
        console.log(`Ninja's name is ${this.name}`);
    }
    showStats(){
        console.log(`
        Name : ${this.name}
        Strength : ${this.strength}
        Speed : ${this.speed}
        Health : ${this.health}
        `);
    }
    drinkSake(){
        this.health += 10;
    }
}