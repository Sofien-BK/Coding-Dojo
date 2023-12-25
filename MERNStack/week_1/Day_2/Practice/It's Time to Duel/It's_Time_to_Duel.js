class Card {
    constructor(name,cost){
            this.name=name;
            this.cost=cost;
    }
}
class Unit extends Card {
    constructor(name,cost,power,resilience){
        super(name,cost)
        this.power=power;
        this.resilience=resilience;
    }
    applyEffect (effect){
        if (effect.stat === 'power'){
            this.power += effect.magnitude;
        } else if (effect.stat === 'resilience'){
            this.resilience += effect.magnitude;

    }
}
    attack(defender){
        defender.resilience -= this.power
        console.log(this.power);
        console.log(defender.resilience);
    }
}
class Effect extends Card {
    constructor(name,cost,text,stat,magnitude){
        super(name,cost)
        this.text=text;
        this.stat=stat;
        this.magnitude=magnitude;
    }
}
const redBeltNinja = new Unit ('Red Belt Ninja', 3 , 3 , 4);
const blackBeltNinja = new Unit ('Black Belt Ninja', 4 , 5 , 4);

const hardAlgorithm = new Effect ('Hard Algorithm', 2 ,"increase target's resilience by 3" , "resilience" , +3);
const unhandledPromiseRejection = new Effect ('Unhandled Promise Rejection', 1 , "reduce target's resilience by 2", "resilience" , -2 );
const pairProgramming = new Effect ('Pair Programming', 3 ,"increase target's power by 2" , "power" , +2);

redBeltNinja.applyEffect(unhandledPromiseRejection);
redBeltNinja.applyEffect(pairProgramming);
redBeltNinja.attack(blackBeltNinja);
