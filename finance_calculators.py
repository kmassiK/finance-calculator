# Capstone Project - Variables and Control Structures

# Use the input() function to prompt the user to enter either 'investement' or 'bond'.
# str.lower() is used to convert entries into lower cases, this will prevent errors if the user enters capital letters.
# if - elif - else statements are used to work out different conditions and display outcomes according to user choices.
#  the 1st if statement is nested as there're 2 conditions to choose from: 'simple' or 'compound' interest.
# round() function is used to limit the output to 2 decimal point.


import math
print()
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print()
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

user_choice = user_choice.lower()

if user_choice == "investment":
    user_deposit = float(input("Enter deposit amount: "))
    interest_rate = float(input("Enter interest rate excluding the percentage '%' sign: "))
    num_year = int(input("Enter investment length in years: "))
    interest = input("Interest type; enter either 'simple' or 'compound: ")
    interest = interest.lower()

    if interest == "simple":
        p = user_deposit
        r = interest_rate / 100
        t = num_year
        A = p * (1 + r * t)   # A is the total amount they'll get back after a given period.
        A = round(A, 2)
        print(f"Total amount after {num_year} years is {A}")

    elif interest == "compound":
        p = user_deposit
        r = interest_rate / 100
        t = num_year
        A = p * math.pow((1 + r), t)
        A = round(A, 2)
        print(f"Total amount after {num_year} years is {A}")

    else:
        print("This is not a valid entry. You must enter either 'simple' or 'compound'")

elif user_choice == "bond":
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate excluding the percentage '%' sign: "))
    num_month = int(input("Enter the number of months over which to repay the bond: ")) 
    p = present_value
    i = (interest_rate / 100) / 12
    n = num_month
    repayment = (i * p) / (1 - (1 + i) ** (-n))
    repayment = round(repayment, 2)
    print(f"Amount to be repaid each month: {repayment}")

else:
    print("This is not a valid entry. Please enter either 'investment' or 'bond'")
