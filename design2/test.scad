REFERENCE_DIAMETER = 280;

RING_ANGLE = 360; RING_OFFSET = 0;
//RING_ANGLE = 90; RING_OFFSET = 120;
//RING_ANGLE = 90; RING_OFFSET = 120;
//RING_ANGLE = 90; RING_OFFSET = 270;

ANGLES_SEPARATION = 6; // degrees
ANGLES = [0: ANGLES_SEPARATION: 360];
BAR_DIAMETER = 10.3; BAR_LENGTH = 40;

_BAR_DIAGONAL = sqrt(BAR_DIAMETER^2+BAR_LENGTH^2);
_RING_DIAMETER = _BAR_DIAGONAL;


difference() {

    rotate([0, 0, RING_OFFSET])
        rotate_extrude(angle = RING_ANGLE, $fn=200)
            translate([REFERENCE_DIAMETER / 2, 0, 0])
                circle(r = _RING_DIAMETER / 2, $fn = 200);

    for (a = ANGLES) {
        rotate([0, 0, a+ANGLES_SEPARATION/2])
            translate([REFERENCE_DIAMETER / 2, 0, 0])
                rotate([0, -a/2, 0])
                    cube(
                        [_BAR_DIAGONAL+5, BAR_DIAMETER, BAR_DIAMETER],
                        center=true
                    );
    }
    
}