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


def move_circle_special(old_event, event, canvas, circle, cursor_rotation, is_mirrored):
    r = 5
    if old_event is not None:
        prev_coord = canvas.coords(circle)
        prev_x = prev_coord[0] + 5
        prev_y = prev_coord[1] + 5
        x_offset, y_offset = event.x - old_event.x, event.y - old_event.y
        x = prev_x - x_offset
        y = prev_y - y_offset
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvas.coords(circle, x0, y0, x1, y1)


def set_title(root, new_trial_number):
    root.title("Visuomotor Trial #" + new_trial_number.__str__())