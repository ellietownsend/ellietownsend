# Stack overflow error: to many frame objects are being created and none are being taken off
# The data frame objects are getting to high, will cap out at 100
# No damage is done to the computer

# Avoiding the crash: Base case: stops the function from calling itself and just returns
# the alternative to base case is a recursive case: if there is no base case to the recursive case , stack overflow error

# First step to writing recursive function: What is the bast case, and what is the recursive case
def countDownandUp(num):
    print(num)
    if num == 0: # Since 0 is the base case it is popped off stack
        # BASE CASE, COMES FIRST
        print('Reached the base case:')
        return # This return refers to the inner call of countDownandUp and the outer call of countDownandUp
    else:
        # RECURSION CASE, WHAT WE WANT REPEATED
        countDownandUp(num - 1) # return breaks us out of this and puts us right to the next one
        print(num, 'returning') # any code after the recurse case will still have to run



countDownandUp(3)



