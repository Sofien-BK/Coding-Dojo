import java.util.ArrayList;
public class TestKiosk {
public static void main(String[] args){

    CoffeeKiosk newKiosk = new CoffeeKiosk ();
    newKiosk.addMenuItem("banana",2);
    newKiosk.addMenuItem("coffee",1.5);
    newKiosk.displayMenu();
    newKiosk.newOrder();


    }
} 