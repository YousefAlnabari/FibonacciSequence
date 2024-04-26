x = int(input("Enter number: "))
n = 0
z = 1
while n <= x:
    if n == x:
        print("Fibonacci number!")
        break
    n += z
    z = n - z
else:
    print("Not a Fibonacci number")
