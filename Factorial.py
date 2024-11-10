# A recursive algorithm can always be an iterative algorithm
# A recursive algorithm calls itself, can be performed by a loop
"""A maze as an example: in a maze you must choose a path to follow, and once you hit a dead end you must back track"""
'''
Making a recursive algorithm: 
1. Identify a base case and recursive case.
--> Recursive: Break the problem into subproblems (a process that needs to be repeated)
--> Base case: You want the case to stop when you have an answer for the subproblem.
        Ex: were looking through subfolders and our key is not in one of them , we have our answer and we can move on.
2. We will always have one base case and one recursive case
Ex: The fibonacci sequense's bigger goals is adding up all the numbers, the small goal is to just add up the prev 2 numbers

'''
def factorial(num):
    product = 1
    for i in range(1, num +1):
        product = product * i
    return product
print(factorial(5))

def factorial2(num):
    if num == 1:
        return 1
    else:
        return num*factorial2(num-1)

print(factorial2(3))

def fibonacci(nthNum):
    a,b = 1,1
    print('a=%s, b =%s'%(a,b))
    for i in range (1,nthNum):
        a,b = b, a + b
        print('a=%s, b = %s'% (a,b))
    return a

fibonacci(10)


def fibonacci2(num):
    print('fibonacci2(%s) called.' % (num))
    if num == 1 or num == 2:
        print('Call to fibonacci2(%s) and fibonacci2(%s)'% (num))
        return 1
    else:
        print('Calling fibonacci2(%s) and fibonacci2(%s)' % (num - 1, num - 2))
        result = fibonacci2(num-1) + fibonacci2(num-2)
        print('Call to fibonacci2(%s) returning %s'% (num, result))
        return result


fibonacci(5)
fibonacci2(5)

