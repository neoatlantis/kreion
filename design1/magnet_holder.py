#!/bin/bash python3

from svgwriter import SVGWriter, SVGElementsList, SVGTransformGroup
from constants import *
from math import sqrt, ceil

svg = SVGWriter(width=420, height=420)

i = 0
for magnet_i in range(*print_range):
    rotate_angle = 180 / total_magnets * magnet_i

    for dup_i in range(0, print_duplicate):
        col_i = i % print_per_row
        row_i = i // print_per_row
        t_dx, t_dy = (magnet_holder_size+print_spacing) * col_i + 5, (print_spacing+magnet_holder_size) * row_i

        magnet_diagonal = sqrt(magnet_l**2+magnet_d**2)
        arc_margin = (magnet_holder_size - magnet_diagonal)/2.0
        arc_thick = arc_margin * 0.8
        arc_span = magnet_holder_size - 2 * arc_margin

        center = (magnet_holder_size/2.0, magnet_holder_size/2.0)

         #.rect_lt_wh((0, 0), magnet_holder_size, magnet_holder_size)\
        el = SVGTransformGroup([
                "translate(%f %f)" % (
                    t_dx, t_dy
                )
            ])\
            .path(" ".join([
                "M0 0",
                "L%f %f" % (arc_margin, 0),
                "A%f %f 0 0 0 %f %f" % (arc_span/2.0, arc_thick/2.0, arc_span+arc_margin, 0),
                "L%f %f" % (magnet_holder_size, 0),
                
                "L%f %f" % (magnet_holder_size, arc_margin),
                "A%f %f 0 0 0 %f %f" % (arc_thick/2.0, arc_span/2.0, magnet_holder_size, arc_span+arc_margin),
                "L%f %f" % (magnet_holder_size, magnet_holder_size),

                "L%f %f" % (arc_span+arc_margin, magnet_holder_size),
                "A%f %f 0 0 0 %f %f" % (arc_span/2.0, arc_thick/2.0, arc_margin, magnet_holder_size),
                "L%f %f" % (0, magnet_holder_size),

                "L%f %f" % (0, arc_span+arc_margin),
                "A%f %f 0 0 0 %f %f" % (arc_thick/2.0, arc_span/2.0, 0, arc_margin),
                "L0 0",
            ]))\
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

        i += 1


print(str(svg))
print("<!-- total drawable width = %f -->" % (print_per_row*magnet_holder_size+(print_per_row-1)*print_spacing))
n_rows = 1 + ((i-1) // print_per_row)
print("<!-- total drawable height = %f -->" % (n_rows*magnet_holder_size+(n_rows-1)*print_spacing))