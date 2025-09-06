def total_cal(total_bill , waiter_tip):
    total = total_bill * (1 + 0.1 * waiter_tip)
    total = round(total , 2)
    return total
print(total_cal(1000,15))
