public class Testing {
    public static void main(String[] args){

        Order orderBot = new Order();

        Order order1 = new Order("capo");
                        order1.addItem(new Item ("latte", 5) );
                        order1.addItem(new Item ("coffee", 7) );
                        order1.addItem(new Item ("latte", 3) );

        double testGetOrderTotal = orderBot.getOrderTotal(order1);

        orderBot.display(order1);

    }
} 