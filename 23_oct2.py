#Write a function that takes an argument that is dictionary and returns a dictionary where keys are value and values are key

def swap(d):
    return {v:k for k,v in d.items()}
d={1:'a',2:'b',3:'c'}
print(swap(d))
