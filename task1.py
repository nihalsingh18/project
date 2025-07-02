num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose operation:")
print("1. +  2. -  3. *  4. /")
choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == '2':
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == '3':
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice == '4':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero.")
else:
    print("Invalid choice.")
