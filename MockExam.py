# CS 303E Mock Exam (homework 6)
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Sphere Surface Area
def sphereSurfaceArea():
    # write your solution to problem 1 here
    r = float(input())
    if r < 0:
        print("Negative radius entered")
    else:
        s = 4*(3.141592653589793)*(r**2)
        print("%.2f"%s)
    pass    


# Problem 2: Make Uppercase
def makeUppercase():
    # write your solution to problem 2 here
    ch = input()
    if (ord(ch) >= 65 and ord(ch) <= 90):
        print(ch)
    elif (ord(ch) >= 97 and ord(ch) <= 122):
        number = int(ord(ch)) - 32
        upper = chr(number)
        print(upper)
    else:
        print(ch)
    pass


# Problem 3: Sum Series
def sumSeries():
    # write your solution to problem 3 here
    n = int(input())
    summ=0
    for n in range(n+1):
        x = (n-1)*n
        summ = summ +x
    print(summ)
    pass


# Problem 4: Sort Three Integers
def sortThreeIntegers():
    # write your solution to problem 4 here
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    if num1<num2:
        if num1<num3:
            if num2<num3:
                print(num1, num2, num3)
            else:
                print(num1, num3, num2)
        else:
            print(num3, num1, num2)
    else:
        if num2<num3:
            if num1<num3:
                print(num2, num1, num3)
            else:
                print(num2, num3, num1)
        else:
            print(num3, num2, num1)
    pass



# Problem 5: Sum Positive Floats
def sumPositiveFloats():
    # write your solution to problem 5 here
    summ = 0
    num = 1
    while num != 0:
        num = float(input())
        if num > 0:
            summ = summ + num
    print("%.3f"%summ)
    pass


# Problem 6: Print Squared Table
def printSquaredTable():
    # write your solution to problem 6 here
    n = int(input())
    print(f'{"n":>3}{"n**2":>10}')
    print("-------------")
    for n in range(1,n+1):
        print(f'{n:>3}{n**2:>10}')
    pass


# Problem 7: Largest Square
def largestSquare():
    # write your solution to problem 7 here
    n = int(input())
    num=[]
    for k in range(1, n+1):
        if k**2 <= n:
            num.append(k)
    print(str(max(num)))
    pass


# Problem 8: Collatz Conjecture
def collatzConjecture():
    # write your solution to problem 8 here
    n = int(input())
    count = 1
    while n != 1:
        if n%2 == 0:
            n = 0.5*n
        else:
            n = 3*n+1
        count += 1
    print(count)   
    pass

