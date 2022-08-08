# 내가 푼 방법
n, m, k = 5, 8, 3
x = [2,4,5,4,6]

x = sorted(x, reverse=True)

sum = 0 
while m!=0:
    for i in range(k):
        sum += x[0]
        m -= 1 
    sum += x[1]
    m -=1 


# 나동빈 방법 1
# N, M, K를 공백으로 구분하여 입력받기 
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기 
data = list(map(int, input().split()))

data.sort()  # 입력받은 수들 정렬하기 
first = data[n-1]  # 가장 큰 수 
second = data[n-2]  # 두 번째로 큰 수 

result = 0 

while True:
    for i in range(k):  # 가장 큰 수를 k번 더하기 
        if m == 0:  # m이 0이라면 반복문 탈출  
            break 
        result += first 
        m -= 1 # 더할 때마다 1씩 빼기 
    if m == 0:  # m이 0이라면 반복문 탈출
        break
    result += second  # 두 번째로 큰수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기 


# 나동빈 방법 2 
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += int(m%(k+1)) # 나누어 떨어지지 않는 경우 고려 

result = 0 
result += count * first
result += (m-count) * second 