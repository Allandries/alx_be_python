# daily_reminder.py

# Prompt the user for task details

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate the reminder using match-case

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"'{task}' has an unknown priority level. Please specify high, medium, or low."

# Modify the reminder if the task is time-sensitive

if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print the final reminder
print("\nReminder:", reminder)
