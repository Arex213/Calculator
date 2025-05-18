# This is a simple calculator program that performs basic arithmetic operations.
while True:
    print('Welcome To The Calculator')
    # Here we input our numbers and the operator
    num1 = float(input('Write your first number: '))
    semb = input('+,-,*,/ : ')
    num2 = float(input('Write your second number: '))

    # Here we check the operator and do the calculation
    if semb=='+':
        print(num1 + num2)

    elif semb=='-': 
        print(num1 - num2)

    elif semb=='*':
        print(num1 * num2)

    elif semb=='/':
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")

    elif semb=='%':
        print(num1 % num2)
    
    elif semb=='**':
        print(num1 ** num2)

    elif semb=='//':
        if num2 != 0:
            print(num1 // num2)
        else:
            print("Error: Division by zero is not allowed.")

    else:
        print("Invalid operator.")
        
        
# Ask if the user wants to continue
    again = input("Do you want to calculate again? (y/n): ")
    if again.lower() != 'y':
        print("Bye!")
        break