public class  WheelerRoom implements Wheeler {
    public static void  main(String[]args){
        Car car = new  Car("Lamborghini",2);
        Yought  yought = new Yought ("Yamaha",100); 
    

    System.out.println("Car Info ");
    car.displayInfo();
    car.start();
    car.stop();

    System.out.println("Yought Info ");
    yought.displayInfo();
    yought.start();
    yought.stop();
}
} 