import random
import math

previous_cursor_pos = [-1000, -1000]


def draw_circle(x, y, r, canvasname, c):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasname.create_oval(x0, y0, x1, y1, fill=c, outline=c)


def move_circle(x, y, r, canvas, circle):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.coords(circle, x0, y0, x1, y1)


# TODO: change to special moving after 0.5 seconds, keep the rotation until end of trial
def move_circle_special(old_event, event, canvas, circle, cursor_rotation, is_mirrored):
    global previous_cursor_pos
    r = 5
    x = event.x
    y = event.y
    if event.x != 500 and event.y != 375:
        x_offset, y_offset = 500 - event.x, 375 - event.y
        # angle
        mouse_angle = math.atan(y_offset / x_offset)
        print(mouse_angle)
        new_x = x_offset * math.cos(math.radians(cursor_rotation)) - \
                 y_offset * math.sin(math.radians(cursor_rotation))
        new_y = x_offset * math.sin(math.radians(cursor_rotation)) - \
                    y_offset * math.cos(math.radians(cursor_rotation))
        x = 500 - new_x
        y = 375 + new_y

    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.coords(circle, x0, y0, x1, y1)


def randomize_target_position(prev_x, prev_y):
    x_offset = random.randint(200, 250) * random.choice([-1, 1])
    y_offset = random.randint(100, 150) * random.choice([-1, 1])

    if 200 > prev_x + x_offset or prev_x + x_offset > 900:
        new_x = prev_x - x_offset
    else:
        new_x = prev_x + x_offset
    if 100 > prev_y + y_offset or prev_y + y_offset > 600:
        new_y = prev_y - y_offset
        print("out of bounds")
    else:
        new_y = prev_y + y_offset
    return [new_x, new_y]


def set_title(root, new_trial_number):
    root.title("Visuomotor Trial #" + new_trial_number.__str__())
