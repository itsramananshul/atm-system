import random

def load_accounts():
    accounts = []
    try:
        file = open("accounts.txt", "r")
        for line in file:
            data = line.strip().split(",")

            accounts.append({
                "name": data[0],
                "age": int(data[1]),
                "address": data[2],
                "phone": data[3],
                "account_number": data[4],
                "debit_card_number": data[5],
                "balance": float(data[6]),
                "pin": data[7],
                "status": data[8]   
            })
        file.close()
    except:
        pass
    return accounts

def save_accounts(accounts):
    file = open("accounts.txt", "w")
    for acc in accounts:
        file.write(
            f"{acc['name']},{acc['age']},{acc['address']},{acc['phone']},"
            f"{acc['account_number']},{acc['debit_card_number']},"
            f"{acc['balance']},{acc['pin']},{acc['status']}\n"
        )
    file.close()


accounts=load_accounts()

while True:
    print("\n")
    print("--- Banking & ATM ---")
    Menu= print(" 1. Open a bank account\n 2. ATM Login\n 3. Exit\n 4. Admin Login")
    Menu_choice= input("Enter your choice (1-4): ")

    if Menu_choice == "1":
        print("\n--- Open a Bank Account ---")
        age = int(input("Enter your age: "))
        if age < 18:
            print("Sorry, you must be at least 18 years old to open a bank account.")
            continue
        name = input("Enter your name: ")
        address = input("Enter your address: ")
        phone = input("Enter your phone number: ")
        account_number = random.randint(10000000000, 99999999999)
        debit_card_number = str(random.randint(1000000000000000, 9999999999999999))
        deposit = float(input("Enter initial deposit amount(Min $45): "))
        if deposit < 45:
            print("Sorry, the minimum initial deposit is $45.")
            continue
        Card_PIN = input("Set your 4-digit PIN for the debit card: ")
        if len(Card_PIN) != 4 or not Card_PIN.isdigit():
            print("Invalid PIN. Please set a 4-digit numeric PIN.")
            continue

        new_account = {
            "name": name,
            "age": age,
            "address": address,
            "phone": phone,
            "account_number": account_number,
            "debit_card_number": debit_card_number,
            "balance": deposit,
            "pin": Card_PIN,
            "status": "UNLOCKED"
        }

        accounts.append(new_account)
        save_accounts(accounts)
        print(f"Congratulations {name}! Your bank account has been created successfully.")
        print(f"Your account number is: {account_number}")
        print(f"Your debit card number is: {debit_card_number}")


    elif Menu_choice == "2":
        print("\n--- ATM Login ---")
        debit_card_number = input("Enter your debit card number: ")
        account_found = False
        for acc in accounts:
            if acc["debit_card_number"] == debit_card_number:
                account_found = True
                if acc["status"] == "LOCKED":
                    print("Your account is locked. Please contact the bank for assistance.")
                    break
                attempts = 3
                while attempts > 0:
                    pin = input("Enter your 4-digit PIN: ")
                    if pin == acc["pin"]:
                        attempts=3
                        print(f"Welcome {acc['name']}! You have successfully logged in.")
                        banking_menu= print(" 1. Balance\n 2. Deposit\n 3. Withdraw\n 4. Statement\n 5. Change PIN\n 6. Exit")
                        banking_choice= input("Enter your choice (1-6): ")
                        if banking_choice == "1":
                            print("Your current balance is: $", acc['balance'])
                        elif banking_choice == "2":
                            deposit_amount = float(input("Enter the amount to deposit: "))
                            acc["balance"] += deposit_amount
                            save_accounts(accounts)
                            print(f"Deposit successful! Your new balance is: ${acc['balance']}")
                        elif banking_choice == "3":
                            withdraw_amount = float(input("Enter the amount to withdraw: "))
                            if withdraw_amount > acc["balance"]:
                                print("Insufficient funds. Withdrawal failed.")
                            else:
                                acc["balance"] -= withdraw_amount
                                save_accounts(accounts)
                                print(f"Withdrawal successful! Your new balance is: ${acc['balance']}")
                        elif banking_choice == "4":
                            print("\n--- Account Statement ---")
                            print(f"Name: {acc['name']}")
                            print(f"Account Number: {acc['account_number']}")
                            print(f"Balance: ${acc['balance']}")
                        elif banking_choice == "5":
                            new_pin = input("Enter your new 4-digit PIN: ")
                            if len(new_pin) != 4 or not new_pin.isdigit():
                                print("Invalid PIN. Please set a 4-digit numeric PIN.")
                            else:
                                acc["pin"] = new_pin
                                save_accounts(accounts)
                                print("PIN changed successfully!")
                        elif banking_choice == "6":
                            print("Thank you for using the ATM. Goodbye!")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                    else:
                        attempts -= 1
                        print(f"Incorrect PIN. You have {attempts} attempts left.")
                if attempts == 0:
                    acc["status"] = "LOCKED"
                    save_accounts(accounts)
                    print("Your account has been locked due to multiple incorrect PIN attempts. Please contact the bank for assistance.")
                break
        if not account_found:
            print("Account not found. Please check your debit card number and try again.")
    elif Menu_choice == "3":
        print("Thank you for using the ATM. Goodbye!")
        break
    elif Menu_choice == "4":
        print("\n--- Admin Login ---")
        admin_password = "bankadmin123"
        while True:
            password_attempt = input("Enter admin password (or type '1' to return to main menu): ")
            if password_attempt == "1":
                print("Returning to main menu.")
                break
            if password_attempt != admin_password:
                print("Incorrect password. Please try again.")
                continue
            if password_attempt == admin_password:
                print("Admin login successful!")
            while True:
                print("\n--- Admin Menu ---")
                print("1. View all accounts\n2. Unlock an account\n3. Exit")
                admin_choice = input("Enter your choice (1-3): ")
                if admin_choice == "1":
                    print("\n--- All Accounts ---")
                    for acc in accounts:
                        print(f"Name: {acc['name']}, Account Number: {acc['account_number']}, Balance: ${acc['balance']}, Status: {acc['status']}")
                elif admin_choice == "2":
                    account_number = input("Enter the account number to unlock: ")
                    account_found = False
                    for acc in accounts:
                        if acc["account_number"] == account_number:
                            account_found = True
                            if acc["status"] == "UNLOCKED":
                                print("This account is already unlocked.")
                            else:
                                acc["status"] = "UNLOCKED"
                                save_accounts(accounts)
                                print(f"Account {account_number} has been unlocked successfully.")
                            break
                    if not account_found:
                        print("Account not found. Please check the account number and try again.")
                elif admin_choice == "3":
                    print("Exiting admin menu.")
                    break
    else:
        print("Invalid menu choice. Please try again.")
