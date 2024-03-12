########################################
# Name:
# Collaborators: Alicia Robbins

# Estimated time spent (hr):
########################################

def largest_two():

    print("this program finds the two largest integers.")
    print("enter a blank line to stop")


    largest = 0
    secondlargest = 0 
    finished=False

    while not finished:
        number = input("?")
        if number != "":
            if int(number)>largest:
                secondlargest = largest
                largest=int(number)
            else:
                if int(number)>secondlargest:
                    secondlargest = int(number)
        else:
            finished= True

            print("the highest numebr is", largest)
            print("the second highest number is", secondlargest)


if __name__ == '__main__':
    largest_two()
