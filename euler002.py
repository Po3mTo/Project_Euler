total = 0
first , second = 1,2
while second <= 4000000:
    if second % 2 == 0:
        total += second
    first, second = second , first + second

print(total)