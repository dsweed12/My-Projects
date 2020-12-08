def payingOffInAyear(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12
    payment = 10
    while balance > 0:
        bal = balance
        for i in range(12):
            unpaidBalance = bal - payment
            bal = unpaidBalance + unpaidBalance*monthlyInterestRate
        if bal <= 0:
            return payment
        payment += 10
print("lowest payment: "+str(payingOffInAyear(50000000, 0.20)))