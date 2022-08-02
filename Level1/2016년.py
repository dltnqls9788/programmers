def solution1(a,b):
    
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']

    sum = 0 
    if a > 1: 
        for i in range(a-1):
            sum += month[i]
        sum += b
    else:
        sum += b 
    return day[sum%7-1]


def solution2(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    return days[(sum(month[:a-1])+b)%7 - 1]