#!/usr/bin/env python3

# annuityCalc.py

# Purpose: Calculate debt, annuity, amortization and interest according to mathematical formulas.

# Change working directory for the actual OS to the home directory:
def changePath():
    from pathlib import Path
    import os, platform

    if os.name == 'posix' or platform.system() == 'Darwin': 
        p = Path.home()
    if os.name == 'nt' or platform.system() == 'Windows': 
        p = Path.home()

    os.chdir(p) # Change the current working directory.

changePath()

# Main program:

def calcDebt(interestRate, years, passedYears, loan):
    numerator = ((1 + interestRate) ** years) - ((1 + interestRate) ** passedYears) 
    denominator = ((1 + interestRate) ** years) - 1
    coefficient = numerator / denominator
    debt = loan * coefficient
    return debt

def calcAnnuity(interestRate, years, loan):
    numerator = ((1 + interestRate) ** years) * interestRate
    denominator = ((1 + interestRate) ** years) - 1
    coefficient = numerator / denominator
    annuity = loan * coefficient
    return annuity

def calcRepayment(interestRate, years, passedYears, loan, annuity):
    coefficient = (1 + interestRate) ** (passedYears - 1)
    amortization = (annuity - loan * interestRate) * coefficient
    return amortization

# Insert your parameters here:

interestRate = 0.03
years = 25
loan = 250000
annuity = round(calcAnnuity(interestRate, years, loan), 2)
amortization:float = 0.00
interest:float = 0.00
resAnnuity:float = 0
resAmortization:float = 0
resInterest:float = 0

strPrint = 'loan;annuity;amortization;interest\n'
strPrint += str('{:.2f}'.format(loan)) + ';' + str('{:.2f}'.format(annuity)) + ';' + str('{:.2f}'.format(amortization)) + ';' + str('{:.2f}'.format(interest)) + '\n\n'

for passedYears in range(1, years + 1):
    resLoan = round(calcDebt(interestRate, years, passedYears, loan), 2)
    annuity = round(calcAnnuity(interestRate, years, loan), 2)
    resAnnuity = resAnnuity + annuity
    amortization = round(calcRepayment(interestRate, years, passedYears, loan, annuity), 2)
    resAmortization = resAmortization + amortization
    interest = round((annuity - amortization), 2)
    resInterest = resInterest + interest
    strResLoan = str('{:.2f}'.format(round(resLoan, 2)))
    strPrint += strResLoan + ';' + str('{:.2f}'.format(round(annuity, 2))) + ';' + str('{:.2f}'.format(round(amortization, 2))) + ';' + str('{:.2f}'.format(round(interest, 2))) +'\n'
strPrint += '\nsum' + ';' + str('{:.2f}'.format(round(resAnnuity, 2))) + ';' + str('{:.2f}'.format(round(resAmortization, 2))) + ';' + str('{:.2f}'.format(round(resInterest, 2)))

with open('annuityCalcTable.csv', 'wt', encoding='utf-8') as output:
    output.write(strPrint.replace('.', ','))
output.close()
