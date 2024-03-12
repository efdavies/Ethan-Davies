#====================================================
# Filename: Prob3.py
# 
# Your name: Ethan Davies
# Who did you work with (if anyone)?:
# Estimate for time spent (in hrs)?: 1
#====================================================


def print_divisible_by_six_or_seven():
    """
    Prints all the numbers between 1 and 100 which are evenly divisible by 6 or 7,
    but not both. One number printed per line, and nothing is returned.
    """
    # Add your code here!
for i in range(100):
    if (i % 6 == 0 or i % 7 == 0) and not (i % 6 == 0 and i % 7 == 0):
        print(i)


def list_divisible_by_six_or_seven():
    for i in range(100):
        if (i % 6 == 0 or i % 7 == 0):
            print(i)










if __name__ == '__main__':
    print('Result of print_divisible_by_six_or_seven:')
    print(print_divisible_by_six_or_seven)
    print('Result of list_divisible_by_six_or_seven:') # You can uncomment this once you get to Part B
    print(list_divisible_by_six_or_seven(1,150)) # You can uncomment this once you get to Part B


