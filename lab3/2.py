#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

print(grams_to_ounces(100))  # 100 грамм = 2834.95231 унция


#2
def my_function(f):
    return (5/9)*(f-32)

f=float(input())
print(my_function(f))

#3
def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None, None 

heads = 35
legs = 94
chickens, rabbits = solve(heads, legs)
if chickens is not None and rabbits is not None:
    print(chickens)
    print(rabbits)
else:
    print("error")

#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [x for x in numbers if is_prime(x)]

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(filter_prime(nums))

#5
def permute(s, l, r):
    if l == r:
        print(''.join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]

def print_permutations():
    user_input = input("Enter a string: ")
    s_list = list(user_input)
    permute(s_list, 0, len(s_list) - 1)

print_permutations()

#6                                                                                                                                              def reverse(): 
    s = input()
    reversed_sentence = ' '.join(s.split()[::-1])
    return reversed_sentence

print(reverse())

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#8
def spy_game(nums):
    code = [0, 0, 7]
    i = 0
    for num in nums:
        if num == code[i]:
            i += 1
            if i == len(code):
                return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#9
import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

print(sphere_volume(5))

#10
def unique_elements(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

print(unique_elements([1, 2, 2, 3, 4, 4, 4, 5]))

#11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("madam"))

#12
def histogram(lst):
    for num in lst:
        print('*' * num)

histogram([4, 9, 7])

#13
import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

guess_the_number()