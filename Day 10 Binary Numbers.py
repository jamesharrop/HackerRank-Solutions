# Finding the max number of consecutive 1's in a binary number
n = int(input())
x = bin(n)[2:]
count = 0
max_count = 0
for digit in x:
    if digit == "1":
        count += 1
    else:
        if max_count<count:
            max_count = count
        count = 0

if max_count<count:
    max_count = count

print(max_count)