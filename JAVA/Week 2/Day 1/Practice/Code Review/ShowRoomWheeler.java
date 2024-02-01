abstract public class ShowRoomWheeler implements Wheeler {

    private String brand;


    public showRoomWheeler (String brand){
        this.brand=brand;
    }  

    public void  displayInfo(){
        System.out.println("Brand :"  + brand);
    }



}  