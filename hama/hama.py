# -*- coding: utf-8 -*-
from PIL import Image
import svgwrite
from svgwrite.extensions import Inkscape
from cairosvg import svg2png, svg2pdf
from io import BytesIO
from pdb import pm


colors = {(0,0,0): 'black',
          (255,255,255): 'white',
          (255,255,0): 'yellow',
          (236,0,140): 'pink',
          (0,173,239): 'lightblue',
          (46,49,146): 'blue',
          (0,166,80): 'green',
          (237,28,36): 'red',
          (255,248,128): 'lightyellow',
          (246,128,197): 'rosy',
          (128,214,247): 'lightblue',
          (145,145,145): 'gray',
          }

def distance(c1, c2):
    return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)**0.5

def nearest_colors(point, colors=colors):
    return sorted((distance(point, color), color) for color in colors)

def nearest_color(point, colors=colors):
    distances = nearest_colors(point, colors=colors)
    return distances[0][1]
# dwg = svgwrite.Drawing(filename='demo.svg', debug=False)
# inkscape = Inkscape(dwg)

# layer = inkscape.layer(label='hest', locked=True)
# g = svgwrite.container.Group(id='ged')
# dwg.add(g)

# # dwg.add(svgwrite.shapes.Circle(center=(0, 0), r=5))

# def LAYER(f, name=None):
#     print(f, name)
#     def inner(*args, **kwargs):
#         print(args, kwargs)
#     return inner


# def rectangle(dwg, x=14, y=14, radius=5, Radius=30):
#     offset = Radius/2  # Zero offset
#     for ix in range(x):
#         for iy in range(y):
#             dwg.add(svgwrite.shapes.Circle(center=(Radius*ix+offset, Radius*iy+offset), r=radius,  fill=svgwrite.rgb(255, 100, 100), opacity=0.4) )


# # @LAYER(name='gede')
# def rct(dwg, x=14, y=14, radius=5, Radius=30):
#     offset = Radius/2  # Zero offset
#     for ix in range(x):
#         for iy in range(y):
#             dwg.add(svgwrite.shapes.Circle(center=(Radius*ix+offset, Radius*iy+offset), r=radius,  fill=svgwrite.rgb(255, 100, 100), opacity=0.4) )




# def rectangle2(dwg, x=14, y=14, radius=5, Radius=30):
#     pattern = dwg.pattern(insert=(10, 10), size=(20, 20))
#     pattern.add(dwg.rect(insert=(5, 5), size=(10, 10)))


# # rct()

# # rectangle(g)
# # pattern = dwg.defs.add(dwg.pattern(insert=(150,0)))
# # pattern.add(rectangle(dwg))


# # rectangle2(dwg)

# # pattern = dwg.defs.add(dwg.pattern(size=(20,20)))
# # pattern.add(dwg.circle((10, 10), 30))
# # dwg.add(dwg.circle((100, 100), 50))

# # # d.svg.save()
# # dwg.save(pretty=True)

# import svgwrite
 
# def pattern(name):
#     dwg = svgwrite.Drawing(name, width='20cm', height='15cm', profile='full', debug=True)
 
#     # set user coordinate space
#     # dwg.viewbox(width=200, height=150)
#     pattern = dwg.defs.add(dwg.pattern(size=(15, 45), patternUnits="userSpaceOnUse"))
#     pattern.add(dwg.circle((7, 14), 3.5))
#     dwg.add(dwg.circle((101, 102), 503, fill=pattern.get_paint_server()))
#     dwg.save(pretty=True)
#     return dwg


from functools import wraps
from time import time, sleep

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        rv = func(*args, **kwargs)
        end = time()
        print(func.__name__, ':', end-start)
        return rv
    return wrapper


class MyDrawing:
    def __init__(self, name, /, d=5, size=(2,2), profile='full', inkscape=True, debug=False):
        self.d = d
        self.size = self.mm(self.d*size[0], self.d*size[1])
        self.dwg = svgwrite.Drawing(name, debug=debug, size=self.size)

        if inkscape:
            self.inkscape = Inkscape(self.dwg)
        self.r = d/2
        self.t = self.d/5

        self.bead1 = self.bead()
        # self.bead2 = self.bead()

    def __repr__(self):
        return repr(self.dwg)

    @staticmethod
    def mm(*numbers):
        numbers = tuple(f'{number}mm' for number in numbers)
        return numbers if len(numbers) > 1 else numbers[0]

    @timer
    def bead(self):
        # Pattern added
        bead = self.dwg.pattern(size=self.mm(self.d, self.d), patternUnits='userSpaceOnUse')
        bead.add(self.dwg.circle(self.mm(self.r, self.r), self.mm(self.r), fill=svgwrite.rgb(255,0,0)))
        bead.add(self.dwg.circle(self.mm(self.r, self.r), self.mm(self.r-self.t), fill=svgwrite.rgb(255,255,255)))
        self.dwg.defs.add(bead)
        self.bead = bead

        spike = self.dwg.pattern(size=self.mm(self.d, self.d), patternUnits='userSpaceOnUse')
        spike.add(self.dwg.circle(self.mm(self.r, self.r), self.mm(self.t/2), stroke=svgwrite.rgb(0,0,0)))
        spike.add(self.dwg.circle(self.mm(self.r, self.r), self.mm(self.t/4), stroke=svgwrite.rgb(240,240,240)))
        self.dwg.defs.add(spike)

        beads     = self.dwg.rect((0,0), size=self.size, patternUnits='userSpaceOnUse', fill=bead.get_paint_server())
        self.dwg.add(beads)

        # baseplate = self.dwg.rect((0,0), size=self.size, patternUnits='userSpaceOnUse', fill=spike.get_paint_server())
        # self.dwg.add(baseplate)

        # self.dwg.add(self.dwg.circle((25,25), 25, fill=svgwrite.rgb(255,255,0)))

    # def use_pattern(self, x=4, y=4):  # 29,29
    #     self.dwg.add(self.dwg.rect((0,0), size=(x*self.d, y*self.d), fill=(255,0,0)))#self.bead1.get_paint_server()))  # 1
    #     self.square.add(svgwrite.shapes.Circle((self.r,self.r),r=self.r))

    @timer
    def save(self):
        self.dwg.save(pretty=True)



if __name__ == '__main__':
    md = MyDrawing('demo.svg')
    md.save()

    png = svg2png(md.dwg.tostring(), dpi=3000, write_to='demo.png')
    # png = svg2png(file_obj=open('demo.svg', 'r'), dpi=1200, output_width=2900, output_height=2900, scale=1, write_to='demo__.png')
    # img = Image.open(BytesIO(png))
    # img.save('demo.png')
    # pdf = svg2pdf(md.dwg.tostring(), write_to='demo.pdf')


    # dwg2 = pattern("demo2.svg")
    # dwg = svgwrite.Drawing(filename='demo.svg', debug=True)
    
    # pattern2(dwg)


