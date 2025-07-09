# Start an infinite loop so the menu keeps repeating until the user chooses to exit
while True:
    # Display the menu options
    print("\nSelect The Function you want to perform")
    print("Enter the value like 1, 2, 3, 4, 5")  # Tell user how to choose
    print("Addition [1]")
    print("Subtraction [2]")
    print("Multiplication [3]")
    print("Division [4]")
    print("Exit [5]")

    # Take user input for menu selection (should be a whole number)
    a = int(input("Enter your choice: "))

    # If the user selects addition
    if a == 1:
        print("You have selected Addition")
        # Use float so both integers and decimals can be handled
        b = float(input("Enter First Number: "))
        c = float(input("Enter Second Number: "))
        d = b + c  # Perform addition
        print("Addition of entered numbers =", d)

    # If the user selects subtraction
    elif a == 2:
        print("You have selected Subtraction")
        sub1 = float(input("Enter First Number: "))
        sub2 = float(input("Enter Second Number: "))
        e = sub1 - sub2  # Perform subtraction
        print("Subtraction of entered numbers =", e)

    # If the user selects multiplication
    elif a == 3:
        print("You have selected Multiplication")
        mul1 = float(input("Enter First Number: "))
        mul2 = float(input("Enter Second Number: "))
        f = mul1 * mul2  # Perform multiplication
        print("Multiplication of entered numbers =", f)

    # If the user selects division
    elif a == 4:
        print("You have selected Division")
        div1 = float(input("Enter First Number: "))
        div2 = float(input("Enter Second Number: "))
        # Check for division by zero to prevent runtime error
        if div2 != 0:
            g = div1 / div2  # Perform division
            print("Division of entered numbers =", g)
        else:
            print("Error: Cannot divide by zero.")  # Handle divide-by-zero case

    # If the user selects to exit
    elif a == 5:
        print("Exiting... Bye!")  # Friendly exit message
        break  # Exit the loop and end the program

    # If the user enters an invalid option
    else:
        print("Invalid Choice. Please select a number between 1 and 5.")

#THIS COPY OF MENU DRIVEN IS NOW AVAILABLE AT: https://github.com/Arihant-code/Python-basic.git
#OR git@github.com:Arihant-code/Python-basic.git
                                               
                                               
