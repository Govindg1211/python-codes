# write a program using dictionary comprehension that creare where keys are number and its values are square of number
n = int(input("Enter the number: "))
res = {x:x**2 for x in range (0,n) if x % 2 == 0}
print(res)