def seriesSum(num):
    # num represents our n
    product = 0
    # Create non-local product variable, will be given a number by iterator
    # If were going to use a loop we need an iterator
    for i in range(1, num +1):
        product = product + i
    return product

print(seriesSum(3))

def seriesSumF(num):
    '''when creating a recursive function we need a base case and recursive case'''
    if num == 1:
        return 1
    else:
        return num + seriesSumF(num - 1)


print(seriesSumF(3))

def sumPowersof2(num):
    # to calculate iteratively we need a loop
    product = 0
    for i in range(1, num+1):
        product += 2 ** i
    return product

print(sumPowersof2(3))

def sumPowersof2R(num):
   if num == 0:
       return 1
   else:
       return 2 ** sumPowersof2R(num-1) # reduce the problem, if we don't then its forever




print(sumPowersof2R(3))






