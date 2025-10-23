#1
from functools import reduce

def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst, 1)

nums = [2, 3, 4, 5]
print("Product:", multiply_list(nums))


#2
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("Upper case letters:", upper)
    print("Lower case letters:", lower)

s = input("Enter a string: ")
count_case(s)

#3
def is_palindrome(s):
    return s == s[::-1]

s = input("Enter a string: ")
print("Palindrome:", is_palindrome(s))

#4
import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    print(f"Square root of {number} after {delay} milliseconds is {math.sqrt(number)}")

num = int(input("Enter number: "))
delay = int(input("Enter delay in milliseconds: "))
delayed_sqrt(num, delay)

#5
def all_true(tpl):
    return all(tpl)

tpl = (True, True, False)
print("All elements are true:", all_true(tpl))



