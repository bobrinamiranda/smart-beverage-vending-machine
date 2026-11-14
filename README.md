# Smart Beverage Vending Machine Management System

A console-based Python program that simulates an automated beverage vending machine. It manages item selection, payments, change and inventory, with a separate refill menu for the machine operator.

## Features
- Displays available beverages with price and current stock
- Multiple-quantity purchases with automatic total calculation
- Payment handling: rejects insufficient amounts and returns the money
- Change calculation, with a check that the machine has enough change
- Out-of-stock detection and quantity checks against available stock
- Refill menu: refill a single item, refill all items, or add change money
- Maximum stock limit (20 per item) enforced on every refill
- Input validation and exception handling for invalid entries
- Runs until the user exits or the machine runs out of change

## Built with
Python (dictionaries, loops, conditionals, exception handling). Developed during a Python programming internship at Taramsys Private Limited.

## How to run
1. Install Python 3.
2. Download `vending_machine.py`.
3. Run: `python vending_machine.py`

## Sample run
```
---- Vending Machine ----
Available items
1 . coffee Rs: 35 Stock: 7
2 . lemontea Rs: 30 Stock: 6
3 . coke Rs: 40 Stock: 8
4. Refill machine
5. Exit
Enter the item number: 3
You selected coke
Price: 40
How many coke do you want: 5
Total price: 200
Enter the money: 100
Insufficient amount
Returning Rs: 100
Enter the money: 250
coke dispensed successfully
Returning change Rs: 50
```
