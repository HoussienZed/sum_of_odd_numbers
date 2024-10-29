# asking user to enter a number n
n = int(input("Enter a number: "))

sum = 0
# selecting odd numbers less than n
for i in range(1, n, 1):
    if i % 2 != 0:
        sum += i

print(f"The sum of odd numbers up to n = {sum}")
