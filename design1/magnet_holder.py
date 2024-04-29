#!/bin/bash python3

from svgwriter import SVGWriter, SVGElementsList, SVGTransformGroup
from constants import *

svg = SVGWriter()


for i in range(0, 10):
    rotate_angle = 15 * i
    col_i = i % 4
    row_i = i // 4
    t_dx, t_dy = magnet_holder_size * col_i + 5, magnet_holder_size * row_i

    center = (magnet_holder_size/2.0, magnet_holder_size/2.0)
    el = SVGTransformGroup([
            "translate(%f %f)" % (
                t_dx, t_dy
            )
        ])\
        .rect_lt_wh((0, 0), magnet_holder_size, magnet_holder_size)\
        .append(
            SVGTransformGroup([
                "rotate(%d   %f %f)" % (
                    rotate_angle,
                    center[0], center[1]
                )
            ])\
            .rect_center_wh(center, magnet_l, magnet_d)
    )
    svg.append(el)


print(str(svg))