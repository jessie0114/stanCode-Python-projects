"""
File: caesar.py
Name: Jessie
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program demonstrates the idea of caesar cipher.
    """
    secret_number = int(input("Secret number: "))
    ciphered_string = input("What’s the ciphered string? ")
    deciphered_string = decipher(ciphered_string, secret_number)
    print("The deciphered string is:", deciphered_string)


def decipher(ciphered_string, secret_number):
    new_alphabet = ''
    new_alphabet = ALPHABET[26-secret_number:] + ALPHABET[:26-secret_number]
    result = ''
    for i in range(len(ciphered_string)):
        ch = new_alphabet.find(ciphered_string[i].upper())
        if ciphered_string[i].isalpha():
            result = result + ALPHABET[ch]
        else:
            result = result + ciphered_string[i]
    return result






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
