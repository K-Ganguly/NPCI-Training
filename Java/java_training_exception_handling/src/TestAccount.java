public class TestAccount {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount(10000);

        try {
            System.out.println(acc.withdrawMoney(-5900));
        } catch (BankException e) {
            System.out.println(e.getMessage());
        } catch (NumberFormatException e) {
            System.out.println(e);
        }

        try {
            acc.withdrawMoney(200000);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        try {
            acc.withdrawMoney(-1400);
        } catch (NumberFormatException | BankException) {
            System.out.println("Multi Catch : " + e.getMessage());
        }

        System.out.println("Going further ..... ");
    }

}