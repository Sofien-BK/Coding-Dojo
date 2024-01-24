import java.util.ArrayList;
import java.util.Arrays;

public class TestCafe {
    public static void main(String[] args){
        CafeUtil cafeTools = new CafeUtil();

        Integer testGetStreakGoal = cafeTools.getStreakGoal(10);
        double  testGetOrderTotal = cafeTools.getOrderTotal(new double[] {1.5,7.75,10,8.36,4.21,1.98});
        
        ArrayList<String> menuItems = new ArrayList <>();
        menuItems.add("latte");
        menuItems.add("drip coffee");
        cafeTools.displayMenu(menuItems);

        ArrayList<String> customers = new ArrayList <>();
        customers.add("Noah");
        customers.add("Jimmy");
        customers.add("Amy");
        customers.add("Lucas");
        String testAddCustomer = cafeTools.addCustomer(customers);     
    } 
}  