alist = list(range(0, 1701, 17))

[17 * element for element in range(101)]
# list comprehension
# starts with a bracket
# new element looks like? (17 * element)
# for
# variable in sequence (element in range(101)
[5 for element in range(10)]
# prints 10 5s in a list

[17 * element for element in range(10) if element % 2]
#prints odd numbers between 1 and 10 multiplied by 17

def color(n):
    """
    turns a number into a color
    """
    return 'red' if n % 2 else 'green'
# returns red if n is odd, returns green if n is even

# <consequent> if <test> else <alternative>
[[2, 1, 3], [5, 4, 7]]
# 2 1 3
# 5 4 7
#transposed =
# 2 5
# 1 4
# 3 7

# transpose a matrix means to rotate over its first diagonal
# has no purpose (great)
# used to multiply matrices
# languages do it for you (yay)
# in matlab, A transposed is A'

# WILL BE USEFUL FOR PACKING PROBLEM!!!!!!!!!!!!!
#nested for loop
#  swap row and column variables
# for var in _:
#   for var2 in _:
#       code

#Packing project:
# Teams of 1, 2, and 3.
# only work within teams
# choose teams carefully