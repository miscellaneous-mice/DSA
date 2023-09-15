'''
Big O is the worst case scenario that a code can perform
Eg : Searching through a forloop

our list is = [1, 2, 3, 4, 5, 6 ,7, 8]

Our best case scenario is finding element : 1 -> Big O (O)
Our worst case scenario is finding element : 8 -> Theta (θ)
Average case scenario is finding elements like : 4 or 5 -> Omeage (Ω)

'''

# Constant time complexity -> O(1) -> most efficient
print("Constant time complexity")
def multiply_number(n): # Only one operation is performed hence O(1)
    return n*n

print(multiply_number(2))

# Other is picking a random card from a deck of cards -> O(1)


# Linear time complexity -> O(n) -> Time complexity will grow with size of i/p
print("\nLinear time complexity")
def print_items(n): # Ten operations performed -> O(n)
    for i in range(n):
        print(i)

print_items(3) # -> O(10)

# Other example is finding a card in deck of cards -> How large the deck is so much time it takes to find the card


# Drop constants
print("\nDrop constants")
def print_items(n): # Has 2 O(n) time complexities -> O(2n)
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

# But we drop the constant O(2n) to O(n) to simplify Big O notation
print_items(3)

'''
- Also possible that O(n) might be faster than O(1) for specific inputs

- We ignore hardware specs while verfying a time complexity of a code

- Different algorithms that does the same operation have different constants
  eg: a*(b-c) or a*b - a*c

- As n -> ∞ constants don't really play a big part
'''

# O(n^2) type complexities
print("\nO(n^2) time complexities")

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(3) # -> runs 25 times O(5^2)

# Other examples searching all the occurances of a card (take 3), hence it will take 4 searches of entire deck

print("\n")
def print_items(n): # -> O(n^3) but we still write it as O(n^2) complexity only
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

print_items(3) # -> O(8) very inefficient

print("\nNon dominant terms")

# Here dominant is n^2 and non dominant is n. Hence we drop non dominant terms
def print_items(n): # -> O(n^2 + n) # But we drop n hence it becomes O(n^2) time complexity
    for i in range(n): # -> O(n^2) complexity
        for j in range(n):
            print(i,j)
    
    for k in range(n): # -> O(n) complexity
        print(k)

print_items(3)

'''
O(logn) time complexity

We have to find number 1
step 1 : [1, 2, 3, 4, 5, 6, 7, 8]

Divide the array into 2 parts and discard the array that doesn't contain 1
step 2 : [1, 2 ,3 ,4] and discard [5 ,6 ,7 ,8]

Again divide the array and 2 parts & discard the array that doesn't contain 1
step 4 : [1, 2] and discard [3 ,4]

Do it again. Until we finally find the number
step 5 : [1] and discard [2] -> found the number 1

It took 3 steps to find 1 in a 8 element array

Hence number of element = 2^number of steps it takes to find the no.
Here, 2^3 = 8

We divide the array into 2 every step. In total 3 steps to find the element
in a 8 element array.

Convert this into logarithmic form
log2(8) = 3. i.e., log(8) base 2 = 3 (Used to see number of steps to find a element)

For million items 
log2(1,048,576) = 20, Hence it takes 20 steps to find the element in array containing million elements
'''

print("\nO(n) space complexity")
def sum(n): # O(n) space complexity
    if n <=0:
         return 0
    return n + sum(n-1)

print(sum(3))
'''
To get sum(3), stack stores function values sum(2), sum(1) in stack as it 
is recursive in nature. Hence it should know what the previous values were.

Here to get sum(3) we need sum(2), if we need sum(2) we need sum(1), if we
need sum(1) we need sum(0).

Here there is no update of n, just storage of function values.

return 0 just exits the function as there is no recursive call again.
'''

print("\nO(1) space complexity")

def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total=total + pair_sum(i, i+1)
    return total

def pair_sum(a, b):
    return a+b

print(pair_sum_sequence(3))
'''
Doesn't store previous function value in each loop as, when pair_sum is 
called the previous memory gets erased from stack and new function value is
stored.

To perform total=total+pair_sum(i, i+1). Here all the values are present
hence no previous values are remember, even total is just updated to new
value in each forloop, not stored.
'''

print("\nAdd vs Multiply")
def print_items(a ,b): # Time complexity is O(a+b)
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

print("\nAdd vs Multiply")
def print_items(a ,b): # Time complexity is O(a*b)
    for i in range(a):
        for j in range(n):
            print(i, j)


print("\nFinding time complexity of a code")
import random
def findBiggestNumber(sampleArray): 
    biggestNumber = sampleArray[0] # O(1)                            |
    for index in range(1, len(sampleArray)): # O(n)          |
        if sampleArray[index] > biggestNumber: # O(1) | O(1) | O(n)  | O(n)
            biggestNumber = sampleArray[index] # O(1) | 
    return biggestNumber # O(1)                                      |

random_array = list(random.sample(population=range(50), k=40))
print(findBiggestNumber(random_array))

'''
Hence the function is O(n) time complexity
'''
