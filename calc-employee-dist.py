import csv
from datetime import datetime

def extract_intervals_minutes(line):
    time_points = []
    for date in line:
        delta = datetime.strptime(date, '%H:%M') - datetime.strptime('00:00', '%H:%M')
        minutes_from_begin_of_day = int(delta.total_seconds())//60
        time_points.append(minutes_from_begin_of_day)
    return time_points

def calc_employee_dist(filepath):
    occupied_intervals = [0]*1440

    with open(filepath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            beg1, end1 , beg2, end2 = extract_intervals_minutes(line)
            if end2 == 0:
                end2 = 1439
            occupied_intervals[beg1] += 1
            occupied_intervals[end1] -= 1
            occupied_intervals[beg2] += 1
            occupied_intervals[end2] -= 1
    prefix_sum_array = [0]
    for point in occupied_intervals:
        prefix_sum_array.append(prefix_sum_array[-1]+point)

    prefix_sum_array.pop(0)
    
    ans =  [prefix_sum_array[i] for i in range(0,len(prefix_sum_array),10)]
    return ans

print(calc_employee_dist('csv_file.csv'))
