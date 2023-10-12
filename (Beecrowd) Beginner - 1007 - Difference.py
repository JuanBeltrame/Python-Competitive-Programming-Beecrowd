"""
Link to the problem: https://www.beecrowd.com.br/judge/en/problems/view/1038
----------------------------------------------------------------------
Using the following table, 
write a program that reads a code and the amount of an item. 
After, print the value to pay.

This is a very simple program with the only intention of practice of selection commands.

Input: 
The input file contains two integer numbers X and Y. 
X is the product code and Y is the quantity of this item according to the above table.

Output: The output must be a message "Total: R$ " followed by the total value to be paid, with 2 digits after the decimal point.
"""
X = int(input("Enter Code: "))
while True: 
    if X == 1:
        Y = int(input("Enter Quantity:"))
    elif X == 2:
        Y = int(input("Enter Quantity:"))
    elif X == 3:
        Y = int(input("Enter Quantity:"))
    elif X == 4:
        Y = int(input("Enter Quantity:"))
    elif X == 5:
        Y = int(input("Enter Quantity:"))
    else:
        False
print("Total: R")
