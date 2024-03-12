##################################################
# Name:Ethan
# Collaborators:
# Estimate of time spent (hr): .8
##################################################

def create_histogram_array(imax, data):
    """ Computes a histogram of the entries of data given imax different bins (starting
    from index 0 and going up to imax - 1).

    Inputs:
        imax (integer): number of possible different elements to count
        data (list of integers): the list of data to compute a histogram for
    Outputs:
        (list of integers): the histogram array
    """
    array=[]
    for i in range((imax)):

        count= 0
        for j in range(len(PI_DIGITS)):
            if i==PI_DIGITS[j]:
                count+=1
        array.append(count)
    return array       
        
        
def create_cumulative_histogram_array(data):
    array=[]
    for i in range(len(data)):
        add=sum(data[:i+1])
        array.append(add)
    return array       


def print_histogram(array):
    """ Prints the counts of a histogram given by array to the screen. 

    Inputs:
        array (list of integers): a histogram array
    Outputs:
        None
    """
    for i in range(len(array)):
        print(i,":",array[i]*"* ")
        



def create_histogram_graph(array, width, height):
    """ Creates and returns a GCompound wherein GRects have been used to represent
    the amount in each histogram index.

    Inputs:
        array (list of integers): a histogram array
        width (integer): the desired width of the GCompound
        height (integer): the desired height of the GCompound
    Outputs:
        (GCompound): a single GCompound with the necessary rectangles added
    """
    from pgl import GCompound, GRect
    x = width/len(array)
    y = height/max(array)

    graph = GCompound()
    for i in range(len(array)):
        bar = GRect(x*i, height - y*array[i], x, y*array[i])
        bar.set_fill_color("red")
        bar.set_filled(True)
        graph.add(bar)
    return graph




def test_create_histogram_graph():
    """ Tests the create_histogram_graph function """
    from pgl import GWindow
    WIDTH, HEIGHT = 800, 600
    gw = GWindow(WIDTH, HEIGHT)
    PI_DIGITS = [8,7,8,6,8,10,4,9,6,9,7,8]
    array = create_histogram_array(10, PI_DIGITS)
    graph = create_histogram_graph(array, WIDTH, HEIGHT)
    gw.add(graph)


        



if __name__ == '__main__':
    # Some testing printouts for your use!
    PI_DIGITS = [8,7,8,6,8,10,4,9,6,9,7,8]
    array = create_histogram_array(11, PI_DIGITS)
    print(array)
    print_histogram(array) # uncomment once you have defined print_histogram
    test_create_histogram_graph() # uncomment once you have defined create_histogram_graph
    print(create_cumulative_histogram_array(array))
