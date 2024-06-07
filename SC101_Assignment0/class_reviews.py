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
    This program will print out the maximum, minimum, and average score of
    different classes based on the information provided by the user.
    """
    class_name = input('Which class? ')
    if class_name == EXIT:
        print('No class scores were entered')
    else:
        # Setting initial conditions before looping the score recording loop.
        min_001 = 10  # Recording the minimum of SC001 score. Starting with 10.
        max_001 = 0   # Recording the maximum of SC001 score. Starting with 0.
        sum_001 = 0   # Computing the summary of all SC001 scores. Starting with 0.
        num_001 = 0   # Counting the number of SC001 score. Starting with 0.
        min_101 = 10  # Recording the minimum of SC101 score. Starting with 10.
        max_101 = 0   # Recording the maximum of SC101 score. Starting with 0.
        sum_101 = 0   # Computing the summary of all SC101 scores. Starting with 0.
        num_101 = 0   # Counting the number of SC101 score. Starting with 0.
        while True:
            if class_name == EXIT:
                break
            elif class_name.upper() == 'SC001':    # Class SC001 database
                score_001 = int(input('Score: '))
                if score_001 >= max_001:
                    max_001 = score_001
                if score_001 <= min_001:
                    min_001 = score_001
                sum_001 += score_001
                num_001 += 1
            else:                                  # Class SC101 database
                score_101 = int(input('Score: '))
                if score_101 >= max_101:
                    max_101 = score_101
                if score_101 <= min_101:
                    min_101 = score_101
                sum_101 += score_101
                num_101 += 1
            class_name = input('Which class? ')  # Asking the user to enter the next class name.

        # The loop ends. Printing all the records of different classes based on their databases.
        print('=============SC001=============')
        # Checking whether the SC001 database has data.
        if num_001 == 0:
            print('No score for SC001')
        else:
            print('Max (001): ' + str(max_001))
            print('Min (001): ' + str(min_001))
            print('Avg (001): ' + str(sum_001 / float(num_001)))  # The average SC001 score.
        print('=============SC101=============')
        # Checking whether the SC101 database has data.
        if num_101 == 0:
            print('No score for SC101')
        else:
            print('Max (101): ' + str(max_101))
            print('Min (101): ' + str(min_101))
            print('Avg (101): ' + str(sum_101 / float(num_101)))  # The average SC101 score.


if __name__ == '__main__':
    main()
