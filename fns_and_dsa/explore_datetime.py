from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in the format YYYY-MM-DD HH:MM:SS."""
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """Calculates and displays a future date based on user input (number of days)."""
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=days_to_add)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()