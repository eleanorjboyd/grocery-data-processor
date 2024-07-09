import pandas as pd
import sys
# get environment variable
import os

def add_item_to_table(table_path, name, price, quantity):
    table = pd.read_csv(table_path)
    new_item = pd.DataFrame({"Name": [name], "Price": [price], "Quantity": [quantity]})
    updated_table = pd.concat([table, new_item], ignore_index=True)
    # if the test constant is set, print the table to the console instead of saving
    try:
        TEST_CONST = os.environ["TEST_CONST"]
    except KeyError:
        TEST_CONST = '0'
    if TEST_CONST == '1':
       print(" \n \n TEST_CONST is 1: Printing table to console! \n")
       print(updated_table.to_markdown())
    else:
        print("\n \n Only saving table, not printing to console.")
    updated_table.to_csv(table_path, index=False)
    print(f"Item '{name}' added to the table.")


def remove_item_from_table(table_path, name):
    table = pd.read_csv(table_path)
    updated_table = table[table['Name'] != name]
    updated_table.to_csv(table_path, index=False)
    print(f"Item '{name}' removed from the table.")


def increment_item_quantity(table_path, name, increment):
    table = pd.read_csv(table_path)
    item = table[table['Name'] == name]
    # if item.empty:
    #     print(f"Item '{name}' not found in the table.")
    #     add item to table, then increment quantity
    # else:
    item_index = item.index[0]
    table.at[item_index, 'Quantity'] += increment
    table.to_csv(table_path, index=False)
    print(f"Quantity of item '{name}' incremented by {increment}.")

def decrement_item_quantity(table_path, name, decrement):
    table = pd.read_csv(table_path)
    item = table[table['Name'] == name]
    if item.empty:
        print(f"Item '{name}' not found in the table.")
    else:
        item_index = item.index[0]
        table.at[item_index, 'Quantity'] -= decrement
        table.to_csv(table_path, index=False)
        print(f"Quantity of item '{name}' decremented by {decrement}.")

def main():
    table_path = "data/grocery_data.csv"
    action = sys.argv[1]
    if action == "add":
        name = input("Enter the name: ")
        price = float(input("Enter the price: "))
        quantity = int(input("Enter the quantity: "))
        add_item_to_table(table_path, name, price, quantity)
    elif action == "remove":
        name = input("Enter the name of the item to remove: ")
        remove_item_from_table(table_path, name)
    elif action == "increment":
        name = input("Enter the name: ")
        increment = int(input("Enter the increment value: "))
        increment_item_quantity(table_path, name, increment)
    elif action == "decrement":
        name = input("Enter the name: ")
        decrement = int(input("Enter the decrement value: "))
        decrement_item_quantity(table_path, name, decrement)
    else:
        print("Invalid action. Please use 'add', 'remove', 'increment', or 'decrement'.")

if __name__ == "__main__":
    main()