public class Car extends ShowRoomWheeler implements Wheeler  {
    private int  numDoors;

    public  Car(String brand,int  numDoors ){
        super(brand);
        this.numDoors = numDoors;  
    }

    public void start(){
        System.out.println("Car  Is  Starting");
    }

    public void stop(){
        System.out.println("Car  Is  Stopping");
    }

    public void displayInfo(){
        super.displayInfo();
        System.out.println("Type : Car ");
        System.out.println("Number of Doors : "  +numDoors);
    }


}  