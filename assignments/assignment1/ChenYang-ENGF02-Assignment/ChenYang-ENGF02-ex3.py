def fizzbuzz1(n):
    for i in range(1, n+1):
        if i % 15 is 0:
            print("FizzBuzz")
        elif i % 3 is 0:
            print("Fizz")
        elif i % 5 is 0:
            print("Buzz")
        else:
            print(n)
def fizzbuzz(n):
    for i in range(1, n):
        print(i%3//2*'fizz'+i%5//4*'buuz'or i+1)


fizzbuzz(100)
