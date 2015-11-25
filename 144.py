from sympy.solvers import solve
from sympy import Symbol
from math import atan, pi, tan

def eq(x0, x1):
    return abs(x0 - x1) < 1e-05
x_var = Symbol('x')
ellipse_top = (100 - 4 * x_var**2)**.5
ellipse_bottom = -(100 - 4 * x_var**2)**.5

initial_line_slope = -197/14.
initial_line = initial_line_slope * x_var + 10.1

intersection_top_x = solve(ellipse_top - initial_line, x_var)[0]
intersection_bottom_x = solve(ellipse_bottom - initial_line, x_var)[0]

intersection_top_y = ellipse_top.evalf(subs={'x': intersection_top_x})
intersection_bottom_y = ellipse_bottom.evalf(subs={'x': intersection_bottom_x})

slope_top = -4 * intersection_top_x / intersection_top_y
slope_bottom = -4 * intersection_bottom_x / intersection_bottom_y


def get_angle_from_slope_and_point(line_slope, x_coord, y_coord):
    # formula for angle between two lines with slope m1 and m2
    # arctan( abs( (m1 - m2) / (1 + m1*m2) ) )
    ellipse_slope = -4 * x_coord / y_coord
    # TODO: fix this function as well
    return atan(((ellipse_slope - line_slope)/(1 + ellipse_slope * line_slope)))


def get_angle_of_intersection_by_slopes(slope1, slope2):
    a = atan(slope1)
    b = atan(slope2)
    angle = abs(a-b)
    return min(angle, abs(pi-angle))


def new_slope_from_two_slopes(int_slope, vect_slope):
    angle = get_angle_of_intersection_by_slopes(int_slope, vect_slope)
    int_angle = atan(int_slope)
    new_angle_1 = int_angle + angle
    new_angle_2 = int_angle - angle
    #print new_angle_1, new_angle_2
    new_slope = tan(new_angle_1)
    if not eq(new_slope, vect_slope):
        return new_slope
    return tan(new_angle_2)

def point_slope(slope, x_coord, y_coord):
    return slope * (x_var - x_coord) + y_coord



def get_next_point_and_line(line, line_slope, x_coord, y_coord):
    # Start with a line, slope and point
    # Get new intersection point
    # Get angle of intersection and new angle
    # Get new slope and line
    # Return a line, slope and point
    # find new x, since it is not the same as the previous x
    xs = solve(ellipse_top - line, x_var) + solve(ellipse_bottom - line, x_var)
    x = filter(lambda x: not eq(x, x_coord), xs)[0]
    y = line.evalf(subs={'x': x})

    ellipse_slope = -4 * x / y
    new_slope = new_slope_from_two_slopes(ellipse_slope, line_slope)
    #print 'ellipse_slope', ellipse_slope, x_coord, y_coord, new_slope

    # find our new y based on the new x and the line
    new_line = point_slope(new_slope, x, y)
    return new_line, new_slope, x, y

init_y = 9.99998989720405
line, line_slope, x_coord, y_coord = get_next_point_and_line(initial_line, initial_line_slope, 0.00710731694996590, init_y)
count = 1
while True:
    count += 1
    line, line_slope, x_coord, y_coord = get_next_point_and_line(line, line_slope, x_coord, y_coord)
    print x_coord, y_coord, count
    if abs(x_coord) < 0.01 and y_coord > 0:
        break    
print count


#angle = get_angle_from_slope_and_point(initial_line_slope, intersection_bottom_x, intersection_bottom_y)

#next_slope = slope_from_angle_and_slope(angle, initial_line_slope)
#next_line = point_slope(next_slope, intersection_bottom_x, intersection_bottom_y)

#next_bottom_xs = [solve(next_line - ellipse_bottom, x)] + [solve(next_line - ellipse_top, x)]
#next_bottom_x = filter(lambda x: x[1] - intersection_bottom_x < 1e-10, next_bottom_xs)[0]
