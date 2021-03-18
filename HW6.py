import numpy as np
import pandas as pd
import os
import re

lecture_start_h = 9
lecture_start_m = 30
lecture_end_h = 10
lecture_end_m = 20
min_time = 25        # minutes

files_path = 'Atten'
student_list_file = os.path.join(files_path, 'Student List.xlsx')

# read the student list file
Names = pd.read_excel(student_list_file, 'Sheet1', index_col='Reg')
print(Names.info())

files = [f for f in os.listdir(files_path) if re.match(r'meeting.*\.xlsx', f)]

# iterate on every attendance file
for f in files:
    # read one file
    fp = os.path.join(files_path, f)
    print('file:', fp)
    # read one attendance file, drop rows with missing info
    atten = pd.read_excel(fp, 'Sheet1').dropna()
    # make the registration number the index
    atten.index = atten.Reg.map(lambda x: int(x))
    # convert the timestamps to datetime objects
    atten.Timestamp = pd.to_datetime(atten.Timestamp)
    print(atten.shape)
    # find lecture start and end times
    ts = atten.iloc[0]['Timestamp']
    lec_start = ts.replace(hour=lecture_start_h, minute=lecture_start_m, second=0)
    lec_end = ts.replace(hour=lecture_end_h, minute=lecture_end_m, second=0)
    # create new column with time delta = 0
    new_col = lec_start.strftime("%d %b %Y")
    Names[new_col] = pd.to_timedelta(0)

    # change times outside the lecture time
    atten.loc[atten['Timestamp'] < lec_start, 'Timestamp'] = lec_start
    atten.loc[atten['Timestamp'] > lec_end, 'Timestamp'] = lec_end
    # iterate on every attendance record
    for index, stu_row in atten.iterrows():
        if index == 0:
            continue
        ua = stu_row['User Action']
        if ua == 'Joined' or ua == 'Joined before':
            delta = lec_end - stu_row['Timestamp']
        else:
            delta = stu_row['Timestamp'] - lec_end
        Names.loc[index, new_col] += delta

    # convert to minutes
    Names[new_col] = Names[new_col].map(lambda x: round(x.total_seconds()/60., 1))
# calculate the number of absences
Names['Absence'] = np.sum(Names.iloc[:, 2:] < min_time, axis=1)

Names.to_excel('Result_file.xlsx')

