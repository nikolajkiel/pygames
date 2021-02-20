# -*- coding: utf-8 -*-
from PIL import Image
import svgwrite
from svgwrite.extensions import Inkscape
from cairosvg import svg2png, svg2pdf
from io import BytesIO
import cv2
from pdb import pm


colors = {

          (255,255,255): 'white',
          (252,193,46): 'yellow',
          (237,28,36): 'red',
          (120, 80, 150): 'Purple',
          (43,114,181): 'lightblue',
          (13,102,65): 'green',
          (145,145,145): 'gray',
          (0,0,0): 'black',
          (132,58,42): 'brown',
          (246,128,197): 'rosy',
          (236,27,80): 'neon pink',
          (18,92,169): 'neon blue',
          (4,166,74): 'neon green',
          (242,112,39): 'orange',
          (249,225,109): 'pastel yellow',
          (236,86,88): 'pastel red',
          (150,124,183): 'pastel purple',
          (55,180,229): 'pastel blue',
          (152,205,135): 'pastel green',
          (232,117,173): 'pink',




          }

colorss ={
         (247, 247, 242): 'White',
         (190, 195, 191): 'Light Gray',
         (150, 152, 156): 'Gray',
         (147, 161, 159): 'Pewter',
         (84, 95, 95): 'Charcoal',
         (86, 87, 92): 'Dark Gray',
         (52, 50, 52): 'Black',
         (241, 229, 216): 'Toasted Marshmallow',
         (234, 196, 159): 'Sand',
         (215, 176, 135): 'Fawn',
         (207, 168, 137): 'Tan',
         (160, 78, 63): 'Rust',
         (136, 64, 79): 'Cranapple',
         (164, 123, 71): 'Light Brown',
         (108, 82, 77): 'Brown',
         (237, 231, 186): 'Cream',
         (250, 238, 141): 'Pastel Yellow',
         (249, 215, 55): 'Yellow',
         (255, 182, 78): 'Cheddar',
         (255, 128, 62): 'Orange',
         (225, 154, 82): 'Butterscotch',
         (255, 97, 88): 'Hot Coral',
         (255, 119, 127): 'Salmon',
         (255, 158, 141): 'Blush',
         (255, 181, 190): 'Flamingo',
         (252, 198, 184): 'Peach',
         (245, 192, 213): 'Light Pink',
         (225, 109, 157): 'Bubble Gum',
         (230, 87, 148): 'Pink',
         (243, 70, 118): 'Magenta',
         (196, 58, 68): 'Red',
         (173, 51, 69): 'Cherry',
         (173, 60, 108): 'Raspberry',
         (178, 95, 170): 'Plum',
         (180, 166, 211): 'Light Lavender',
         (149, 130, 187): 'Pastel Lavender',
         (111, 84, 147): 'Purple',
         (135, 167, 225): 'Blueberry Creme',
         (108, 136, 191): 'Periwinkle',
         (180, 217, 223): "Robin's Egg",
         (124, 210, 242): 'Clear Blue',
         (99, 169, 214): 'Pastel Blue',
         (39, 138, 203): 'Light Blue',
         (0, 102, 179): 'Cobalt',
         (43, 48, 124): 'Dark Blue',
         (22, 40, 70): 'Midnight',
         (176, 232, 213): 'Toothpaste',
         (0, 143, 204): 'Turquoise',
         (56, 199, 175): 'Light Green',
         (0, 150, 138): 'Parrot Green',
         (115, 213, 148): 'Pastel Green',
         (119, 202, 74): 'Kiwi Lime',
         (84, 177, 96): 'Bright Green',
         (0, 150, 84): 'Shamrock',
         (16, 131, 85): 'Dark Green',
         (203, 215, 53): 'Prickly Pear',
         (60, 97, 79): 'Evergreen',
         (0, 172, 74): 'Neon Green',
         (189, 210, 0): 'Neon Yellow',
         (241, 82, 137): 'Neon Pink',
         (255, 141, 46): 'Neon Orange',
         (34, 85, 183): 'Neon Blue',
         (129, 137, 142): 'Silver',
         (181, 127, 69): 'Gold',
         (151, 99, 78): 'Copper',
         (204, 164, 155): 'Pearl Light Pink',
         (233, 149, 145): 'Pearl Coral',
         (209, 198, 110): 'Pearl Yellow',
         (132, 176, 149): 'Pearl Green',
         (130, 185, 179): 'Pearl Light Blue',
         (157, 56, 46): 'Red Glitter',
         (12, 104, 179): 'Blue Glitter',
         (105, 65, 132): 'Purple Glitter',
         (186, 180, 86): 'Yellow Glitter',
         (0, 135, 110): 'Green Glitter',
         (166, 169, 177): 'Clear Glitter',
         (56, 55, 55): 'Black Glitter',
         (208, 219, 222): 'White Glitter',
         (226, 88, 127): 'Pink Glitter',
         (155, 175, 158): 'Fairy Dust',
         (85, 158, 69): 'Kiwi Glitter',
         (158, 167, 174): 'Clear',
         (175, 195, 157): 'Glow Green',
         (86, 172, 190): 'Glow Blue',
         (238, 117, 168): 'Glow Pink',
         (174, 102, 177): 'Glow Purple',
         (234, 175, 111): 'Glow Orange'}

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
# import inspect
# class VidCap(cv2.VideoCapture):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def read(self):
#         curframe = inspect.currentframe()
#         calframe = inspect.getouterframes(curframe, 2)
#         print('caller name:', calframe[1][3])
#         if calframe[1][3] == 'open':
#             return super().read()[-1]
#         return super().read()

# cap = VidCap(0)
# cap.read()

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
    @timer
    def __init__(self, name, /, path=None, colors=colors, d=5, size=(29,29), profile='full', inkscape=True, debug=False):
        self.d = d
        self.size_num = size
        self.size = self.mm(self.d*size[0], self.d*size[1])
        self.dwg = svgwrite.Drawing(name, debug=debug, size=self.size)
        self.colors = colors
        self.beads = {}
        self.path = path

        if inkscape:
            self.inkscape = Inkscape(self.dwg)
            # Add layer(s)
            self.beads_layer = self.inkscape.layer(label='beads', locked=True)
            self.dwg.add(self.beads_layer)
            self.baseplate = self.inkscape.layer(label='baseplate', locked=True)
            self.dwg.add(self.baseplate)

        self.r = d/2
        self.t = self.d/4

        self.setup()
        self.setup2()
        hest=12


    def __repr__(self):
        return repr(self.dwg)

    @timer
    def read_img(self, path=None):
        path = path if path is not None else self.path
        if isinstance(path, cv2.VideoCapture):
            self.im_org = cv2.cvtColor(path.read()[-1], cv2.COLOR_BGR2RGB)
            self.im_org = Image.fromarray(self.im_org)
        else:
            self.im_org = Image.open(path)
        self.im = self.im_org.resize((self.size_num[0], self.size_num[1]))


    @staticmethod
    def mm(*numbers):
        numbers = tuple(f'{number}mm' for number in numbers)
        return numbers if len(numbers) > 1 else numbers[0]

    @timer
    def setup(self):
        # Pattern added
        spike = self.dwg.pattern(size=self.mm(self.d, self.d), patternUnits='userSpaceOnUse')
        spike.add(self.dwg.circle(self.mm(self.r, self.r), self.mm(self.t/3), stroke=svgwrite.rgb(0,0,0)))
        spike.add(self.dwg.circle(self.mm(self.r, self.r), self.mm(self.t/4), stroke=svgwrite.rgb(240,240,240)))
        self.dwg.defs.add(spike)

        self.baseplate.add( self.dwg.rect((0,0), size=self.size, patternUnits='useSpaceOnUse', fill=spike.get_paint_server()) )

        self.create_beads_patterns()


    @timer
    def create_beads_patterns(self):
        for color in self.colors:
            bead = self.dwg.pattern(size=self.mm(self.d, self.d), patternUnits='userSpaceOnUse')
            bead.add(self.dwg.circle(self.mm(self.r, self.r), self.mm(self.r), fill=svgwrite.rgb(color[0],color[1],color[2])))
            bead.add(self.dwg.circle(self.mm(self.r, self.r), self.mm(self.r-self.t), fill=svgwrite.rgb(255,255,255)))
            self.dwg.defs.add(bead)
            self.beads[color] = bead


    @timer
    def setup2(self):
        self.read_img()
        if 1==0:
            beads     = self.dwg.rect((0,0), size=self.size, patternUnits='userSpaceOnUse', fill=self.bead.get_paint_server())
            self.beads_layer.add(beads)
        else:
            for i, args in enumerate(self.im.getdata()):
                if len(args) == 3:
                    r, g, b = args
                else:
                    r, g, b, a = args
                    if r==g==b==a==0:
                        r = g = b = 255
                color = nearest_color((r,g,b), self.colors)
                bead = self.dwg.rect((self.mm(i%self.size_num[0]*self.d), self.mm(i//self.size_num[0]*self.d)), size=(self.mm(self.d), self.mm(self.d)), patternUnits='userSpaceOnUse', fill=self.beads[color].get_paint_server())
                self.beads_layer.add(bead)

        del self.beads


    #     # baseplate = self.dwg.rect((0,0), size=self.size, patternUnits='userSpaceOnUse', fill=spike.get_paint_server())
    #     # self.dwg.add(baseplate)

    #     # self.dwg.add(self.dwg.circle((25,25), 25, fill=svgwrite.rgb(255,255,0)))

    # # def use_pattern(self, x=4, y=4):  # 29,29
    # #     self.dwg.add(self.dwg.rect((0,0), size=(x*self.d, y*self.d), fill=(255,0,0)))#self.bead1.get_paint_server()))  # 1
    # #     self.square.add(svgwrite.shapes.Circle((self.r,self.r),r=self.r))

    @timer
    def save(self):
        self.dwg.save(pretty=False)



if __name__ == '__main__':
    md = MyDrawing('demo.svg', path=cv2.VideoCapture(0), size=(29*4,29*4))
    md.save()

    # png = svg2png(md.dwg.tostring(), dpi=3000, write_to='demo.png')




# png = svg2png(file_obj=open('demo.svg', 'r'), dpi=1200, output_width=2900, output_height=2900, scale=1, write_to='demo__.png')
    # img = Image.open(BytesIO(png))
    # img.save('demo.png')
    # pdf = svg2pdf(md.dwg.tostring(), write_to='demo.pdf')


    # dwg2 = pattern("demo2.svg")
    # dwg = svgwrite.Drawing(filename='demo.svg', debug=True)
    
    # pattern2(dwg)


