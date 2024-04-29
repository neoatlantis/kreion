#!/bin/bash python3


class SVGElementsList:

    def __init__(self):
        self.ins = []

    def circle_center_d(self, center, d):
        self.ins.append("""
            <circle cx="%d" cy="%d" r="%d" fill="none" stroke="green" stroke-width="1"/>
        """ % (center[0], center[1], d/2.0))
        return self

    def rect_lt_wh(self, lt, width, height):
        left, top = lt
        self.ins.append("""
            <rect x="%d" y="%d" width="%d" height="%d" 
            fill="none"
            stroke="green" stroke-width="1"/>
        """ % (left, top, width, height))
        return self

    def rect_center_wh(self, center, width, height):
        left = center[0] - width/2.0
        top = center[1] - height/2.0
        return self.rect_lt_wh((left, top), width, height)

    def __str__(self):
        return "".join(self.ins)

    def append(self, e):
        self.ins.append(str(e))
        return self

class SVGTransformGroup(SVGElementsList):

    def __init__(self, transformations=[]):
        SVGElementsList.__init__(self)
        self.transformations = transformations

    def __str__(self):
        return "".join([
            '<g transform="%s">' % " ".join(self.transformations),
            super().__str__(),
            '</g>',
        ])




class SVGWriter(SVGElementsList):

    def __init__(self, width=297, height=210):
        SVGElementsList.__init__(self)
        self.size = (width, height)
    

    def __str__(self):
        return "".join([
            """
            <svg version="1.1" 
                xmlns="http://www.w3.org/2000/svg"
                width="%d" height="%d"
                viewbox="%d %d %d %d">
            """ % (
                self.size[0],
                self.size[1],
                0, 0, self.size[0], self.size[1],
            ),
            super().__str__(),
            '</svg>'
        ])
