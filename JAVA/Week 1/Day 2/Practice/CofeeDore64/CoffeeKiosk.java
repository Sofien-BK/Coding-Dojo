import java.util.ArrayList;
public class CoffeeKiosk {

    //MEMBER VARIABLE
    private ArrayList<Item> menu;
    private ArrayList<Order> orders;

    //METHODS
    public CoffeeKiosk (){
        this.menu = new ArrayList<Item>();
        this.orders = new ArrayList<Order>();
    } 

    public void addMenuItem (String name , double price){
        Item newItem = new Item();
        newItem.setName(name);
        newItem.setPrice(price);
        menu.add(newItem); 
        newItem.setIndex(menu.size() - 1);
    }

    public void displayMenu (){
        for(Item items : menu){
            System.out.println(String.format("%s  %s  --  $ %s" , items.getIndex(), items.getName() , items.getPrice()));
        }
    }

    public void newOrder (){
        Order newOrder = new Order();
        System.out.println("Please enter customer name for new order:");
        String name = System.console().readLine();
        newOrder.setName(name);
        newOrder.setItems(new ArrayList<Item>());
        displayMenu();
        System.out.println("Please enter a menu item index or q to quit:");
        String itemNumber = System.console().readLine();
        while(!itemNumber.equals("q")){
            int itmNumber = Integer.parseInt(itemNumber);
            newOrder.getItems().add(menu.get(itmNumber));
            System.out.println("Please enter a menu item index or q to quit:");
            itemNumber = System.console().readLine();
            
        }
        double total = 0.0;
    for (Item itm : newOrder.getItems()) {
        total += itm.getPrice();
    }
    newOrder.setTotal(total);
        System.out.println(newOrder.getName());
        for (Item itm : newOrder.getItems()){
        System.out.println(String.format("%s  %s  --  $ %s" , itm.getIndex(), itm.getName() , itm.getPrice()));
        
        }
        System.out.println("Total : " + total);
    }

}