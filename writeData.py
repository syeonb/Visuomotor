import csv

# csv file data
# TODO: dynamically generated path, create csv file directly from the code
data_path = './trial_data/'
mouse_position_path = './trial_data/mouse_positions_'

general_header = ["trial", "time elapsed", "cursor starting position", "goal position"]


# previous target position, new target position, rotational angle
def write_mouse_data_by_row(trial_num, row):
    path = mouse_position_path + trial_num.__str__() + ".csv"
    with open(path, 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(row)


def write_general_trial_data(trial_number, elapsed_time, target_position, previous_target_pos):
    # overwrites data. use 'a' to ad to existing data
    path = data_path + "general_trialData_" + trial_number.__str__() + ".csv"
    f = open(path, 'w')
    writer = csv.writer(f)
    writer.writerow(general_header)
    writer.writerow([trial_number, elapsed_time, previous_target_pos, target_position])
    f.close()