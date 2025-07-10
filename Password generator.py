# Menu-Driven Password Generator without def or import

while True:
    print("\n--- Password Generator Menu ---")
    print("\n1. Generate Password")
    print("2. Exit")

    choice = input("\nEnter your choice (1 or 2): ")

    if choice == "1":
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!@#$%^&*()-_=+[]{};:,.<>/?"
        all_chars = letters + numbers + symbols

        # Simulate a seed using simple math
        n = 1
        for i in range(500):
            n = (n * 1299721 + 1234567) % 1000000007

        try:
            length = int(input("\nEnter password length: "))
            password = ""

            for i in range(length):
                n = (n * 9301 + 49297) % 233280
                index = n % len(all_chars)
                password += all_chars[index]

            # Simulated delay without import
            print("\nGenerating password, please wait...")
            for i in range(7000000):  # Fake delay loop
                pass
            print("\nGenerated Password:", password)

        except:
            print("Invalid input. Please enter a number.")

    elif choice == "2":
        print("Exiting. Have a nice day!")
        break
        exit()

    else:
        print("Invalid choice. Please press 1 or 2.")
