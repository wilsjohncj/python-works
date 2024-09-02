# emi calculator
# EMI = p*r*(1+r)**n/(1+r)**n-1
# Where P represents the principal amount borrowed.
# R represents the per-month interest rate (for example,
# if the annual interest rate is 12%, then monthly interest will be 1% (12% / 12)).
# N represents the loan period in months.
p = int(input("Loan amount "))
R = int(input("interest rate "))
tenure = int(input("No. of years - Tenure "))
rm = R/12/100 # monthly interest rate
tenure_months = tenure * 12 # number of months totally
print(f" Loan amoun Rs.= {p}")
print(f" Rate of interest = {rm} per year")
print(f" Loan tenure = {tenure_months} monhts")
emi = (p*rm*(1+rm)**tenure_months) / ((1+rm)**tenure_months-1)
print(f" EMI =  {round(emi)}")
# print(f" Total amount paid {emi}*{tenure_months} ") this will work ??

total_amt_paid= emi * tenure_months
print(f" Total amount paid {total_amt_paid}")

# output below
#Loan amoun Rs.= 200000
# Rate of interest = 0.0075 per year
# Loan tenure = 120 monhts
# EMI =  2534
# Total amount paid 304021.8570005972
