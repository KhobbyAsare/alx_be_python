"""
To format the date and time into a more readable string like "YYYY-MM-DD HH:MM:SS", you should use strftime().
"""

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
    return current_date  # return datetime object for further use


def calculate_future_date():
    """
    Prompts user for number of days and calculates the future date
    """
    try:
        curr_date = display_current_datetime()  # returns a datetime object
        number_of_days = int(input("Enter a number of days: "))
        future_date = curr_date + timedelta(days=number_of_days)
        print(f"Future date: {future_date}")
        # print("Future Date after", number_of_days, "days:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer for the number of days.")

# Run the program
if __name__ == "__main__":
    calculate_future_date()

