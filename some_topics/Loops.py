while True:
    # Prompt the user to enter the color of the signal
    signal_color = input("Enter the color of the traffic signal (RED/YELLOW/GREEN) or 'quit' to exit: ").upper()
    
    # Check if the user wants to quit
    if signal_color == "QUIT":
        print("Exiting the program.")
        break
    
    # Display the appropriate message based on the input signal color
    if signal_color == "RED":
        print("Stop")
    elif signal_color == "YELLOW":
        print("Stay")
    elif signal_color == "GREEN":
        print("Go")
    else:
        print("Invalid signal color")


# Pre-specified numbers
a = 10
b = 20
c = 15

# Find the largest number using ternary operators
largest = a if (a > b and a > c) else (b if b > c else c)

# Display the largest number
print("The largest number is:", largest)

# Input: Whole number from the user
number = int(input("Enter a whole number to find its factors: "))

# Initialize variables
i = 1

# Print the factors
print(f"The factors of {number} are:")
while i <= number:
    if number % i == 0:
        print(i)
    i += 1

