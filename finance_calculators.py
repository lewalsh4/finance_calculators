import math

# print initial menu for reference.
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan\n")

# Request 'investment' or 'bond' input from the user.
calc_type = input("Either enter 'investment' or 'bond' from the menu above to proceed: ")

# If user chooses 'investment' request information.
if calc_type == ("investment" or "Investment" or "INVESTMENT"):
    print("\nPlease enter")
    deposit = int(input("the amount of money you are depositing (e.g. 100000): "))
    interest = int(input("the interest rate (e.g. 7): "))
    years = int(input("the number of years you plan on investing (e.g. 5): "))

    interest_type = input("\nState whether you would like 'simple' or 'compound' interest: ")

    int_rate = (interest/100)/12

    # Create if and elif statements within prior one, asking whether the user 
    # requires a 'simple' or 'compound' risk calculation.
    # Carry out relevant calculation and print the answer.
    if interest_type == ("simple" or "Simple" or "SIMPLE"):
        A = deposit *(1 + int_rate * years)
        A = round(A, 2)
        print(f"You will have {A} pounds after {years} years of investment.")

    elif interest_type == ("compound" or "Compound" or "COMPOUND"):
        A = deposit * math.pow((1+int_rate),years)
        A = round(A, 2)
        print(f"You will have {A} pounds once after {years} years of investment.")
    
    # If user enters an answer outside of the options, print error message.
    else:
        print("Error, please provide an answer from the menu.")

# "bond' elif statement linked to first if statement, request information, 
# bondcalculate, and print answer.
elif calc_type == ("bond" or "Bond" or "BOND"):
    print("\nPlease enter")
    h_value = int(input("the present value of the house (e.g. 100000): "))
    bint = int(input("the interest rate (e.g. 7): "))
    months = int(input("the number of months you plan to take to repay the bond (e.g. 120): "))

    bint_rate = (bint/100)/12
    repayment = (bint_rate * h_value)/(1 - (1 + bint_rate)**(-months))
    repayment = round(repayment, 2) 
    print(f"\nYou will have to repay {repayment} pounds each month for {months} months.\n")

# else statement returns error if user input is not 'investment' and 'bond' 
else:
    print("\nError, please provide an answer from the menu.")



