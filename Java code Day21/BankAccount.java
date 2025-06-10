import java.util.*;
public class BankAccount {
    long acc_no;
    String name,ac_type;
    double balance, deposit,withdraw;

    Scanner sc=new Scanner(System.in);
    BankAccount(){
        System.out.println("Enter Name:");
        name=sc.nextLine();
        System.out.println("Enter Account No:");
        acc_no=sc.nextLong();
        sc.nextLine();
        System.out.println("Enter Account Type:");
        ac_type=sc.nextLine();
        System.out.println("Enter You account Balance:");
        balance=sc.nextDouble();
    }

    void withdrawMoney(){
        System.out.println("Enter Money to withdraw:");
        withdraw=sc.nextDouble();
        if(withdraw>balance){
            System.out.println("No Sufficient Balance to withdraw");

        }
        else{
            balance -=withdraw;
            System.out.println("Withdraw Successfully");
            System.out.println("Available Balance is:"+balance);
        }
    }

    void depositMoney(){
        System.out.println("Enter Amount to be deposit:");
        deposit =sc.nextDouble();
        balance +=deposit;
        System.out.println("Deposit Successfully");
        System.out.println("Available Balance:"+balance);
    }
    void display(){
        System.out.println("Name:"+name);
        System.out.println("Available Balance:"+balance);
    }
}
