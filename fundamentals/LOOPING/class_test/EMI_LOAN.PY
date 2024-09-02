# Program to calculate monthly EMI and total payable for loan
loan_amount=int(input("Enter loan amount"))
interest_rate=int(input("Enter interest rate"))
loan_tenure=int(input("Enter loan tenure (years)"))

interest_rate_monthly = interest_rate/12*100
emi=loan_amount*interest_rate_monthly*((1+interest_rate_monthly)**interest_rate_monthly)/(1+interest_rate_monthly)**interest_rate-1
print(emi)
