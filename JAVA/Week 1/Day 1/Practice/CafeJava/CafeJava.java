public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = " Your total is $";
        
        // Menu variables (add yours below)
        double mochaPrice = 3.5;
        double dripCoffee = 1.75;
        double latte = 2.8;
        int cappuccino = 4;
    
        // Customer name variables (add yours below)
        String customer1 = "Cindhuri";
        String customer2 = "Sam ";
        String customer3 = "Jimmy";
        String customer4 = "Noah";
    
        // Order completions (add yours below)
        boolean isReadyOrder1 = false;
        boolean isReadyOrder2 = true;
        boolean isReadyOrder3 = false;
        boolean isReadyOrder4 = true;
    
        // APP INTERACTION SIMULATION (Add your code for the challenges below)
        // Example:
        System.out.println(generalGreeting + customer1); // Displays "Welcome to Cafe Java, Cindhuri"
    	// ** Your customer interaction print statements will go here ** //
        System.out.println(pendingMessage);

        if (isReadyOrder4 == true){
            System.out.println(generalGreeting + customer4 + readyMessage + displayTotalMessage +  cappuccino);
        } else  {
            System.out.println(generalGreeting + pendingMessage);
        }


        System.out.println(customer2 + displayTotalMessage + (latte*2));
        if (isReadyOrder2 == true){
            System.out.println(readyMessage);
        }else{
            System.out.println(pendingMessage);
        }

        System.out.println(customer3 +  displayTotalMessage + (cappuccino-dripCoffee));
    }

}
