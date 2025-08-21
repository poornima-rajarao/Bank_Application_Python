# Bank Application Using Python Classes

## What this project is

This is a simple command-line based **Bank Application** implemented in Python using **Object-Oriented Programming (OOP)** principles.

---

## What it does

This application allows users to:

- Deposit money
- Withdraw money (with PIN verification)
- Check account balance (with PIN verification)
- Change their 4-digit PIN
- View account details
- Update branch name for all users (using a class method)

Each user is created as an object of the `Bank` class.

---

## Class: `Bank`

The core of the application is the `Bank` class, which manages individual bank accounts.

### Class Variables:
- `Branch`: Name of the branch (default: `'Marathahalli'`)
- `IFSC`: Branch IFSC code (default: `'BANK0000420'`)
- `ROI`: Rate of interest (default: `0.07`)

---

## Constructor (`__init__`)
Initializes a new bank account with the following attributes:
- `Name`: Account holder's name
- `Mobno`: Mobile number
- `Aadhar`: Aadhar number
- `Gender`: Gender
- `Bal`: Initial balance
- `Pin`: 4-digit PIN for authentication

---

## Available Methods

### 1. `Details()`
Displays the account holder’s complete details.

### 2. `Deposite()`
Allows the user to deposit cash between ₹100 and ₹10,000 in multiples of ₹100.

### 3. `Withdraw()`
Allows cash withdrawal with:
- PIN verification (3 attempts)
- Amount validation: ₹100–₹10,000
- Only denominations in multiples of ₹100
- Balance check before deduction

### 4. `CheckBalance()`
Prints the current balance after PIN verification (3 attempts).

### 5. `ChangePin()`
Allows the user to change their PIN after verifying the current one.

### 6. `UpdateBranch()` (Class Method)
Updates the branch for all users (e.g., from `'Marathahalli'` to `'Whitefield'`).

### 7. `Password()` (Static Method)
Used internally to prompt for 4-digit PIN input.

---

## Sample Usage

```python
# Creating user objects
User1 = Bank('Pranay', 9876543210, 123456789012, 'Male', 20000, 1234)
User2 = Bank('Dhruva', 9999999999, 234567890123, 'Male', 30000, 4321)
User3 = Bank('Greeshma', 8888888888, 345678901234, 'Female', 10000, 1111)

# Performing transactions
User1.Deposite()
User1.Withdraw()
User1.CheckBalance()
User1.ChangePin()
User1.Details()
