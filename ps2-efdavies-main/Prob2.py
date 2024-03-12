#====================================================
# Filename: Prob2.py 
# 
# Your name:Ethan davies
# Who did you work with (if anyone)?: alicia
# Estimate for time spent (in hrs)?: 1
#====================================================

word=""
# Define negate here
def negate(word):
    return "un"+str(word)


# Define intensify here

def intensify(word):
    return "plus"+str(word)

# Define reinforce here

def reinforce(word):
    return "super"+word





if __name__ == '__main__':
    # I've included the example in the description here for you to test against!
    print(negate("cold"))
    print(intensify("cold"))
    print(reinforce("cold"))
    print(intensify(negate("cold")))
    print(reinforce(intensify("cold")))
    print(reinforce(intensify(negate("good"))))
