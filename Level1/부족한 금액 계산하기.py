def solution1(price, money, count):
    sum = 0 
    for i in range(count+1):
         sum += price * i 
    if sum > money:
        return sum - money 
    else:
        return 0