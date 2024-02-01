public class Yought extends ShowRoomWheeler {
    private int length;

    public yought  (String brand,int length ){
        super(brand);
        this.length=length;
    } 

    public void start(){
        System.out.println("Yought  Is  Starting");
    }

    public void stop(){
        System.out.println("Yought  Is  Stopping");
    }

    public void displayInfo(){
        super.displayInfo();
        System.out.println("Type : Yought ");
        System.out.println("Length : "  +numDoors);
    }

}