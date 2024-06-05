"""
File: complement.py
Name: Jessie
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program will turn 'A' into 'T', 'T' into 'A', 'C' into 'G', and 'G' into 'C'.
    When DNA is empty, it will show 'DNA strand is missing. '.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    if dna == '':
        return 'DNA strand is missing. '
    else:
        ans=''
        for i in range(len(dna)):
            ch = dna[i]
            if ch == 'A':
                ans += 'T'
            elif ch == 'T':
                ans += 'A'
            elif ch == 'C':
                ans += 'G'
            elif ch == 'G':
                ans += 'C'
        return ans





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
