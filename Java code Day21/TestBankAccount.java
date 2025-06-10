import java.util.*;
public class TestBankAccount {
    public static void main(String[] args) {
        BankAccount b=new BankAccount();
        Scanner sc=new Scanner(System.in);
        int ch;
        do{
            System.out.println("1:Deposit 2:Withdraw 3:Display 4:Exit");
            System.out.println("Enter Choice:");
            ch=sc.nextInt();
            switch(ch){
                case 1:b.depositMoney();
                break;

                case 2:b.withdrawMoney();
                break;

                case 3:b.display();
                break;

                case 4:System.out.println("Exiting.....");
                break;
            }



        }while(ch!=4);
    }
}
