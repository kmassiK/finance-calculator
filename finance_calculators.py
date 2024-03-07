# Capstone Project - Variables and Control Structures

# Use the input() function to prompt the user to enter either 'investement' or 'bond'.
# str.lower() is used to convert entries into lower cases, this will prevent errors if the user enters capital letters.
# if - elif - else statements are used to work out different conditions and display outcomes according to user choices.
#  the 1st if statement is nested as there're 2 conditions to choose from: 'simple' or 'compound' interest.
# round() function is used to limit the output to 2 decimal point.



import math

print("Welcome to the Finance Calculator!")
print("Choose an option:")
print("1. Investment")
print("2. Bond")

def numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Input must be a positive number")
            return value
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number.")

def calculate_investment(user_deposit, interest_rate, num_year, interest_type):
    if interest_type == "simple":
        A = user_deposit * (1 + (interest_rate / 100) * num_year)
    elif interest_type == "compound":
        A = user_deposit * math.pow(1 + interest_rate / 100, num_year)
    return round(A, 2)

def calculate_bond(present_value, interest_rate, num_month):
    i = (interest_rate / 100) / 12
    repayment = (i * present_value) / (1 - (1 + i) ** (-num_month))
    return round(repayment, 2)


while True:
    user_choice = input("Enter the number corresponding to your choice: ")

    if user_choice == "1":
        user_deposit = numeric_input("Enter deposit amount: ")
        interest_rate = numeric_input("Enter interest rate (in %): ")
        num_year = int(numeric_input("Enter investment length in years: "))
        interest_type = input("Enter interest type (simple or compound): ").lower()

        while interest_type not in ["simple", "compound"]:
            print("Error: Invalid interest type. Please enter 'simple' or 'compound'.")
            interest_type = input("Enter interest type (simple or compound): ").lower()

        total_amount = calculate_investment(user_deposit, interest_rate, num_year, interest_type)
        print(f"Total amount after {num_year} years is {total_amount}")
        break

    elif user_choice == "2":
        present_value = numeric_input("Enter the present value of the house: ")
        interest_rate = numeric_input("Enter the interest rate (in %): ")
        num_month = int(numeric_input("Enter the number of months to repay the bond: "))

        monthly_repayment = calculate_bond(present_value, interest_rate, num_month)
        print(f"Amount to be repaid each month: {monthly_repayment}")
        break

    else:
        print("Error: Invalid choice. Please enter either '1' or '2'.")


  
