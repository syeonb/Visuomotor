from tkinter import *
from renderUtils import *
from writeData import *
import time

# save application after each trial.
# TODO: let the users customize the number of trials
# number of trials, angle of rotation
# window size

# set these variables
is_mirrored = False
cursor_rotation = 0

# global variables to keep track of
trial_number = 1
target_position = [300, 300]
elapsed_time = 0
old_event = None
current_mouse_pos = [0, 0]
red_circle_pos = [0, 0]
previous_target_pos = [0, 0]
can_reset = False

max_trial_num = 0
window_size = [1000, 750]

# initialize root window
root = Tk()
root.geometry("1000x750")
root.resizable(False, False)
set_title(root, trial_number)


# set canvas to draw circles
canvas = Canvas(root, width=1200, height=800)
canvas.pack()

# draw target and cursor
target = draw_circle(300, 300, 10, canvas, "red")
cursor = draw_circle(500, 375, 5, canvas, "blue")
# special_circle = draw_circle(500, 375, 5, canvas, "red")

# start measuring time
start = time.time()
initialTime = start


def motion(event):
    global cursor, canvas, old_event, current_mouse_pos, initialTime
    x, y = event.x, event.y
    if not can_reset:
        write_mouse_data_by_row(trial_number, [x, y])
        move_circle_special(old_event, event, canvas, cursor, cursor_rotation, is_mirrored)
    else:
        move_circle(x, y, 5, canvas, cursor)
    old_event = event
    current_mouse_pos = [x, y]


def reset_starting_position():
    global can_reset
    move_circle(target_position[0], target_position[1], 10, canvas, target)
    print("current target position: {}, {}".format(target_position[0], target_position[1]))
    can_reset = False


def increment_trial():
    global start, trial_number, target_position, target, canvas, elapsed_time, previous_target_pos, can_reset
    end = time.time()
    elapsed_time = end - start
    write_general_trial_data(trial_number, elapsed_time, target_position, previous_target_pos)
    # restart trial: reset time, target position, and title
    trial_number += 1
    previous_target_pos = target_position
    target_position = randomize_target_position(target_position[0], target_position[1])
    set_title(root, trial_number)
    move_circle(500, 375, 10, canvas, target)
    can_reset = True


def check_trial_complete(event):
    global start
    if (can_reset):
        start = time.time()
        reset_starting_position()
    else:
        coords = canvas.coords(cursor)
        print("coord: {}, {}".format(coords[0], coords[1]))
        print("Target: {}, {}".format(target_position[0], target_position[1]))
        if coords[0] + 5 + 10 > target_position[0] > coords[0] + 5 - 10 and \
            coords[1] + 5 - 10 < target_position[1] < coords[1] + 5 + 10:
            print("trial is complete")
            increment_trial()
        else:
            print("coord not valid")


root.bind('<Motion>', motion)
root.bind('<Button-1>', check_trial_complete)

root.mainloop()