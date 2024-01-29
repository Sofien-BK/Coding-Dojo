import java.util.ArrayList;
public class Order {
//* MEMBER VARIABLES
    private String name;
    private boolean ready;
    private ArrayList<Item>items;


    
    public Order(){
        this.name = "Guest";
        this.ready = false;
        this.items = new ArrayList<>(); 
   }

   public Order(String name){
        this.name = name;
        this.ready = false;
        this.items = new ArrayList<>(); 
   }


//* ORDER METHODS
public void addItem (Item item){
    items.add(item);
   } 

public String getStatusMessage (){
    if(ready == false){
        System.out.println("Thank you for waiting. Your order will be ready soon");
        return "Thank you for waiting. Your order will be ready soon.";
         
    }else{
        System.out.println("Your order is ready.");
        return "Your order is ready.";
        
    }
}    

public double getOrderTotal (Order order) {
    double total = 0;
    for (Item item : order.getItems()) {
        total += item.getPrice();
    }
    System.out.println(total);
    return total;
}  

public void display (Order order){
    System.out.println("Customer Name: " + order.getName());
    for (Item item : order.getItems()) {
        System.out.println(item.getName() + " - $" +item.getPrice());
    }
    System.out.println(order.getOrderTotal(order));
}  







//* GETTERS & SETTERS

    public String getName() {
        return name; 
    }
    public void setName(String name){
        this.name =  name;
    }

    public boolean getReady() {
        return ready; 
    }
    public void setReady(boolean ready){
        this.ready =  ready;
    }

    public ArrayList<Item> getItems() {
        return items; 
    }
    public void setItems(ArrayList<Item> items){
        this.items =  items;
    }

}