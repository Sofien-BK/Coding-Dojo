public class Item {

    private String name;
    private double price;
    private int index;



    //GETTERS AND  SETTERS

    public String getName(){
        return name;
    }
    public void setName(String itemName){
        this.name = itemName;
    }  
    public double getPrice(){
        return price;
    }
    public void  setPrice (double itemPrice) {
        this.price = itemPrice;
    }
    public int getIndex(){
        return index;
    }
    public void  setIndex (int itemIndex) {
        this.index = itemIndex;
    }
} 