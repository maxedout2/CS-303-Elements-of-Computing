# File: RecursiveFunctions.py
# Student: Anna Dougharty
# UT EID: amd5933
# Course Name: CS303E
# 
# Date Created:
# Date Last Modified: 
# Description of Program: 


def sumItemsInList(l):
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList(L[1:])

def countOccurencesInList(key, L):
    if L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurencesInList(key, L[1:])
    else:
        return countOccurencesInList(key, L[1:])

def addToN(n):
    if n<=0:
        return 0
    else:
        return n + addToN(n-1)

def findSumOfDigits(n):
    if n==0:
        return 0
    else:
        return n%10 + findSumOfDigits(n//10)

def decimalToBinary(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10 * (decimalToBinary(n//2))
#cant get this to do the string thing

def decimalToList(n):
    l=[]
    if n>0:
        num = str(n%10)
        l = decimalToList(n//10)
        l.append(num)
    return l

def isPalindrome(s):
    if s == "" or len(s)==1:
        return True
    else:
        return s[0]==s[-1] and isPalindrome(s[1:-1])

def findFirstUppercase(s):
    if len(s) == 0:
        return None
    elif s[0].isupper():
        return s[0]
    else:
        return findFirstUppercase(s[1:])

def findFirstUppercaseIndexHelper(s, index):
    if len(s)==0:
        return -1
    elif s[0].isupper():
        return index
    else:
        return findFirstUppercaseIndexHelper(s[1:],index+1)

def findFirstUppercaseIndex(s):
    return findFirstUppercaseIndexHelper(s,0)


    
