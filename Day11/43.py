'''
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
'''

def even(x):
    return x%2==0

num = filter(lambda x:x%2==0, range(1,21))

print(list(num))

