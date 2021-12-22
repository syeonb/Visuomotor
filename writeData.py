import csv

# csv file data
# TODO: dynamically generated path, create csv file directly from the code
data_path = './trial_data/trialData.csv'
mouse_position_path = './trial_data/mousePositions.csv'

general_header = ["trial", "time elapsed"]


def write_data_by_row(path, row):
    with open(path, 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(row)


def write_general_trial_data(path, trial_number, elapsed_time):
    # overwrites data. use 'a' to add to existing data
    f = open(path, 'w')
    writer = csv.writer(f)
    writer.writerow(general_header)
    writer.writerow([trial_number, elapsed_time])
    f.close()