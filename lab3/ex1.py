from math import sqrt

from graph import *

windowSize(500, 500)
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def oval_gorizont(fx1, fy1,fx2, fy2, a, b, color):
#эллипс по фокусам и точке только горизонтальный
    c = canvas()
    l = (sqrt((fx1-a)*(fx1-a)+(fy1-b)*(fy1-b))+sqrt((fx2-a)*(fx2-a)+(fy2-b)*(fy2-b)))
    x1=(fx2+fx1-l)/2
    y1= fy1-sqrt(l*l/4-(fx2-fx1)*(fx2-fx1)/4)
    x2=(l+fx2+fx1)/2
    y2=(fy1+sqrt(l*l/4-(fx2-fx1)*(fx2-fx1)/4))
    c.create_oval(x1, y1, x2, y2, fill =color, outline=color)

def oval_vertic(xx1, yy1, xx2, yy2, xx3, yy3, color):
    # овал только вертикальный
    c = canvas()
    l = (sqrt((xx1 - xx3) * (xx1 - xx3) + (yy1 - yy3) * (yy1 - yy3)) + sqrt((xx2 - xx3) * (xx2 - xx3) + (yy2 - yy3) * (yy2 - yy3)))
    x1=  xx2-sqrt(l*l/4-(yy2-yy1)*(yy2-yy1)/4)
    x2= xx2+sqrt(l*l/4-(yy2-yy1)*(yy2-yy1)/4)
    y1=(yy2+yy1-l)/2
    y2=(yy2+yy1+l)/2
    c.create_oval(x1, y1, x2, y2, fill=color, outline=color)
def tree(x,y, k):
    brushColor("brown")
    polygon([(x,y ), ((x+20)*k, y*k), ((x+20)*k, (y-80)*k), (k*x, (y-80))*K])
    green_tree = rgb_to_hex((18, 84, 4))
    oval_gorizont(x - 17, y - 100, x + 41, y - 100, x + 60, y - 100, green_tree)
    oval_gorizont(x-45, y-170, x+80, y-170, x+20, y-220, green_tree)
    circle(x+39, y-112, 8)
    oval_vertic(x+21, y-300, x+21, y-230, x+90, y-240, green_tree)

def unicooooooooorn(x,y):
    # x=220 , 40
    brushColor('white')
    penColor('white')
    polygon([(x, y), (x + 10, y), (x + 10, y - 80), (x, y - 80)])
    polygon([(x+28, y-11), (x+42, y-11), (x + 42, y - 70), (x+28, y - 70)])
    polygon([(x + 118, y +5), (x + 135, y +5), (x + 135, y - 60), (x + 118, y - 60)])
    polygon([(x + 142, y -5), (x + 156, y -5), (x + 156, y - 75), (x + 142, y - 75)])
    white=rgb_to_hex((255,255,255))
    oval_gorizont(x+1, y-90, x+161, y-90, x+66, y-150, white)
    penColor('white')
    polygon([(x + 130, y - 117), (x + 170, y - 117), (x + 170, y - 230), (x + 130, y - 230)])
    oval_gorizont(x + 135, y - 223, x + 180, y - 223, x + 150, y - 260, white)
    oval_gorizont(x + 173, y - 210, x + 213, y - 210, x + 183, y - 225, white)
    brushColor('black')
    circle(x+178, y-233, 10)
    penColor('violet')
    brushColor('violet')
    polygon([(x + 163, y - 260), (x + 177, y - 257), (x + 174, y - 330)])
    pink=rgb_to_hex((242,41,232))
    grr=rgb_to_hex((41,252,175))
    orange=rgb_to_hex((242,108,41))
    red=rgb_to_hex((242,41,41))
    yellow=rgb_to_hex((242,215,41))
    viol=rgb_to_hex((152,41,242))

    oval_gorizont(x+110, y-233, x+130, y-233, x+120, y-247, viol)
    oval_gorizont(x + 100, y - 215, x + 132, y - 215, x + 120, y - 224, pink)
    oval_gorizont(x + 90, y - 200, x + 132, y - 200, x + 120, y - 210, grr)
    oval_gorizont(x + 70, y - 190, x + 132, y - 190, x + 120, y - 200, yellow)
    oval_gorizont(x + 80, y - 175, x + 132, y - 175, x + 120, y - 185, orange)
    oval_gorizont(x + 83, y - 155, x + 132, y - 155, x + 120, y - 170, red)
    oval_gorizont(x -30, y - 93, x -10, y - 93, x-30, y - 78, red)
    oval_gorizont(x -90, y - 20, x -12, y - 20, x -40, y - 35, orange)
    oval_gorizont(x - 78, y - 33, x - 18, y - 33, x - 40, y - 46, yellow)
    oval_gorizont(x - 73, y - 45, x - 16, y - 45, x - 40, y - 55, grr)
    oval_gorizont(x  -65, y - 55, x  -18, y -55, x  -40, y - 67, pink)
    oval_gorizont(x -50, y - 70, x -18, y - 70, x - 40, y -85, viol)


penColor('green')
brushColor('green')
polygon([(0,500 ), (500, 500), (500, 260), (0, 260)])
brushColor('blue')
penColor('blue')
polygon([(0,0 ), (500, 0), (500, 260), (0, 260)])
penColor('yellow')
brushColor('yellow')
c = canvas()
sun=[(x, sqrt(2500-x*x+1000*x-500*500)) for x in range(450,500)]
sun.append((500,0))
polygon(sun)
tree(80,400)
unicooooooooorn(255,400)

run()