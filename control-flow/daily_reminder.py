
"""
Task Description:

Develop a script named daily_reminder.py. This script will ask the user for a single task, its priority level, and
if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow
and loops without relying on data structures to store multiple tasks.
"""

# Ask for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()



match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder:'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder:'{task}' is a high priority task. Make sure to address it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder:'{task}' is a medium priority task that is time-sensitive. Try to complete it today.")
        else:
            print(f"Reminder:'{task}' is a medium priority task. Plan to get it done this week.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder:'{task}' is a low priority but time-bound task. Schedule a time today to complete it.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Reminder: Priority '{priority}' not recognized. Please enter high, medium, or low.")

