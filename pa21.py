
num = int(input("Enter Number : "))
for i in range(num + 1):
    if i % 4 == 0 and i % 5 == 0:
        print("Number divisible by 4 and 5")
    else:
        print("Numbers not divisible by 4 and 5")
