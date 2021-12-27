# File: Project2.py
# Student: Anna Dougharty
# UT EID: amd5933
# Course Name: CS303E
# 
# Date Created: 4.12.21
# Date Last Modified: 4.12.21
# Description of Program: Substitution Cipher program that can take any cipher and encrypt and decrypt

import random

LCLETTERS = "abcdefghijklmnopqrstuvwxyz"

def isLegalKey(key):
    return(len(key) == 26 and all( [ch in key for ch in LCLETTERS]))

def makeRandomKey():
    lst = list(LCLETTERS)
    random.shuffle(lst)
    return ''.join(lst)

class SubstitutionCipher:

    def __init__(self, key = makeRandomKey()):
        self.key = key


    def getKey(self):
        return self.key

    def setKey(self, newkey):
        self.key = newkey
        return self.key

    def encryptText(self, plaintext, key, alphabet):
        keyMap = dict(zip(alphabet, key))
        return ''.join(keyMap.get(n.lower(), n) for n in plaintext)
        

    def decryptText(self, ciphertext, key, alphabet):
        keyMap = dict(zip(key, alphabet))
        return ''.join(keyMap.get(n.lower(), n) for n in ciphertext)


def main():
    cipher = SubstitutionCipher()
    command = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")
    while command != 'quit':
        if command.lower() == 'getkey':
            key = cipher.getKey()
            print('Current cipher key: ', key)

        if command.lower() == 'changekey':
            key = str(input("Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: "))
            while key != 'quit':
                if key == 'random':
                    newkey = makeRandomKey()
                    cipher.setKey(newkey)
                    print('New cipher key: ', newkey)
                    break
                elif isLegalKey(key) is True:
                    newkey = key
                    cipher.setKey(newkey)
                    print('New cipher key: ', newkey)
                    break
                elif isLegalKey(key) is False:
                    print("Illegal key entered. Try again!")
                    key = str(input("Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: "))    
                    

        if command.lower() == 'encrypt':
            plaintext = input('Enter a text to encrypt: ')
            ciphertext = cipher.encryptText(plaintext, cipher.getKey(), LCLETTERS)
            print('The encrypted text is:', ciphertext)

        if command.lower() == 'decrypt':
            ciphertext = input('Enter a text to decrypt: ')
            plaintext = cipher.decryptText(ciphertext, cipher.getKey(), LCLETTERS)
            print('The decrypted text is:', plaintext)

        else:
            print('Command not recognized. Try again!')
        
        command = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")
    print('Thanks for visiting!')
        
    
main()
