atm_money = {1000: 5, 500: 10, 200: 10}
total_amt = 0
for k, v in atm_money.items():
    total_amt += k * v

transactions = list()

balance = int(input("Enter the balance : "))


def withdraw():
    global total_amt
    global balance
    global transactions
    amt = int(input("Enter the withdraw amount : "))
    permitted_amt = 0.9 * total_amt
    if amt > permitted_amt:
        return "Sorry, transaction not permitted. Maximum amount permitted is {} ".format(permitted_amt)
    else:
        temp_amt = amt
        denominations = list(atm_money.keys())
        i = 0
        while temp_amt > 0:
            if i == len(denominations) :
                return "Unavailable notes"
            notes = temp_amt // denominations[i]
            if notes > atm_money[denominations[i]]:
                return "Transaction can not be done."
            temp_amt = temp_amt % denominations[i]
            atm_money[denominations[i]] -= notes
            i += 1
            
                
        total_amt -= amt
    balance -= amt

    transaction = "Withdrawn Rs. {} ".format(amt)
    transactions.append(transaction)
    return transaction


def view_transaction_history():
    global transactions
    if len(transactions) == 0 :
        print("No transactions made ")
    elif len(transactions) < 3 : 
        print("\nYour previous transactions : ")
        i = len(transactions) - 1
        while i > -1 :
            print(transactions[i])
            i -=1
    else : 
        i = len(transactions) - 1
        print("\nYour Last 3 Transactions in reverse chronological order : ")
        while i >= len(transactions) - 3 :
            print(transactions[i])
            i -=1


def exit():
    print("Exiting")


choice = 1
while choice < 3:
    choice = int(
        input("1. Withdraw Money\t2. View Transaction History\t3. Exit : \t"))
    if choice == 1:
        transaction_msg = withdraw()
        print(transaction_msg)
    elif choice == 2:
        view_transaction_history()
    else:
        exit()
#########        Output : 
#########            Enter the balance : 5000
#########            1. Withdraw Money       2. View Transaction History     3. Exit :       1
#########            Enter the withdraw amount : 400
#########            Withdrawn Rs. 400
#########            1. Withdraw Money       2. View Transaction History     3. Exit :       1
#########            Enter the withdraw amount : 500
#########            Withdrawn Rs. 500
#########            1. Withdraw Money       2. View Transaction History     3. Exit :       1
#########            Enter the withdraw amount : 10000
#########            Sorry, transaction not permitted. Maximum amount permitted is 9990.0
#########            1. Withdraw Money       2. View Transaction History     3. Exit :       1
#########            Enter the withdraw amount : 6000
#########            Transaction can not be done.
#########            1. Withdraw Money       2. View Transaction History     3. Exit :       1
#########            Enter the withdraw amount : 3000
#########            Withdrawn Rs. 3000 
#########            1. Withdraw Money       2. View Transaction History     3. Exit :       1
#########            Enter the withdraw amount : 400
#########            Withdrawn Rs. 400 
#########            1. Withdraw Money       2. View Transaction History     3. Exit :       2
#########            
#########            Your Last 3 Transactions in reverse chronological order :         
#########            Withdrawn Rs. 400 
#########            Withdrawn Rs. 3000 
#########            Withdrawn Rs. 500 
#########            1. Withdraw Money       2. View Transaction History     3. Exit :       3
#########            Exiting