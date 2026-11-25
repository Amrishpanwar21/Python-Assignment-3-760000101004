numbers = [10, 20, 30, 40, 50]

num = int(input("Enter number: "))

if num in numbers:
    print("Index =", numbers.index(num))
else:
    print("Element not found")