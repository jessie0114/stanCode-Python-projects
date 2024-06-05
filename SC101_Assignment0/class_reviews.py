"""
File: class_reviews.py
Name: Jessie
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1


def main():
    """
    This program will find the max, min and avg of SC001 and SC101.
    """

    sc = input('Which class? ').upper()

    if sc == str(EXIT):
        print('No class scores were entered')

    else:
        max_score001 = 0
        min_score001 = 999999999
        counts001 = 0
        total_score001 = 0

        max_score101 = 0
        min_score101 = 999999999
        counts101 = 0
        total_score101 = 0

        while True:
            if sc == str(EXIT):
                break
            else:
                if sc == 'SC001':
                    score001 = int(input('Score: '))
                    if score001 > max_score001:
                        max_score001 = score001
                    if score001 < min_score001:
                        min_score001 = score001
                    counts001 += 1
                    total_score001 += score001
                if sc == 'SC101':
                    score101 = int(input('Score: '))
                    if score101 > max_score101:
                        max_score101 = score101
                    if score101 < min_score101:
                        min_score101 = score101
                    counts101 += 1
                    total_score101 += score101
                sc = input('Which class? ').upper()

        if counts001 > 0:
            avg_score001 = total_score001 / counts001
            print('=' * 13 + 'SC001' + '=' * 13)
            print('Max(001): ' + str(max_score001))
            print('Min(001): ' + str(min_score001))
            print('Avg(001): ' + str(avg_score001))
        if counts101 > 0:
            avg_score101 = total_score101 / counts101
            print('=' * 13 + 'SC101' + '=' * 13)
            print('Max(101): ' + str(max_score101))
            print('Min(101): ' + str(min_score101))
            print('Avg(101): ' + str(avg_score101))
        else:
            print('No class scores were entered')





# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
