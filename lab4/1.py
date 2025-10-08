#1
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

N = int(input())
for square in square_generator(N):
    print(square)


#2
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())
print(", ".join(map(str, even_generator(n))))

#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
print(list(divisible_by_3_and_4(n)))

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Example usage:
a = int(input("a="))
b = int(input("b="))

for square in squares(a, b):
    print(square)

#5
def numbers(n):
    for i in range(n,-1,-1):
        yield i

n = int(input())
for num in numbers(n):
    print(num)

    