import arcade
import random
import math

def draw_grass():
    # Draw the grass.
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.ARMY_GREEN)


def draw_windmill_body():
    # Windmill cement base.
    arcade.draw_lrtb_rectangle_filled(275, 525, 220, 170, arcade.color.GRAY)

    # Bottom half of windmill.
    arcade.draw_lrtb_rectangle_filled(285, 515, 420, 220, arcade.color.BROWN_NOSE)

    # Draw a border around the bottom half of the windmill.
    arcade.draw_lrtb_rectangle_outline(285, 515, 420, 220, 
    arcade.color.DARK_BROWN, 5)

    # Draw the Top of the windmmill.
    arcade.draw_triangle_filled(275, 420, 525, 420, 400, 520, 
    arcade.color.BROWN_NOSE
    )

    # Put an outline around the roof.
    arcade.draw_triangle_outline(275, 420, 525, 420, 400, 520, 
    arcade.color.DARK_BROWN, 5
    )

    # Draw a point.
    arcade.draw_point(400, 460, arcade.color.BLACK, 30)


def draw_l_arm(x1, y1, x2, y2):
    """ 
    Takes x1, y1, x2, y2 as arguments.
    Draws the left arm handle of the windmill.
    """
    arcade.draw_line(x1, y1, 
    x2, y2, arcade.color.BLACK, 5
    )
    
# Draw the canvas for the windmill's wing.
def draw_canvas(x1, x2, y1, y2):
    """ Takes x1, x2, y1, y2 as arguments """
    arcade.draw_lrtb_rectangle_filled(x1, x2, 
    y1, y2, arcade.color.DARK_GRAY)

#Draw the supports for the windmill's wing.
def draw_support_outline(x1, x2, y1, y2):
    arcade.draw_lrtb_rectangle_outline(x1, x2, y1, y2, 
        arcade.color.BLACK, 2
    )

def draw_horiz_support(x1, y1, x2, y2):
    arcade.draw_line(x1, y1, x2, y2, 
        arcade.color.BLACK, 3
    )

def draw_vert_support_1(x1, y1, x2, y2):
    arcade.draw_line(x1, y1, x2, y2, 
        arcade.color.BLACK, 3
    ) 

def draw_vert_support_2(x1, y1, x2, y2):
    arcade.draw_line(x1, y1, x2, y2,
        arcade.color.BLACK, 3
    )

def draw_vert_support_3(x1, y1, x2, y2):
    arcade.draw_line(x1, y1, x2, y2, 
        arcade.color.BLACK, 3
    )

def rot_2_points(origin, point1, point2, r):
    """
    Given an origin and a point, this function
    rotates the point around the origin by
    r (in radians) degrees. 
    """
    ox, oy = origin
    px, py = point1
    nx, ny = point2

    qx = ox + math.cos(r) * (px - ox) - math.sin(r) * (py - oy)
    qy = oy + math.sin(r) * (px - ox) + math.cos(r) * (py - oy)

    rx = ox + math.cos(r) * (nx - ox) - math.sin(r) * (ny - oy)
    ry = oy + math.sin(r) * (nx - ox) + math.cos(r) * (ny - oy)

    return qx, qy, rx, ry

def wheat(x, y):
    # Draw the stem
    arcade.draw_line(x, y, x, y-40, arcade.color.WHEAT, 2)
    # Draw the seeds
    arcade.draw_circle_filled(x, y+3, 3, arcade.color.WHEAT)
    arcade.draw_circle_filled(x+3, y, 3, arcade.color.WHEAT)
    arcade.draw_circle_filled(x+3, y-6, 3, arcade.color.WHEAT)
    arcade.draw_circle_filled(x-3, y-2, 3, arcade.color.WHEAT)
    arcade.draw_circle_filled(x-3, y-8, 3, arcade.color.WHEAT)
    # Draw fluffs.
    arcade.draw_line(x, y, x, y+15, arcade.color.WHEAT, 1)
    arcade.draw_line(x, y-5, x+7, y+10, arcade.color.WHEAT, 1)
    arcade.draw_line(x, y-5, x-7, y+10, arcade.color.WHEAT, 1)
    arcade.draw_line(x, y-10, x+7, y+5, arcade.color.WHEAT, 1)
    arcade.draw_line(x, y-10, x-7, y+5, arcade.color.WHEAT, 1)
    arcade.draw_line(x, y-15, x+7, y, arcade.color.WHEAT, 1)
    arcade.draw_line(x, y-15, x-7, y, arcade.color.WHEAT, 1)

    return None



def random_wheat_spawn(num_wheat):
    x_range = random.sample(range(10, 790), num_wheat)
    y_range = random.sample(range(20, 200), num_wheat)
    for n in range(num_wheat):
        x = x_range[n]
        y = y_range[n]
        wheat(x, y)
    
    return None

def rotate_all_points():
    origin = [400, 460] # x, y
    angle = 0

    # Manually put in the rotation for the lrtb functions.
    # If not manually, coordinates will be jarbled.
    q1, w1, e1, r1 = rot_2_points(origin, [150, 528], [350, 463], 
                                  0)
    draw_canvas(q1, e1, w1, r1)
    draw_support_outline(q1, e1, w1, r1)

    q2, w2, e2, r2 = rot_2_points(origin, [150, 528], [350, 463], 
                                  math.pi/2)
    draw_canvas(q2, e2, r2, w2)
    draw_support_outline(q2, e2, r2, w2)

    q3, w3, e3, r3 = rot_2_points(origin, [150, 528], [350, 463], 
                                  math.pi)
    draw_canvas(e3, q3, r3, w3)
    draw_support_outline(e3, q3, r3, w3)

    q4, w4, e4, r4 = rot_2_points(origin, [150, 528], [350, 463], 
                                  3*math.pi/2)
    draw_canvas(e4, q4, w4, r4)
    draw_support_outline(e4, q4, w4, r4)

    for i in range(0, 4):
        a1, b1, c1, d1 = rot_2_points(origin, [400, 460], [150, 460],
                                      angle)
        draw_l_arm(a1, b1, c1, d1)

        a2, b2, c2, d2 = rot_2_points(origin, [150, 497], [350, 497],
                                      angle)
        draw_horiz_support(a2, b2, c2, d2)

        a3, b3, c3, d3 = rot_2_points(origin, [250, 463], [250, 528],
                                      angle)
        draw_vert_support_1(a3, b3, c3, d3)

        a4, b4, c4, d4 = rot_2_points(origin, [200, 463], [200, 528],
                                      angle)
        draw_vert_support_2(a4, b4, c4, d4)

        a5, b5, c5, d5 = rot_2_points(origin, [300, 463], [300, 528],
                                      angle)
        draw_vert_support_3(a5, b5, c5, d5)

        angle += math.pi/2

def draw_bat(x, y):
    # Draw the body
    arcade.draw_ellipse_filled(x, y, 10, 30, arcade.color.BLACK)

    # Draw the ears
    arcade.draw_triangle_filled(x, y+12, x+5, y+10, x+3, y+20, arcade.color.BLACK)
    arcade.draw_triangle_filled(x, y+12, x-5, y+10, x-3, y+20, arcade.color.BLACK)

    # Draw the wings
    arcade.draw_ellipse_filled(x+20, y+5, 15, 40, arcade.color.BLACK, tilt_angle=-70)
    arcade.draw_ellipse_filled(x-20, y+5, 15, 40, arcade.color.BLACK, tilt_angle=70)
    
    # Draw the legs :)
    arcade.draw_line(x+2, y-13, x+6, y-18, arcade.color.BLACK, 2)
    arcade.draw_line(x-2, y-13, x-6, y-18, arcade.color.BLACK, 2)


def on_draw(delta_time):
    """ Draw everything in this function. """
    arcade.start_render()
    draw_grass()

    draw_windmill_body()

    rotate_all_points()

    draw_bat(on_draw.center_x, on_draw.center_y)

    on_draw.center_x += on_draw.delta_x * delta_time
    on_draw.center_y += on_draw.delta_y * delta_time

    # Figure out if we hit the edge and need to reverse.
    if on_draw.center_x < 40 // 2 \
            or on_draw.center_x > 800 - 40 // 2:
        on_draw.delta_x *= -1
    if on_draw.center_y < 38 // 2 \
            or on_draw.center_y > 750 - 38 // 2:
        on_draw.delta_y *= -1
    
on_draw.center_x = 200
on_draw.center_y = 700
on_draw.delta_x = 50
on_draw.delta_y = 50

def main():
    arcade.open_window(800, 750, "Windmill Attempt")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    # random_wheat_spawn(50)

    arcade.schedule(on_draw, 1/80)

    arcade.run()

if __name__ == "__main__":
    main()


