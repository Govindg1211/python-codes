#wap to create a list of squares of numbers from 1 to n using list comprehension 

n = int(input("Enter the number: "))
square = [i ** 2 for i in range(1,n+1)]
print(square)

