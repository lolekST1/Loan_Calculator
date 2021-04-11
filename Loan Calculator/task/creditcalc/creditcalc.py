import math
import argparse
import sys

parser = argparse.ArgumentParser(description="Loan calculator")
parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)
args = parser.parse_args()
arglist = [a for a in vars(args).values() if type(a) != str and a]
#
if len(sys.argv) != 5:
    print("Incorrect parameters", sys.argv)
elif not args.interest:
    print("Incorrect parameters", sys.argv)
elif any(a < 0 for a in arglist):
    print("Incorrect parameters", sys.argv)
elif args.type != "annuity" and args.type != "diff":
    print("Incorrect parameters", args.type)
elif args.type == "diff" and args.payment:
    print("Incorrect parameters", sys.argv)

elif args.type == "annuity" and args.principal and args.payment:  # number of months
    principal = args.principal
    monthly_payment = args.payment
    loan_interest = args.interest
    monthly_interest = loan_interest / (12 * 100)
    months_num = math.log(monthly_payment / (monthly_payment - monthly_interest * principal), (1 + monthly_interest))
    if months_num == 1:
        print("It will take 1 month to repay the loan")
    elif math.ceil(months_num) < 13:
        print(f"It will take {math.ceil(months_num)} months to repay the loan")
    else:
        months = math.ceil(months_num) % 12
        years = math.ceil(months_num) // 12
        if months == 0:
            if years == 1:
                print(f"It will take 1 year to repay the loan")
            else:
                print(f"It will take {years} years to repay the loan")
        else:
            if years == 1:
                print(f"It will take 1 year and {months} months to repay the loan")
            else:
                print(f"It will take {years} years and {months} months to repay the loan")
    interest_paid = math.ceil(months_num) * monthly_payment
    print(f"\nOverpayment = {math.ceil(interest_paid - principal)}")
elif args.type == "annuity" and args.periods and args.payment:  # loan principal
    annuity_payment = args.payment
    months_num = args.periods
    loan_interest = args.interest
    monthly_interest = loan_interest / (12 * 100)
    principal = annuity_payment / (monthly_interest * math.pow((1 + monthly_interest), months_num) / (
            math.pow((1 + monthly_interest), months_num) - 1))
    interest_paid = months_num * annuity_payment
    print(f"Your loan principal = {int(principal)}!")
    print(f"\nOverpayment = {math.ceil(interest_paid - principal)}")

elif args.type == "annuity" and args.periods and args.principal:  # annuity payment
    principal = args.principal
    months_num = args.periods
    loan_interest = args.interest
    monthly_interest = loan_interest / (12 * 100)
    annuity_payment = principal * (monthly_interest * math.pow((1 + monthly_interest), months_num) / (
            math.pow((1 + monthly_interest), months_num) - 1))
    interest_paid = months_num * math.ceil(annuity_payment)
    print(f"Your annuity payment = {math.ceil(annuity_payment)}!")
    print(f"\nOverpayment = {math.ceil(interest_paid - principal)}")

elif args.type == "diff" and args.principal and args.periods:  # diff payment
    principal = args.principal
    months_num = args.periods
    loan_interest = args.interest
    interest_paid = 0
    for p in range(1, months_num+1):
        payment = math.ceil((principal / months_num) + (loan_interest / 100 / 12) * (principal - ((principal * (p - 1)) / months_num)))
        print(f"Month {p}: payment is {payment}")
        interest_paid += payment
    print(f"\nOverpayment = {interest_paid - principal}")
