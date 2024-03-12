##################################################
# Name: Ethan 
# Collaborators: 
# Estimate of time spent (hr): 0.5
##################################################

def to_obenglobish(word):
    """ Converts an English word into its Obenglobish equivalent.

    Inputs:
        word (string): word to be translated to Obenglobish
    Outputs:
        (string): the Obenglobish translation of the word
    """
    # Add your code below and remove this pass!
    vowels=["a","e","i","o","u"]
    new_word=""
    silent_vowels=["e"]
    for i in range (0,len(word)):
        if word[i] not in vowels:
            new_word+=word[i]
        elif word[i-1] in vowels and word[i] in vowels and i>0:
            new_word+=word[i]
        elif i+1==len(word) and word[i]==vowels[1]:
            new_word+=word[i]

        else:
            new_word+="ob"+word[i]

    return new_word




if __name__ == '__main__':
    # Some testing printouts for your use!
    print(f"to_obenglobish('english') gives {to_obenglobish('english')}.")
    print(f"to_obenglobish('gooiest') gives {to_obenglobish('gooiest')}.")
    print(f"to_obenglobish('amaze')   gives {to_obenglobish('amaze')}.")
    print(f"to_obenglobish('rot')     gives {to_obenglobish('rot')}.")
    print(to_obenglobish('hello'))
