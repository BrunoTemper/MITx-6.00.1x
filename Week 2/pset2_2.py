# MITx 6.00.1x
# Week 2
# Problem Set 2
#
# Problem 2: Now write a program that calculates the minimum fixed monthly 
# payment needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change
# each month, but instead is a constant amount that will be paid each month.
#


balance = 4842
annualInterestRate = 0.2
month = 0

for payment in range(0, balance, 10):

    newBalance = balance

    while month < 12:
        newBalance -= payment
        interest = ((annualInterestRate/12) * newBalance)
        newBalance += interest
        month += 1

    month = 0
    if newBalance <= 0:
        print("Lowest Payment: " + str(payment))
        break