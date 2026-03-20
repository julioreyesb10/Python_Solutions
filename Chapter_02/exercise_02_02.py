# Starting Out with Python, Third Edition
# Capítulo 2, Ejercicio 2
"Sales prediction"
"""
A company has determined that its annual profit is typically 23 percent of total sales. Write
a program that asks the user to enter the projected amount of total sales, and then displays
the profit that will be made from that amount.
Hint: Use the value 0.23 to represent 23 percent.
"""

def sales_prediction():
    annual_profit = 0.23
    projected_amount = float(input("What is the projected amount: "))
    profit = projected_amount * annual_profit
    print("Total sales: ", profit)

def main():
    sales_prediction()
    pass

if __name__ == "__main__":
    main()
