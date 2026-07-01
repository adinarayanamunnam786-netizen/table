# Basic Number Programs in One Page

n = int(input("Enter a number: "))

# 1. Sum of Digits
temp = n
sum_digits = 0
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
print("Sum of Digits:", sum_digits)

# 2. Reverse a Number
temp = n
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reverse:", rev)

# 3. Count Digits
temp = n
count = 0
while temp > 0:
    count += 1
    temp //= 10
print("Digit Count:", count)

# 4. Check Even or Odd
print("Even" if n % 2 == 0 else "Odd")

# 5. Check Prime Number
prime = n > 1
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        prime = False
        break
print("Prime" if prime else "Not Prime")

# 6. Factorial
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

# 7. Factors
print("Factors:", end=" ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()

# 8. Check Palindrome
print("Palindrome" if n == rev else "Not Palindrome")

# 9. Check Armstrong Number
temp = n
digits = len(str(n))
arm = 0
while temp > 0:
    digit = temp % 10
    arm += digit ** digits
    temp //= 10
print("Armstrong" if arm == n else "Not Armstrong")

# 10. Find GCD (HCF) of Two Numbers
a = int(input("Enter first number for GCD: "))
b = int(input("Enter second number for GCD: "))
x, y = a, b
while y:
    x, y = y, x % y
print("GCD (HCF):", x)