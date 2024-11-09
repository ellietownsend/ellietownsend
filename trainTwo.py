# How do call stacks " the stack " work?
'''They use a stack of frame objects'''
# What are frame objects?
'''They contain information about a single function call'''
# How do frame objects keep track?
'''They use a stack! When three functions are called each is added to the top, like a pancake, then moved off as they are completed.'''
# Whenever we call a function we add a frame object to the stack which contains a function, it's arguments (no args if there are none), and local variables (can have same name).
# Automatically implemented in the background

# What are stacks?
'''Stacks store multiple values like a list, but it limits how you can remove and add items.'''
# Adding and removing to a stack is called pushing (append) and popping (pop).
# The top of the stack is where we can add and remove items from (think of items like pancakes, it would be gross to try to remove the bottom one... sticky pancake)
# Examples of usage: Web browsers back button
# Follow a last in first out structure


def a():
    print('a() was called')
    # First thing we run into, print
    b()
    # Go to function B
    print("a() is returning\n")
    # Final print


def b():
    print('b() was called')
    # First thing we run into, print
    c()
    # Go to function C
    print("b() is returning")
    #Where we left off before we got told to go to C, Go to A


def c():
    print('c() was called')
    # First thing we run into, print
    print("c() is returning")
    #After three have printed, this prints then we go back to where C was called (function B)

a()
#Activate Everything

def d():
    spam = 'ant'
    print('spam is ' + spam)
    e()
    print("spam is " + spam)

def e():
    spam = 'bobcat'
    print('spam is ' + spam)
    f()
    print("spam is " + spam)
    #each spam is seen differently on the frame object stack because they are local variables

def f():
    spam = 'frog'
    print('spam is ' + spam)
    print("spam is " + spam)

d()