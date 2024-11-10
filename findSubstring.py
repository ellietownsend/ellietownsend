# Iterative example
def findSubstringI(needle, haystack):
    i = 0 #set index for our loop
    while i < len(haystack): # to iterate through
        if haystack[i:i + len(needle)] == needle: #substring comparison
            return i
        i = i + 1
    return - 1

#Recursive example

# In this recursive string we initiate i in the arguments
def findSubStringR(needle, haystack, i = 0):
    # I need a base case, base case's start with an if
    # This one is cool because there are two base cases, one if we find it, one if we dont
    # No matter which happens we cant the recursive case to stop checking
    if i >= len(haystack):
        return - 1

    if haystack[i:i + len(needle)] == needle:
        return i
    else:
        return findSubStringR(needle, haystack, i + 1)

print(findSubStringR('cat', 'My cat is named Kat'))
print(findSubstringI('cat', 'My cat is named Kat'))



