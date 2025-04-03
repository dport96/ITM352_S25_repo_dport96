import pandas as pd
import numpy as np
import time
import os
import sys

def load_csv(file_path):
    """Loads a CSV file into a DataFrame with error handling, timing, and validation."""
    print(f"Loading CSV file: {file_path}")

    start_time = time.time()

    try:
        df = pd.read_csv(file_path, engine="pyarrow", on_bad_lines="skip")
        load_time = time.time() - start_time

        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        print(f"Columns: {list(df.columns)}")

        # convert dates to more useable format
        df['order_date'] = pd.to_datetime(df['order_date'],  format='%m/%d/%y', errors='coerce')
        
        # Validate necessary columns
        required_columns = {"quantity", "unit_price"}
        missing_columns = required_columns - set(df.columns)

        if missing_columns:
            print(f"⚠️ Warning: Missing columns {missing_columns}. Some analytics may not function correctly.")

        return df

    except Exception as e:
        print(f"❌ Error: Could not load the CSV file. Reason: {e}")
        return None

def display_initial_rows(data):
    """Prompts user for number of rows to display and validates input."""
    while True:
        user_input = input("\nEnter the number of rows to display ('all' for all rows, or press Enter to skip): ").strip().lower()

        if user_input == "":
            print("Skipping preview.")
            break
        elif user_input == "all":
            print(data)
            break
        elif user_input.isdigit():
            num_rows = int(user_input)
            if num_rows > 0:
                print(data.head(num_rows))
                break
            else:
                print("⚠️ Please enter a positive number.")
        else:
            print("⚠️ Invalid input. Enter a number, 'all', or press Enter to skip.")

def exit_program(data):
    sys.exit("Exiting program.")
    
def sales_by_region_order_type(data):
    print('sales_by_region_order_type')
    # add sales col
    data['sales'] = data['quantity'] * data['unit_price']

    # Create pivot table aggregating sales by region and order_type
    pivot_table = pd.pivot_table(data, 
                                 values='sales', 
                                 index='sales_region', 
                                 columns='order_type', 
                                 aggfunc=np.sum, 
                                 margins=True,  # Adds a 'Total' column and row
                                 margins_name="Total Sales")  # Rename total column

    # Print pivot table
    print(pivot_table)

def get_user_selection(options, prompt): 
    print(prompt) 
    for i, option in enumerate(options):
        print(f"{i+1}. {option}") 
    choice = input("Enter the number(s) of your choice(s), separated by commas: ") 
    selected = [options[int(i) - 1] for i in choice.split(',')] if choice else []
    return selected


def generate_custom_pivot_table(data):
    row_options = list(data.columns) 
    rows = get_user_selection(row_options, "Select rows:")
    col_options = [col for col in col_options if col not in rows]
    cols = get_user_selection(col_options, "Select columns:")
    value_options = list(data.select_dtypes(include=['number']).columns)
    values = get_user_selection(value_options, "Select values:")
    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(agg_options, "Select aggrigation function:")

    pivot_table = pd.pivot_table(
        data, 
        index=rows, 
        columns=cols if cols else None, 
        values=values, 
        aggfunc=agg_func
    )
    print(pivot_table)
    
def display_menu(data):
    menu_options = (
        ("Show the first n rows of sales data", display_initial_rows),
        ("Show the sales by region and order_type", sales_by_region_order_type),
        ('Custom pivot table', generate_custom_pivot_table),
        ("Exit the program", exit_program)
    )
    
    while True:
        print("\nMenu:")
        for i, (option, _) in enumerate(menu_options, 1):
            print(f"{i}. {option}")
        
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(menu_options):
                menu_options[choice - 1][1](data)  # Call the corresponding function
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    file_path = "sales_data_test.csv"  
    #file_path = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'

    df = load_csv(file_path)

    if df is not None:
        display_menu(df)
                

if __name__ == "__main__":
    main()