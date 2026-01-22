- Loop Practice

# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

print("------------")

# 2. Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("------------")

# 3. Sum of first 5 numbers
sum = 0
for i in range(1, 6):
    sum += i
print("Sum is:", sum)

print("------------")

# 4. Multiplication table of 5
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)