############################################################
# Name:
# Name(s) of anyone worked with:
# Est time spent (hr):
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel, GPolygon
import random

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

gw = GWindow(WIDTH, HEIGHT)

def mountain():
    def create_triangle(b, h):
        tri = GPolygon()
        tri.add_vertex(-b / 2, h / 2)
        tri.add_vertex(b / 2, h / 2)
        tri.add_vertex(0, -h / 2)
        return tri

    triangle = create_triangle(300, 200)
    triangle.set_filled(True)
    triangle.set_color("green")
    gw.add(triangle, 600, 200)

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    
    
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!
    def Sunset():
        darkest5= GRect(0, 0, 600,(5*HEIGHT)/10)
        darkest5.set_fill_color("silver")
        darkest5.set_filled(True)
        darkest5.set_line_width(0)
        gw.add(darkest5)
        darkest4= GRect(0, 0, 600,(4*HEIGHT)/10)
        darkest4.set_fill_color("#9DBBD8")
        darkest4.set_filled(True)
        darkest4.set_line_width(0)
        gw.add(darkest4)

        darkest3= GRect(0, 0, 600,(3*HEIGHT)/10)
        darkest3.set_fill_color("#B09CFF")
        darkest3.set_filled(True)
        darkest3.set_line_width(0)
        gw.add(darkest3)
        
        darkest2= GRect(0, 0, 600,(2*HEIGHT)/10)
        darkest2.set_fill_color("#8C54D0")
        darkest2.set_filled(True)
        darkest2.set_line_width(0)
        gw.add(darkest2)

        darkest= GRect(0, 0, 600,HEIGHT/10)
        darkest.set_fill_color("#622d90")
        darkest.set_filled(True)
        darkest.set_line_width(0)
        gw.add(darkest)
        
    def red_boat():

        pole= GRect(395, 430, 10,20)
        pole.set_fill_color("black")
        pole.set_filled(True)
        pole.set_line_width(0)
        gw.add(pole)

        deck= GRect(355, 450, 90,25)
        deck.set_fill_color("black")
        deck.set_filled(True)
        deck.set_line_width(0)
        gw.add(deck)
        def create_triangle(b, h):
            tri = GPolygon()
            tri.add_vertex(-b / 2, h / 2)
            tri.add_vertex(b / 2, h / 2)
            tri.add_vertex(0, -h / 2)
            return tri

        triangle = create_triangle(70, 70)
        triangle.set_filled(True)
        triangle.set_color("red")
        gw.add(triangle, 400, 400)




    def sun(): # its actually the moon but I was originally making it a sun
        sun = GOval(WIDTH/2-75, HEIGHT/2-275, 150, 150)
        sun.set_fill_color("#FEFCD7")
        sun.set_filled(True)
        sun.set_line_width(0)
        gw.add(sun)

    def barrier(): #gray barrier dividing the city and the water
        bar= GRect(0, 300, 600,50)
        bar.set_fill_color("#969696")
        bar.set_filled(True)
        bar.set_line_width(0)
        gw.add(bar)

    def ocean():
        ocean= GRect(0, 350, 600,300)
        ocean.set_fill_color("midnightblue")
        ocean.set_filled(True)
        ocean.set_line_width(0)
        gw.add(ocean)
    
    def buildings():
        for i in range (9):
                building= GRect(i*60+10*i, 300, 50, random.randint(-200, -100))
                building.set_filled(True)
                building.set_line_width(0)
                gw.add(building)

    def lights():
            for i in range (9):
                light= GLine(60+(WIDTH/10)*i,275,60+(WIDTH/10)*i,300)
                light.set_color("gray")
                light.set_line_width(5)
                gw.add(light)
                sun = GOval(56+60*i, 270,10,10)
                sun.set_fill_color("orange")
                sun.set_filled(True)
                sun.set_line_width(0)
                gw.add(sun)
    
    def stars():
        for i in range (100):
            stars=GOval(random.randint(5,595 ), random.randint(5, 200),2,2)
            stars.set_fill_color("white")
            stars.set_filled(True)
            stars.set_line_width(0)
            gw.add(stars)
    
    def pink_boat():

        pole= GRect(195, 480, 10,20)
        pole.set_fill_color("black")
        pole.set_filled(True)
        pole.set_line_width(0)
        gw.add(pole)

        deck= GRect(155, 500, 90,25)
        deck.set_fill_color("black")
        deck.set_filled(True)
        deck.set_line_width(0)
        gw.add(deck)
        def create_triangle(b, h):
            tri = GPolygon()
            tri.add_vertex(-b / 2, h / 2)
            tri.add_vertex(b / 2, h / 2)
            tri.add_vertex(0, -h / 2)
            return tri

        triangle = create_triangle(70, 70)
        triangle.set_filled(True)
        triangle.set_color("pink")
        gw.add(triangle, 200, 450)

    def orange_boat():

        pole= GRect(95, 380, 10,20)
        pole.set_fill_color("black")
        pole.set_filled(True)
        pole.set_line_width(0)
        gw.add(pole)

        deck= GRect(55, 400, 90,25)
        deck.set_fill_color("black")
        deck.set_filled(True)
        deck.set_line_width(0)
        gw.add(deck)
        def create_triangle(b, h):
            tri = GPolygon()
            tri.add_vertex(-b / 2, h / 2)
            tri.add_vertex(b / 2, h / 2)
            tri.add_vertex(0, -h / 2)
            return tri

        triangle = create_triangle(70, 70)
        triangle.set_filled(True)
        triangle.set_color("orange")
        gw.add(triangle, 100, 350)

    def boat():
        pole= GRect(495, 530, 10,20)
        pole.set_fill_color("black")
        pole.set_filled(True)
        pole.set_line_width(0)
        gw.add(pole)

        deck= GRect(455, 550, 90,25)
        deck.set_fill_color("black")
        deck.set_filled(True)
        deck.set_line_width(0)
        gw.add(deck)
        def create_triangle(b, h):
            tri = GPolygon()
            tri.add_vertex(-b / 2, h / 2)
            tri.add_vertex(b / 2, h / 2)
            tri.add_vertex(0, -h / 2)
            return tri

        triangle = create_triangle(70, 70)
        triangle.set_filled(True)
        triangle.set_color("lime")
        gw.add(triangle, 500, 500)

    Sunset()
    stars()
    barrier()
    ocean()
    sun()
    mountain()
    buildings()
    lights()
    red_boat()
    pink_boat()
    orange_boat()
    boat()





if __name__ == '__main__':
    draw_image()
