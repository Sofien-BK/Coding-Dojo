import java.util.ArrayList;
public class TestOrders {
    public static void main(String[] args){

        Item item1 = new Item();
            item1.name  = "mocha";
            item1.price = 5.55;
        Item item2 = new Item();
            item2.name  = "latte";
            item2.price = 7.75;
        Item item3 = new Item();
            item3.name  = "drip coffee";
            item3.price = 8.3;
        Item item4 = new Item();
            item4.name  = "cappuccino";
            item4.price = 7.1;

        Order order1 = new Order();
            order1.name = "Cindhuri";
            order1.ready = true;
        Order order2 = new Order();
            order2.name = "Jimmy";
            order2.items =new ArrayList<>();
            order2.items.add(item1);
            order1.ready = true;
        Order order3 = new Order();
            order3.name = "Noah";
            order3.items =new ArrayList<>();
            order3.items.add(item4);
        Order order4 = new Order();
            order4.name = "Sam";
            order4.items =new ArrayList<>();
            order4.items.add(item2);
            order4.items.add(item2);
            order4.items.add(item2);
        

        System.out.println(order2.items);


        //*** if we Print order1.total it will return the initial value of the double total which is 0.0 */





    }
} 