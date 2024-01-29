public class BankAccount {
    //MEMBER VARIABLES
    private double checkingBalance;
    private double savingBalance;

    private static int accounts;
    private static double totalMoney;

    public BankAccount (){
        this.checkingBalance = 0.0;
        this.savingBalance = 0.0;
        accounts++;
    } 
    //METHODS
    public double deposit(double depositedMoney){
        checkingBalance += depositedMoney;
        savingBalance += depositedMoney;
        totalMoney += depositedMoney;
        System.out.println(savingBalance);
        return savingBalance;
    }
    public double withdraw(double withdrawnMoney){
        if (checkingBalance < withdrawnMoney && savingBalance < withdrawnMoney) {
            System.out.println("insufficient funds");
            
        }else {
            checkingBalance -= withdrawnMoney;
        savingBalance -= withdrawnMoney;
        totalMoney -= withdrawnMoney;
        }
        System.out.println(savingBalance);
        return savingBalance;   
    }
    public void getBalance(BankAccount account) {
        System.out.println(account.getCheckingBalance());
    }

    public static double accountsCount(){
        System.out.println(accounts);
        return accounts;
    }
    public static double total(){
        System.out.println(totalMoney);
        return totalMoney;
    }
    //GETTERS
    public double getCheckingBalance() {
        return checkingBalance;
    }
    public double getSavingBalance() {
        return savingBalance;
    }    
} 