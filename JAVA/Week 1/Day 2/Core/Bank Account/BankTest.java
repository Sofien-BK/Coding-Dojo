public class BankTest {
    public static void main(String[]args){


        BankAccount account1 = new BankAccount();
        BankAccount account2 = new BankAccount();
        BankAccount account3 = new BankAccount(); 

        account1.deposit(748.5);
        account2.deposit(540);
        account3.deposit(770);

        account1.withdraw(504.5);
        account2.withdraw(360);
        account3.withdraw(222);

        account1.getBalance(account1); 
        account1.getBalance(account2);
        account1.getBalance(account3);
        BankAccount.total();
        BankAccount.accountsCount();

    }
} 