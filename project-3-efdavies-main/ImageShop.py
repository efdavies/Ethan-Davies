######################################################################
# Name: Ethan
# Collaborators (if any): 
# Section leader's name: Olivia
# List of extensions made (if any): 
######################################################################

"""
This program is the starter file for the ImageShop application, which
implements the "Load" and "Flip Vertical" buttons.
"""

from filechooser import choose_input_file
from pgl import GWindow, GImage, GRect, GCompound
from button import GButton
from GrayscaleImage import create_grayscale_image, luminance


# Constants

GWINDOW_WIDTH = 900
GWINDOW_HEIGHT = 500
BUTTON_WIDTH = 125
BUTTON_HEIGHT = 20
BUTTON_MARGIN = 10
BUTTON_BACKGROUND = "#CCCCCC"

# Derived constants

BUTTON_AREA_WIDTH = 2 * BUTTON_MARGIN + BUTTON_WIDTH
IMAGE_AREA_WIDTH = GWINDOW_WIDTH - BUTTON_AREA_WIDTH

# The image_shop application

def image_shop():
    def add_button(label, action):
        """
        Adds a button to the region on the left side of the window
        label is the text that will be displayed on the button and
        action is the callback function that will be run when the
        button is clicked.
        """
        x = BUTTON_MARGIN
        y = gw.next_button_y
        button = GButton(label, action)
        button.set_size(BUTTON_WIDTH, BUTTON_HEIGHT)
        gw.add(button, x, y)
        gw.next_button_y += BUTTON_HEIGHT + BUTTON_MARGIN
    
    def set_image(image):
        """
        Sets image as the current image after removing the old one.
        """
        if gw.current_image is not None:
            gw.remove(gw.current_image)
        gw.current_image = image
        x = BUTTON_AREA_WIDTH + (IMAGE_AREA_WIDTH - image.get_width()) / 2
        y = (gw.get_height() - image.get_height()) / 2
        gw.add(image, x, y)

    def load_button_action():
        """Callback function for the Load button"""
        filename = choose_input_file()
        if filename != "":
            set_image(GImage(filename))

    def flip_vertical_action():
        """Callback function for the Flip Vertical button"""
        if gw.current_image is not None:
            set_image(flip_vertical(gw.current_image))

    def flip_horizontal_action():
        """Callback function for the Flip Horizontal button"""
        if gw.current_image is not None:
            set_image(flip_horizontal(gw.current_image))

    def rotate_left_action():
        if gw.current_image is not None:
            set_image(rotate_left(gw.current_image))

    def rotate_right_action():
        if gw.current_image is not None:
            set_image(rotate_right(gw.current_image))

    def grayscale():
        if gw.current_image is not None:
            set_image(create_grayscale_image(gw.current_image))

    def greenscreen_action():
        if gw.current_image is not None:
            filename = choose_input_file(dir="images")
            if filename != "":
                set_image(greenscreen(gw.current_image, GImage(filename)))

    def luminance_action():
        if gw.current_image is not None:
            set_image(luminance1(gw.current_image))

    def invert_color_action():
        if gw.current_image is not None:
            set_image(color_negative(gw.current_image))

    def overlay_action():
        """Callback function for the Overlay button"""
        if gw.current_image is not None:
            filename = choose_input_file(dir="images")
            if filename != "":
                set_image(overlay(gw.current_image, GImage(filename)))
    def oval_action():
        if gw.current_image is not None:
            set_image(clip_oval(gw.current_image))
    def red_eye_action():
        if gw.current_image is not None:
            set_image(red_eye(gw.current_image))
        
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    button_area = GRect(0, 0, BUTTON_AREA_WIDTH, GWINDOW_HEIGHT)    
    button_area.set_filled(True)
    button_area.set_color(BUTTON_BACKGROUND)
    gw.add(button_area)
    gw.next_button_y = BUTTON_MARGIN
    gw.current_image = None
    add_button("Load", load_button_action)
    add_button("Flip Vertical", flip_vertical_action)
    add_button("Flip Horizontal", flip_horizontal_action)
    add_button("Rotate Left", rotate_left_action)
    add_button("Rotate Right", rotate_right_action)
    add_button("Grayscale", grayscale)
    add_button("Greenscreen", greenscreen_action)
    add_button("Luminance", luminance_action)
    add_button("Invert color", invert_color_action)
    add_button("Overlay", overlay_action)
    add_button("Oval", oval_action)
    add_button("Red Eye", red_eye_action)

# Creates a new GImage from the original one by flipping it vertically.

def flip_vertical(image):
    array = image.get_pixel_array()
    return GImage(array[::-1])

def flip_horizontal(image):
    array = image.get_pixel_array()
    for i in range(len(array)): #loops through the list of all of the rows
        array[i]=array[i][::-1] #fliping the ith row in the array
    return GImage(array) #returning the array after we have done all of the flips to each row in the image

def rotate_left(image):
    array = image.get_pixel_array()
    array2=[]

    for j in range(len(array[0])): 
        row=[]
        for i in range(len(array)): #looping through the i and j components of the pixel array
            row.append(array[i][j]) # adding the aray with fliped i and j components so that the image inverts
        array2.append(row)          # adding each row to a new array
    return flip_vertical(GImage(array2)) # fliping vertical because array 2 is upside down and doesnt turn left as it is

def rotate_right(image): #same as rotate left function
    array = image.get_pixel_array()
    array2=[]

    for j in range(len(array[0])): 
        row=[]
        for i in range(len(array)):
            row.append(array[i][j])
        array2.append(row)
    return flip_horizontal(GImage(array2)) #horizontal flip because inverted array does not turn rigth as it is

def greenscreen(image1, image2):
    array1 = image1.get_pixel_array() #two pixel arrays
    array2 = image2.get_pixel_array()
    height1 = len(array1)
    height2 = len(array2)
    width1 = len(array1[0])
    width2 = len(array2[0])
    for i in range(min(height1, height2)):
        for j in range(min(width1, width2)): #looping through both images i and j components in their arrays
            pix= array2[i][j] 
            r= GImage.get_red(pix)
            g = GImage.get_green(pix)
            b= GImage.get_blue(pix)
            if g<2*max(r,b): #if we find any green in the picture that is lexx than two times the maximim of red and blue pixels in the image
                array1[i][j]=array2[i][j] #we replace those green pixels with the array of pixels from image 1
    return GImage(array1)

def create_histogram_array(imax, data):
    array=[]
    for i in range((imax)):
        count= 0
        for j in range(len(data)):
            if i==data[j]:
                count+=1
        array.append(count)
    return array  


def create_histogram_graph(array, width, height):
    x = width/len(array)
    y = height/max(array)

    graph = GCompound()
    for i in range(len(array)):
        bar = GRect(x*i, height - y*array[i], x, y*array[i])
        bar.set_fill_color("red")
        bar.set_filled(True)
        graph.add(bar)
    return graph

def luminance1(image):
    array = image.get_pixel_array()
    lumlist=[]
    for i in range(len(array)):
        for j in range(len(array[0])): #looping through i and j in the array
            pix = array[i][j] 
            lumlist.append(luminance(pix)) # creating a list with the original luminance of each pixel
    array1 = create_histogram_array(257, lumlist) # creating a histogram with these values just appended
    chist = cumulative_histogram(array1) # then a cumulative histogram of the previous historgam
    for i in range(len(array)):
        for j in range(len(array[0])):
            pix = array[i][j]
            newlum=round((255*chist[luminance(pix)])/(len(array)*len(array[0]))) #equation which changes the luminance of each pixel
            array[i][j] = GImage.create_rgb_pixel(newlum, newlum,newlum) #looping through and creating a new array with the new luminance values of each pixel
    return GImage(array)
    #WIDTH, HEIGHT = 800, 600
    #gw = GWindow(WIDTH, HEIGHT)
    #chist = cumulative_histogram(array)
    #graph = create_histogram_graph(chist, WIDTH, HEIGHT)
    #gw.add(graph)


def cumulative_histogram(hist):
    chist=[0 for i in range(len(hist))]
    total=0
    for i in range(len(hist)):
        total+=hist[i]
        chist[i]=total
    return chist



def red_eye(image):
    array = image.get_pixel_array()
    for i in range(len(array)):
        for j in range(len(array[0])):
            pix= array[i][j]
            r= GImage.get_red(pix)
            g = GImage.get_green(pix)
            b= GImage.get_blue(pix)
            if r>2*max(g,b):
                r=max(g,b)
            array[i][j]=GImage.create_rgb_pixel(r,g,b)
    return GImage(array)

def color_negative(image):
    array = image.get_pixel_array()
    for i in range(len(array)):
        for j in range(len(array[0])):
            pix = array[i][j]
            r = GImage.get_red(pix)
            g = GImage.get_green(pix)
            b = GImage.get_blue(pix)
            array[i][j] = GImage.create_rgb_pixel(255-r, 255-g, 255-b) #changing the color by just reversing the value of rgb
    return GImage(array)

def overlay(image1, image2):
    """Creates a new GImage by interleaving the pixels of the two given images"""
    array1 = image1.get_pixel_array()
    array2 = image2.get_pixel_array()
    height1 = len(array1)
    height2 = len(array2)
    width1 = len(array1[0])
    width2 = len(array2[0])
    for i in range(min(height1, height2)):
        for j in range(min(width1, width2)): #function replaces everyother pixel with the new image put on top
            if (i+j) % 2 == 1:
                array1[i][j] = array2[i][j]
    return GImage(array1)

def clip_oval(image):
    """Creates a new GImage by erasing any pixels outside the oval."""

    def inside_oval(i, j):
        return (i - h2) ** 2 / h2 ** 2 + (j - w2) ** 2 / w2 ** 2 < 1.0

    array = image.get_pixel_array()
    height = len(array)
    width = len(array[0])
    h2 = height / 2
    w2 = width / 2
    for i in range(height):
        for j in range(width):
            if not inside_oval(i, j):
                array[i][j] = GImage.create_rgb_pixel(255, 255, 255)
    return GImage(array)


# Startup code

if __name__ == "__main__":
    image_shop()
