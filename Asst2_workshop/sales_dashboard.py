import pandas as pd
import time
import os

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


def main():
    file_path = "sales_data_test.csv"  
    #file_path = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'

    df = load_csv(file_path)

    if df is not None:
        while True:
            display_initial_rows(df)
            continue_prompt = input("\nWould you like to preview again? (yes/no): ").strip().lower()
            if continue_prompt != "yes":
                print("Exiting program.")
                break

if __name__ == "__main__":
    main()