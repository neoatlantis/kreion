#!/usr/bin/env python3

from math import pi
import subprocess
import os

REFERENCE_DIAMETER = 340
BAR_DIAMETER = 10
BAR_TOLERANCE = 0.3
BAR_LENGTH = 40

RING_DIVISION = 6
ELEMENT_SPACING_MIN_COEFF = 0.2
ELEMENT_SPACING_MAX_COEFF = 0.4

count_elements = []
for times in range(1, 1000):
    divisions = RING_DIVISION * times
    l = pi * (REFERENCE_DIAMETER-BAR_LENGTH)
    p = (l / divisions / BAR_DIAMETER) - 1
    if ELEMENT_SPACING_MIN_COEFF <= p <= ELEMENT_SPACING_MAX_COEFF:
        count_elements.append((divisions, p))
if len(count_elements) < 1:
    print("Cannot find proper count of magnets.")
    exit()

count_elements = min(count_elements, key=lambda x: x[1])[0]

element_spacing = \
    (pi * (REFERENCE_DIAMETER-BAR_DIAMETER) / count_elements - BAR_DIAMETER)

for i in range(0, RING_DIVISION):
    RING_ANGLE = 360 / RING_DIVISION
    RING_OFFSET = i * RING_ANGLE

    filename_base = "D%d-N%d-%d_of_%d" % (
        REFERENCE_DIAMETER, count_elements, i+1, RING_DIVISION)
    filename_scad = "%s.scad" % filename_base
    filename_stl  = "%s.stl" % filename_base

    print(filename_stl)
    
    data = f"""
/*
-------------------------------------------------------------------------------
{filename_scad}
Count of magnets in total: {count_elements}
Magnet spacing: {element_spacing}mm
-------------------------------------------------------------------------------
*/


REFERENCE_DIAMETER = {REFERENCE_DIAMETER};
RING_ANGLE = {RING_ANGLE}; RING_OFFSET = {RING_OFFSET};

ANGLES_SEPARATION = {360/count_elements}; // degrees
ANGLES = [0: ANGLES_SEPARATION: 360];
BAR_DIAMETER = {BAR_DIAMETER+BAR_TOLERANCE};
BAR_LENGTH = {BAR_LENGTH};

_BAR_DIAGONAL = sqrt(BAR_DIAMETER^2+BAR_LENGTH^2);
_RING_DIAMETER = _BAR_DIAGONAL;


difference() {{

    rotate([0, 0, RING_OFFSET])
        rotate_extrude(angle = RING_ANGLE, $fn=200)
            translate([REFERENCE_DIAMETER / 2, 0, 0])
                circle(r = _RING_DIAMETER / 2, $fn = 200);

    for (a = ANGLES) {{
        rotate([0, 0, a+ANGLES_SEPARATION/2])
            translate([REFERENCE_DIAMETER / 2, 0, 0])
                rotate([0, -a/2, 0])
                    cube(
                        [_BAR_DIAGONAL+5, BAR_DIAMETER, BAR_DIAMETER],
                        center=true
                    );
    }}
    
}}
"""

    print(data)

    open(filename_scad, "w+").write(data)
    subprocess.call(["openscad", "-o", filename_stl, filename_scad])
    os.unlink(filename_scad)
