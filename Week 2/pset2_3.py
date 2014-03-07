# MITx 6.00.1x
# Week 2
# Problem Set 2
#
# Problem 3: Use bisection search to figure out payment to the cent
# and to make the program run faster
#

balance = 999999
annualInterestRate = 0.18

found = True
monthlyInterestRate = annualInterestRate / 12
lower = balance/12
upper = (balance * (1+monthlyInterestRate)**12)
payment = (lower + upper) / 2

while (found):

    newBalance = balance
    month = 0
    
    while month < 12:
        newBalance -= payment
        interest = ((annualInterestRate/12) * newBalance)
        newBalance += interest
        month += 1
    
    if newBalance >=-0.02 and newBalance <= 0.02:
        print("Lowest Payment: %.2f " % payment)
        found = False
        break
    elif newBalance > 0.1:
        lower = payment
        payment = (lower + upper) / 2
    else:
        upper = payment
        payment = (lower + upper) / 2

    print("Payment: %.2f - Balance: %.2f" % (payment, newBalance))
        
