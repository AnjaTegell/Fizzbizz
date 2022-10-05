print("Welcome to fizzbuzz game!")

x = int(input("Enter a number between 1 and 100: "))
if x > 100:
        print("Pick a smaller number")

number = 1
while number <= x:
    print(number)
    number = number + 1
    if number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3==0 and number % 5 == 0:
        print("fizzbuzz")
    else:
        print(number)
