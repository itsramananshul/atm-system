# Smart ATM & Banking System

This is a **Python-based ATM and Banking System** project that simulates real-world banking operations.  
It allows users to open accounts, use debit cards with PIN authentication, perform transactions, and more.

---

## Features

### For Users:
- Open a bank account with personal details (name, age, address, phone number)  
- Generate random account numbers and debit card numbers  
- Set a 4-digit PIN for your debit card  
- Deposit money  
- Withdraw money (with insufficient funds check)  
- Check account balance  
- View account statement  
- Change debit card PIN  
- ATM login allows 3 attempts for PIN before locking the account  

### For Admins:
- Secure login with password  
- View all accounts with account number, balance, and status  
- Unlock locked accounts  
- Admin password requires correct entry (type 1 to return to main menu)  

### Data Persistence:
- All accounts are stored in `accounts.txt`  
- Each line contains:  
name,age,address,phone,account_number,debit_card_number,balance,PIN,status

- Accounts stay persistent even after program closes  

### Security:
- Locked accounts cannot access ATM until unlocked by admin  
- PIN attempts are tracked, and account status updates automatically  

---

## How it Works

### Open Account:
1. User enters personal info  
2. Minimum deposit is $45  
3. System generates random account and debit card numbers  
4. User sets a 4-digit PIN  
5. Account info is saved to `accounts.txt`  

### ATM Login:
1. Enter debit card number  
2. Enter PIN (3 attempts max)  
3. Access banking options: Balance, Deposit, Withdraw, Statement, Change PIN  
4. Failed PIN attempts lock the account  

### Admin Login:
1. Enter admin password  
2. View all accounts  
3. Unlock accounts if needed  

---

## Challenges & Solutions
- Generating unique account and debit card numbers  
- Storing and loading accounts reliably from a text file  
- Handling incorrect PIN attempts and automatically locking accounts  
- Implementing a continuous menu for both users and admin  
- Maintaining data integrity while updating balances and account statuses  
- Debugging edge cases like insufficient funds, invalid inputs, and login attempts  

---

## Requirements
- Python 3.x  
- No external libraries required  

---

## How to Run
### Clone the repository:
```bash
git clone https://github.com/itsramananshul/atm-system.git
Navigate to the folder:
cd atm-system
Run the program:
python atm.py
File Structure
atm.py – main Python program

accounts.txt – stores all account information

