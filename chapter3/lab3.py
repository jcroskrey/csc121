import arcade
import random

arcade.open_window(800, 750, "Windmill Attempt")

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

# Draw the grass.
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

# Windmill cement base.
arcade.draw_lrtb_rectangle_filled(275, 525, 220, 170, arcade.color.GRAY)

# Bottom half of windmill.
arcade.draw_lrtb_rectangle_filled(285, 515, 420, 220, arcade.color.BROWN_NOSE)

# Draw a border aroun the bottom half of the windmill.
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

# Draw the left arm of the windmill.


arm_l = 250
wing_l = 200
wing_h = 68
ox = 400                 # Origin x.
oy = 460                 # Origin y.
end_x = ox - arm_l          # 150
canvas_rx = ox - 50         # 350
canvas_ty = oy + wing_h     # 530
canvas_by = oy + 3          # 463
canvas_my = oy + 37         # 497

# Draw the arm of the wing.
arcade.draw_line(ox, oy, 
end_x, oy,
arcade.color.BLACK, 5
)
# Draw the canvas for the windmill's wing.
arcade.draw_lrtb_rectangle_filled(end_x, canvas_rx, 
canvas_ty, canvas_by, 
arcade.color.DARK_GRAY
)
#Draw the supports for the windmill's wing.
arcade.draw_lrtb_rectangle_outline(end_x, canvas_rx, 
canvas_ty, canvas_by, 
arcade.color.BLACK, 2
)
arcade.draw_line(arm_l, canvas_by,
arm_l, canvas_ty, 
arcade.color.BLACK, 3
)
arcade.draw_line(end_x, canvas_my,
canvas_rx, canvas_my, 
arcade.color.BLACK, 3
)
arcade.draw_line(wing_l, canvas_by,
wing_l, canvas_ty,
arcade.color.BLACK, 3
)
arcade.draw_line(wing_l+100, canvas_by, 
wing_l+100, canvas_ty, 
arcade.color.BLACK, 3
)

# Draw arm of the bottom wing of the windmill.
arcade.draw_line(400, 460, 400, 210, arcade.color.BLACK, 5)
# Draw the canvas for the wing.
arcade.draw_lrtb_rectangle_filled(332, 397, 410, 210, 
    arcade.color.DARK_GRAY
)
# Draw the supports for the wing.
arcade.draw_lrtb_rectangle_outline(332, 397, 410, 210, 
    arcade.color.BLACK, 2
)
arcade.draw_line(365, 410, 365, 210, arcade.color.BLACK, 3) # Vertical.
arcade.draw_line(332, 360, 397, 360, arcade.color.BLACK, 3) # Horizontal.
arcade.draw_line(332, 310, 397, 310, arcade.color.BLACK, 3) # Horizontal.
arcade.draw_line(332, 260, 397, 260, arcade.color.BLACK, 3) # Horizontal.

# Draw right wing of the windmill. 
arcade.draw_line(400, 460, 650, 460, arcade.color.BLACK, 5)
# Draw canvas for wing.
arcade.draw_lrtb_rectangle_filled(450, 650, 457, 389,
    arcade.color.DARK_GRAY
)
# Draw the supports for the wing.
arcade.draw_lrtb_rectangle_outline(450, 650, 457, 389,
    arcade.color.BLACK, 3
)
arcade.draw_line(450, 423, 650, 423, 
    arcade.color.BLACK, 3
)
arcade.draw_line(500, 457, 500, 389,
    arcade.color.BLACK, 3
)
arcade.draw_line(550, 457, 550, 389, 
    arcade.color.BLACK, 3
)
arcade.draw_line(600, 457, 600, 389,
    arcade.color.BLACK, 3
)

# Draw the top wing of the windmill.
arcade.draw_line(400, 460, 400, 710, 
    arcade.color.BLACK, 5
)
# Draw the canvas
arcade.draw_lrtb_rectangle_filled(403, 472, 710, 510, 
    arcade.color.DARK_GRAY
)
# Draw the supports
arcade.draw_lrtb_rectangle_outline(403, 472, 710, 510,
    arcade.color.BLACK, 3
)
arcade.draw_line(437, 510, 437, 710, 
    arcade.color.BLACK, 3
)
arcade.draw_line(403, 560, 472, 560,
    arcade.color.BLACK, 3
)
arcade.draw_line(403, 610, 472, 610,
    arcade.color.BLACK, 3
)
arcade.draw_line(403, 660, 472, 660,
    arcade.color.BLACK, 3
)



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

def random_wheat_spawn(num_wheat):
    x_range = [2*i + x for i, x in enumerate(sorted(random.sample(range(10, 790), num_wheat)))]
    y_range = random.sample(range(20, 200), num_wheat)

    for n in range(num_wheat):
        x = x_range[n]
        y = y_range[n]
        wheat(x, y)

random_wheat_spawn(100)

arcade.finish_render()

arcade.run()