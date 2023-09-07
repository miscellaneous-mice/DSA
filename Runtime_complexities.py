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
