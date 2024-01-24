import java.util.ArrayList; 
public class CafeUtil {


    public int getStreakGoal(int numWeeks){
        Integer sum = 0;      
        for(int i=0; i<=numWeeks; i++ ){
            sum += i ; 
        }
        System.out.println(sum);
        return sum;  
    }  

    public double getOrderTotal(double[] prices){
        double total = 0;
        for (int i = 0; i< prices.length; i++  ){
            total = total += prices[i]; 
        }
        System.out.println(total);
        return total;
    }  

    public void displayMenu (ArrayList<String> menuItems){
        for (String menuItem : menuItems){
        System.out.println(String.format("%s %s" , menuItems.indexOf(menuItem) , menuItem));
    }
    }

    public String addCustomer (ArrayList<String> customers){
        System.out.println("Please enter your name:");
        String username = System.console().readLine();
        System.out.println(String.format("Hello %s" , username));
        int customersNum = customers.size();
        System.out.println(String.format( "%s %s %s","There are" , customersNum , "people in front of you" ));
        customers.add(username);
        System.out.println(customers);

    return username;
    }
}