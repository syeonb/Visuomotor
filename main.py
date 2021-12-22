from tkinter import *
from renderUtils import *
from writeData import *
import time

# save application after each trial.
# let the users customize the number of trials

# global variables to keep track of
trial_number = 1
cursor_rotation = 0
is_mirrored = False
target_position = [100, 100]
elapsed_time = 0
old_event = None
current_mouse_pos = [0, 0]
red_circle_pos = [0, 0]

# initialize root window
root = Tk()
root.geometry("1000x750")
root.resizable(False, False)
set_title(root, trial_number)

# set canvas to draw circles
canvas = Canvas(root, width=1000, height=750)
canvas.pack()

# draw target and cursor
target = draw_circle(100, 100, 10, canvas, "red")
circle = draw_circle(0, 0, 5, canvas, "blue")
special_circle = draw_circle(500, 375, 5, canvas, "red")

# start measuring time
start = time.time()


def motion(event):
    x, y = event.x, event.y
    write_data_by_row(mouse_position_path, [x, y])
    global circle, special_circle, canvas, prev_x_pos, prev_y_pos, old_event, current_mouse_pos
    move_circle(x, y, 5, canvas, circle)
    prev_x_pos = x
    prev_y_pos = y
    move_circle_special(old_event, event, canvas, special_circle, cursor_rotation, is_mirrored)
    print("red circle pos, {}, {}".format(canvas.coords(special_circle)[0], canvas.coords(special_circle)[1]))
    old_event = event
    current_mouse_pos = [x, y]


def increment_trial():
    global start
    global trial_number
    global target_position
    global target
    global canvas
    global elapsed_time
    end = time.time()
    elapsed_time = end - start
    write_general_trial_data(data_path, trial_number, elapsed_time)

    # restart trial: reset time, target position, and title
    start = end
    trial_number += 1
    target_position[0] += 20
    target_position[1] += 30
    set_title(root, trial_number)
    move_circle(target_position[0], target_position[1], 10, canvas, target)


def check_trial_complete(event):
    if event.x + 10 > target_position[0] > event.x - 10 and event.y - 10 < target_position[1] < event.y + 10:
        print("trial is complete")
        increment_trial()


def handle_focus(event):
    global current_mouse_pos
    move_circle(current_mouse_pos[0], current_mouse_pos[1], 5, canvas, special_circle)


# record mouse movement during trial
root.bind('<Motion>', motion)
# check if the trial is complete, given click
root.bind('<Button-1>', check_trial_complete)
# if the window is focused, reset special cursor position
root.bind("<Return>", handle_focus)
# root.bind("<Leave>", handle_focus)


root.mainloop()
