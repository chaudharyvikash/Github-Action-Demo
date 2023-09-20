
import os
from datetime import datetime

# get current date and time
x = datetime.now()


# with name as day-month-year-hours-minutes-seconds
file_name_2 = x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open("output.json", 'w') as fp:
    fp.write(file_name_2)

fp.close()
