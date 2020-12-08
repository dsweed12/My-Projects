balance = 320000
annualInterestRate = 0.20
monthlyInterestRate = annualInterestRate / 12.0
paymentLow = balance/12.0
paymentHigh = (balance*(1+monthlyInterestRate)**12)/12.0
epsilon = 0.1
while balance > 0:
    bal = balance
    payment = round((paymentLow + paymentHigh) / 2, 2)
    for i in range(12):
        unpaidBalance = bal - payment
        bal = unpaidBalance + unpaidBalance*monthlyInterestRate
    if bal > epsilon:
        paymentLow = payment
    elif bal < -epsilon:
        paymentHigh = payment
    else:
        print("lowest payment: " + str(payment))
        break

