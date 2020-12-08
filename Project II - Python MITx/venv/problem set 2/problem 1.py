balance = 42
annualInterestRate = .18
monthlyPaymentRate = .02

def updateBalance(balance, payment):
    """
    :param balance: float
    :param payment: float
    :return: updated balance to next month, type float
    """
    unpaidBalance = balance - payment
    newBalance = unpaidBalance + unpaidBalance*(annualInterestRate/12)
    return newBalance

for i in range(12):
    balance = updateBalance(balance, monthlyPaymentRate*balance)
print("remaining balance: "+str(round(balance, 2)))