'''head tail technique for splitting data'''
'''Three basic questions: What is the base case? 
What argument is passed to the recursive function? 
How do these arguments get us closer to the basecase?
'''
# Examining the head tail technique:
# Splits recursive functions array argument into two parts, the first element, and everything else after it)
# Plan: get the tail of the arrays sum, then add it to the first element
# - Find the tail sum by calling it recursively
# In fact we'll seperate it so much it becomes its own array
# But once that array is empty there is no more to add, hence our base case

'''What is thr base case? When our array no longer has any numbers, sum = 0
What is the argument that passed in our recursive function: It has to be going down, the tail 
How does the argument get closer to the base case? The array element shrinks by one each recursive call'''



def sum(numbers):
    if len(numbers) == 0:
        #len(numbers) is at 0, our array is empty, there is nothing more to add
        return 0
    #reutrn 0 = were done
    else:
        head = numbers[0] #to use the head tail method we need to define both, single number
        tail = numbers[1:] #python uses [1:] to define range
        return head + sum(tail) #each recursive call passes a smaller array

    # Stacking Visualization:
    # What it returns: 1 + sum [2,3,4,5]
    '''Before it can add, another responsability gets put on the stack'''
    #What it returns: 2 + sum[3,4,5]
    # -- Why does it return at two instead of 1? We are giving it the tail, a new array
    # What it returns: 3 + sum[4,5]
    # What it returns: 4 + sum[5]
    # What it returns: 5 + sum[0]
    '''We have reached 0! But now we got a list of things to do'''
    # 5 + 0 = 5
    # 5 + 4
    # 5 + 3
    # ...

num = [1,2,3,4,5]
print("The sum of the numbers", num, "is", sum(num))

# Reversing a String:
def reverse(string):
    if len(string) == 0 or len(string) == 1:
        return string
    else:
        head = string[-1]
        tail =  string[:-1]
        return head + reverse(tail)

print(reverse("im ellie"))

'''Thinking: if the middle characters reversed are the same, and the back and front are the same, palindrome'''

def ifPalindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    else:
        head = string[0]
        tail = string[-1]
        middle = string[1:-1]
        return head == tail and ifPalindrome(middle)
'''Stack Visualization:
    The head and the tail are constanly changing, First pass:
    1. head = "l" and the tail is "l", so they are equal
    2. head = "e" and the tail is "e"
    ifPalindrome(middle), just works to keep redefining
    '''

print(ifPalindrome("racecar"))

