# pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in a single row
    for _ in range(size):
        print("*", end="")  # Print asterisk without moving to a new line
    print()  # Move to the next line after printing a row
    row += 1  # Increment row counter
