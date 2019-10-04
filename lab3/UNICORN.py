from math import sqrt

from graph import *

windowSize(500, 500)
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def oval_gorizont(fx1, fy1,fx2, fy2, a, b, color, d):
#эллипс по фокусам и точке только горизонтальный
    c = canvas()
    l = (sqrt((fx1-a)*(fx1-a)+(fy1-b)*(fy1-b))+sqrt((fx2-a)*(fx2-a)+(fy2-b)*(fy2-b)))
    x1=(fx2+fx1-l)/2
    y1= fy1-sqrt(l*l/4-(fx2-fx1)*(fx2-fx1)/4)
    x2=(l+fx2+fx1)/2
    y2=(fy1+sqrt(l*l/4-(fx2-fx1)*(fx2-fx1)/4))
    c.create_oval(x1, y1, x2, y2, fill =color, outline=d)

####################################33


def oval_vertic(xx1, yy1, xx2, yy2, xx3, yy3, color, a):
    # овал только вертикальный
    c = canvas()
    l = (sqrt((xx1 - xx3) * (xx1 - xx3) + (yy1 - yy3) * (yy1 - yy3)) + sqrt((xx2 - xx3) * (xx2 - xx3) + (yy2 - yy3) * (yy2 - yy3)))
    x1=  xx2-sqrt(l*l/4-(yy2-yy1)*(yy2-yy1)/4)
    x2= xx2+sqrt(l*l/4-(yy2-yy1)*(yy2-yy1)/4)
    y1=(yy2+yy1-l)/2
    y2=(yy2+yy1+l)/2
    c.create_oval(x1, y1, x2, y2, fill=color, outline=a)


#########################################3


def tree(x,y, k):
    green=rgb_to_hex((74,247,5))
    brushColor("brown")
    penColor('green')
    polygon([(x,y ), ((x+20*k), y), ((x+20*k), (y-80*k)), (x, (y-80*k))])
    penColor('green')
    green_tree = rgb_to_hex((18, 84, 4))
    oval_gorizont((x - 17*k), (y - 100*k), (x + 41*k), (y - 100*k), (x + 60*k), (y - 100*k), green_tree, green)
    oval_gorizont((x-45*k), (y-170*k), (x+80*k), (y-170*k), (x+20*k), (y-220*k), green_tree, green)
    circle((x+39*k), (y-112*k), 8*k)
    oval_vertic((x+21*k), (y-300*k), (x+21*k), (y-230*k), (x+90*k), (y-240*k), green_tree, green)

#####################################3


def unicooooooooorn(x,y,k):
    # x=220 , 40
    brushColor('white')
    penColor('white')
    polygon([(x, y), (x + 10*k, y), (x + 10*k, y - 80*k), (x, y - 80*k)])
    polygon([(x+28*k, y-11*k), (x+42*k, y-11*k), (x + 42*k, y - 70*k), (x+28*k, y - 70*k)])
    polygon([(x + 118*k, y +5*k), (x + 135*k, y +5*k), (x + 135*k, y - 60*k), (x + 118*k, y - 60*k)])
    polygon([(x + 142*k, y -5*k), (x + 156*k, y -5*k), (x + 156*k, y - 75*k), (x + 142*k, y - 75*k)])
    white=rgb_to_hex((255,255,255))
    oval_gorizont(x+1*k, y-90*k, x+161*k, y-90*k, x+66*k, y-150*k, white, white)
    penColor('white')
    polygon([(x + 130*k, y - 117*k), (x + 170*k, y - 117*k), (x + 170*k, y - 230*k), (x + 130*k, y - 230*k)])
    oval_gorizont(x + 135*k, y - 223*k, x + 180*k, y - 223*k, x + 150*k, y - 260*k, white, white)
    oval_gorizont(x + 173*k, y - 210*k, x + 213*k, y - 210*k, x + 183*k, y - 225*k, white, white)
    brushColor('black')
    circle(x+178*k, y-233*k, 10*k)
    penColor('violet')
    brushColor('violet')
    polygon([(x + 163*k, y - 260*k), (x + 177*k, y - 257*k), (x + 174*k, y - 330*k)])
    pink=rgb_to_hex((242,41,232))
    grr=rgb_to_hex((41,252,175))
    orange=rgb_to_hex((242,108,41))
    red=rgb_to_hex((242,41,41))
    yellow=rgb_to_hex((242,215,41))
    viol=rgb_to_hex((152,41,242))

    oval_gorizont(x+110*k, y-233*k, x+130*k, y-233*k, x+120*k, y-247*k, viol, white)
    oval_gorizont(x + 100*k, y - 215*k, x + 132*k, y - 215*k, x + 120*k, y - 224*k, pink, white)
    oval_gorizont(x + 90*k, y - 200*k, x + 132*k, y - 200*k, x + 120*k, y - 210*k, grr, white)
    oval_gorizont(x + 70*k, y - 190*k, x + 132*k, y - 190*k, x + 120*k, y - 200*k, yellow, white)
    oval_gorizont(x + 80*k, y - 175*k, x + 132*k, y - 175*k, x + 120*k, y - 185*k, orange, white)
    oval_gorizont(x + 83*k, y - 155*k, x + 132*k, y - 155*k, x + 120*k, y - 170*k, red, white)
    oval_gorizont(x -30*k, y - 93*k, x -10*k, y - 93*k, x-30*k, y - 78*k, red, white)
    oval_gorizont(x -90*k, y - 20*k, x -12*k, y - 20*k, x -40*k, y - 35*k, orange, white)
    oval_gorizont(x - 78*k, y - 33*k, x - 18*k, y - 33*k, x - 40*k, y - 46*k, yellow, white)
    oval_gorizont(x - 73*k, y - 45*k, x - 16*k, y - 45*k, x - 40*k, y - 55*k, grr, white)
    oval_gorizont(x  -65*k, y - 55*k, x  -18*k, y -55*k, x  -40*k, y - 67*k, pink, white)
    oval_gorizont(x -50*k, y - 70*k, x -18*k, y - 70*k, x - 40*k, y -85*k, viol, white)

def unicooooooooorn_back(x,y,k):
    # x=220 , 40
    brushColor('white')
    penColor('white')
    polygon([(2*x+130-x, y), (2*x+130-x + 10*k, y), (2*x+130-x + 10*k, y - 80*k), (2*x+130-x, y - 80*k)])
    polygon([(2*x+130-(x+28*k), y-11*k), (2*x+130-(x+42*k), y-11*k), (2*x+130-(x + 42*k), y - 70*k), (2*x+130-(x+28*k), y - 70*k)])
    polygon([(2*x+130-(x + 118*k), y +5*k), (2*x+130-(x + 135*k), y +5*k), (2*x+130-(x + 135*k), y - 60*k), (2*x+130-(x + 118*k), y - 60*k)])
    polygon([(2*x+130-(x + 142*k), y -5*k), (2*x+130-(x + 156*k), y -5*k), (2*x+130-(x + 156*k), y - 75*k), (2*x+130-(x + 142*k), y - 75*k)])
    white=rgb_to_hex((255,255,255))
    oval_gorizont(2*x+130-(x+1*k), y-90*k, 2*x+130-(x+161*k), y-90*k, 2*x+130-(x+66*k), y-150*k, white, white)
    penColor('white')
    polygon([(2*x+130-(x + 130*k), y - 117*k), (2*x+130-(x + 170*k), y - 117*k), (2*x+130-(x + 170*k), y - 230*k), (2*x+130-(x + 130*k), y - 230*k)])
    oval_gorizont(2*x+130-(x + 135*k), y - 223*k, 2*x+130-(x + 180*k), y - 223*k, 2*x+130-(x + 150*k), y - 260*k, white, white)
    oval_gorizont(2*x+130-(x + 173*k), y - 210*k, 2*x+130-(x + 213*k), y - 210*k, 2*x+130-(x + 183*k), y - 225*k, white, white)
    brushColor('black')
    circle(2*x+130-(x+178*k), y-233*k, 10*k)
    penColor('violet')
    brushColor('violet')
    polygon([(2*x+130-(x + 163*k), y - 260*k), (2*x+130-(x + 177*k), y - 257*k), (2*x+130-(x + 174*k), y - 330*k)])
    pink=rgb_to_hex((242,41,232))
    grr=rgb_to_hex((41,252,175))
    orange=rgb_to_hex((242,108,41))
    red=rgb_to_hex((242,41,41))
    yellow=rgb_to_hex((242,215,41))
    viol=rgb_to_hex((152,41,242))

    oval_gorizont(2*x+130-(x+110*k), y-233*k, 2*x+130-(x+130*k), y-233*k, 2*x+130-(x+120*k), y-247*k, viol, white)
    oval_gorizont(2*x+130-(x + 100*k), y - 215*k, 2*x+130-(x + 132*k), y - 215*k, 2*x+130-(x + 120*k), y - 224*k, pink, white)
    oval_gorizont(2*x+130-(x + 90*k), y - 200*k, 2*x+130-(x + 132*k), y - 200*k, 2*x+130-(x + 	120*k), y - 210*k, grr, white)
    oval_gorizont(2*x+130-(x + 70*k), y - 190*k, 2*x+130-(x + 132*k), y - 190*k, 2*x+130-(x + 120*k), y - 200*k, yellow, white)
    oval_gorizont(2*x+130-(x + 80*k), y - 175*k, 2*x+130-(x + 132*k), y - 175*k, 2*x+130-(x + 120*k), y - 185*k, orange, white)
    oval_gorizont(2*x+130-(x + 83*k), y - 155*k, 2*x+130-(x + 132*k), y - 155*k, 2*x+130-(x + 120*k), y - 170*k, red, white)
    oval_gorizont(2*x+130-(x -30*k), y - 93*k, 2*x+130-(x -10*k), y - 93*k, 2*x+130-(x-30*k), y - 78*k, red, white)
    oval_gorizont(2*x+130-(x -90*k), y - 20*k, 2*x+130-(x -12*k), y - 20*k, 2*x+130-(x -40*k), y - 35*k, orange, white)
    oval_gorizont(2*x+130-(x - 78*k), y - 33*k, 2*x+130-(x - 18*k), y - 33*k, 2*x+130-(x - 40*k), y - 46*k, yellow, white)
    oval_gorizont(2*x+130-(x - 73*k), y - 45*k, 2*x+130-(x - 16*k), y - 45*k, 2*x+130-(x - 40*k), y - 55*k, grr, white)
    oval_gorizont(2*x+130-(x  -65*k), y - 55*k, 2*x+130-(x  -18*k), y -55*k, 2*x+130-(x  -40*k), y - 67*k, pink, white)
    oval_gorizont(2*x+130-(x -50*k), y - 70*k, 2*x+130-(x -18*k), y - 70*k, 2*x+130-(x - 40*k), y -85*k, viol, white)




######################3
# земля

green=rgb_to_hex((74,247,5))
penColor(green)
brushColor(green)
polygon([(0,500 ), (500, 500), (500, 260), (0, 260)])

# небо
blue=rgb_to_hex((167,239,250))
brushColor(blue)
penColor(blue)
polygon([(0,0 ), (500, 0), (500, 260), (0, 260)])

#солнце
# penColor('yellow')
#brushColor('yellow')
#c = canvas()
#sun=[(x, sqrt(2500-x*x+1000*x-500*500)) for x in range(450,500)]
#sun.append((500,0))
#polygon(sun)

brushColor(rgb_to_hex((210, 247, 247)))
penColor(rgb_to_hex((210, 247, 247)))
circle(400,100,55)
brushColor(rgb_to_hex((195, 249, 250)))
penColor(rgb_to_hex((195, 249, 250)))
circle(400,100,57)
brushColor(rgb_to_hex((252, 251, 177)))
penColor(rgb_to_hex((252, 251, 177)))
circle(400, 100, 50)
penColor(rgb_to_hex((252, 253, 158)))
brushColor(rgb_to_hex((252, 253, 158)))
circle(400,100,45)
brushColor(rgb_to_hex((252,251,139)))
penColor(rgb_to_hex((252,251,139)))
circle(400, 100, 40)
brushColor(rgb_to_hex((252, 250, 116)))
penColor(rgb_to_hex((252, 250, 116)))
circle(400,100,35)
brushColor(rgb_to_hex((255, 252, 94)))
penColor(rgb_to_hex((255, 252, 94)))
circle(400, 100, 30)
brushColor(rgb_to_hex((255,252,64)))
penColor(rgb_to_hex((255,252,64)))
circle(400,100, 25)
brushColor(rgb_to_hex((255,251,43)))
penColor(rgb_to_hex((255,251,43)))
circle(400, 100, 20)
brushColor(rgb_to_hex((255, 250 ,49)))
penColor(rgb_to_hex((255, 250 ,49)))
circle(400, 100, 15)
brushColor(rgb_to_hex((255,251,20)))
penColor(rgb_to_hex((255,251,20)))
circle(400,100,8)
brushColor(rgb_to_hex((255, 252 , 3)))
penColor(rgb_to_hex((255,253,3)))
circle(400, 100, 5)

tree(80,400,1.1)
tree(80,400,0.7)
tree(80,400,0.5)
unicooooooooorn(130,450,0.5)
unicooooooooorn(200,290,0.4)
unicooooooooorn_back(300,480,0.35)
unicooooooooorn_back(300,280,0.25)
#unicooooooooorn_back(300,200,0.2)

run()