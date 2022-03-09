def name_age(name, age):
    print("Hello", name,". Your age is:", age)
    return " "

x = name_age("Marina", 19)
print(x)


string1 = "Marina"
z = 19
concatString = string1 + str(z)
print(concatString)


def swap_integers(X,Y):
    temp = X
    X = Y
    Y = temp
    print("After swapping numbers", (X, Y))
num1 = input("Please Enter the first number:")
num2 = input("Please enter the second number:")
print("Before swapping numbers", (num1, num2))
swap_integers(num1, num2)
# habe die input function noch nicht richtig verstanden

def check_numbers(num1, num2):
    if (num1 % 6 == 0 or num2 % 6 == 0) and (num1 % 10 == 0 and num2 % 10 == 0):
        print("True")
    else:
        print("False")

check_numbers(6, 10)


def sum_up(num1, num2):
    if num2 < num1:
        return "zero"
    elif num1 and num2 < 0:
        return "zero"
    else:
        result = sum(range(num1, num2 +1))
        return result
print(sum_up(3,9))


def circle_area(r1, r2, r3):
    pi = 3.14
    a1 = pi * r1
    a2 = pi * r2
    a3 = pi * r3
    print("a1 =", a1)
    print("a2 =", a2)
    print("a3 =", a3)
    print("Area as combined integer =",a1 + a2 + a3)
# ergebnis ist kein integer ?
circle_area(1,2,3)


def check_string(text):
    if text.lower().startswith("a") or text.lower().endswith("a"):
        print("True")
    else:
        print("False")
check_string("text")


def triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print(" ")
triangle(5)