#######################################
# Name:Ethan
# Collaborators:Owen Mecklem
# Estimated time spent (hr):
#######################################

from english import ENGLISH_WORDS


# Part A
def contains_repeated_letters(word):
    """Returns True if the word contains more than one instance of any letter.

    Arguments:
        word (str): The word to check
    Returns:
        (bool): True or False depending on if the word contains duplicated letters
    """

    for i in range(len(word)-1):
        letter = word[i]
        for j in range(len(word)-1):
            letter2=word[j]
            if i!= j:
                if letter==letter2:
                    return True
    return False
    # Your turn!





# Part B
def longest_no_repeats():
    """Returns the longest word in the English dictionary without an repeated letters."""

    longest = ""
    for word in ENGLISH_WORDS:
        if contains_repeated_letters(word) == False:
            if len(word) > len(longest):
                longest = word
    return longest
    
    # Your turn!





if __name__ == '__main__':
    # Part A
    print(contains_repeated_letters("single"))
    print(contains_repeated_letters("repeating"))

    # Part B
    print(longest_no_repeats()) #Uncomment when you've finished Part B
