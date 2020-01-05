n = int(input())
dict = {}

for _ in range(n):
    name, number = input().split(" ")
    dict[name] = number

while True:
    try:
        name_to_check = input()
    except:
        break
    if name_to_check not in dict:
        print("Not found")
    else:
        print(f"{name_to_check}={dict[name_to_check]}")
