def modify_immutable(x):
    x += 1
    print(f"inside function: {x}")

a = 5
modify_immutable(a)
print(f"outside function: {a}")
