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
    # Asking the user to enter the class name.
    class_name = input('Which class? ')
    # Checking whether the 1st input class name is '-1' (EXIT).
    if class_name == EXIT:  # True. The program ends with no class scores.
        print('No class scores were entered')
    else:                   # False. The program has at least 1 class scores.
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
                break  # When the input class name is '-1' (EXIT), the loop ends.
            # Recording input scores based on class name.
            # Turning the class name into uppercase to make the program be case-insensitive.
            elif class_name.upper() == 'SC001':    # Class SC001 database.
                score_001 = int(input('Score: '))  # Asking the user to enter a score.
                if score_001 >= max_001:  # Comparing new score with the maximum score.
                    max_001 = score_001   # New score is larger. Reassigning the maximum score.
                if score_001 <= min_001:  # Comparing new score with the minimum score.
                    min_001 = score_001   # New score is smaller. Reassigning the minimum score.
                sum_001 += score_001      # Adding new score to the summary of all SC001 scores.
                num_001 += 1              # Adding one to the number of SC001 score.
            else:                                  # Class SC101 database.
                score_101 = int(input('Score: '))  # Asking the user to enter a score.
                if score_101 >= max_101:  # Comparing new score with the maximum score.
                    max_101 = score_101   # New score is larger. Reassigning the maximum score.
                if score_101 <= min_101:  # Comparing new score with the minimum score.
                    min_101 = score_101   # New score is smaller. Reassigning the minimum score.
                sum_101 += score_101      # Adding new score to the summary of all SC101 scores.
                num_101 += 1              # Adding one to the number of SC101 score.
            class_name = input('Which class? ')  # Asking the user to enter the next class name.

        # The loop ends. Printing all the records of different classes based on their databases.
        print('=============SC001=============')
        # Checking whether the SC001 database has data.
        if num_001 == 0:    # True. No score for SC001.
            print('No score for SC001')
        else:   # False. The SC001 database has scores.
            print('Max (001): ' + str(max_001))
            print('Min (001): ' + str(min_001))
            print('Avg (001): ' + str(sum_001 / float(num_001)))  # The average SC001 score.
        print('=============SC101=============')
        # Checking whether the SC101 database has data.
        if num_101 == 0:    # True. No score for SC101.
            print('No score for SC101')
        else:   # False. The SC101 database has scores.
            print('Max (101): ' + str(max_101))
            print('Min (101): ' + str(min_101))
            print('Avg (101): ' + str(sum_101 / float(num_101)))  # The average SC101 score.


if __name__ == '__main__':
    main()
