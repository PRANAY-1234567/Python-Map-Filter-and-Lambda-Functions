# a=['Hello','Good','Morning']
# res = map(len,a)
# print(list(res))

# a=['10','20','30']
# res = map(int,a)
# print(list(res))

'''numbers = eval(input("Enter the numbers: "))
print(list(map(lambda x: x**2, numbers)))
'''
"""
Filter is a inbuilt class in the python which will itterate on each value and filter 
the value based on user condition and require 
"""

'''a = [10,21,30,40,50]
res = filter(lambda x:x%2==0, a)
print(list(res))'''

"""a=[40,43,48,60,75,83]
res = filter(lambda x:x%5==0, a)
print(list(res))"""

'''
a=[10,12,13,6,9,7]
res = filter (lambda x:x%2 ==0, a)
print(list(res))
'''

'''
a=[10,12,13,6,9,7]
print(list(map(lambda x:x**2, filter(lambda x:x%2==0, a))))
'''