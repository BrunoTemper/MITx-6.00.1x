# MITx 6.00.1x
# Week 2
# Problem Set 2
#
# Problem 1: Write a program to calculate the credit card balance after 
# one year if a person only pays the minimum monthly payment required by
# the credit card company each month.
#


balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = 1
totalPaid = 0

while month < 13:
    
    payment = balance * monthlyPaymentRate
    balance -= payment
    totalPaid += payment
    interest = ((annualInterestRate/12) * balance)
    balance += interest
    print("Month: %i " % month)
    print("Minimum monthly payment: %.2f" % payment)
    print("Remaining balance: %.2f" % balance)
    month += 1

print("Total paid: %.2f" % totalPaid)
print("Remaining balance: %.2f" % balance)
    
    
    
