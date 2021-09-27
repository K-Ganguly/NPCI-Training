public class BankAccount {
    float balance;

    BankAccount() {
        this.balance = 0;
    }

    BankAccount(float openingBalance) {
        this.balance = openingBalance;
    }

    float withdrawMoney(float withdrawAmt) {
        if (withdrawAmt > balance) throw new BankException();
    }

    float depositMoney(float depositAmt) {
        this.balance += depositAmt;
        return this.balance;
    }
}