import java.util.ArrayList;

public class Order {

    private String name;
    private double total;
    private boolean ready;
    private ArrayList<Item> items;


    public Order (){
        this.items = new ArrayList <Item>();
    }
     //GETTERS AND  SETTERS

    public String getName(){
        return name;
    }
    public void setName(String orderName){
        this.name = orderName;
    }  
    public double getTotal(){
        return total;
    }
    public void  setTotal (double orderTotal) {
        this.total = orderTotal;
    }
    public boolean getReady(){
        return ready;
    }
    public void setReady(boolean orderReady){
        this.ready = orderReady;
    }  
    public ArrayList<Item> getItems(){
        return items;
    }
    public void  setItems (ArrayList<Item> orderItems) {
        this.items = orderItems;
    }
}
