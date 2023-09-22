from datetime import datetime
import os
# get current date & time
x = datetime.now()



file_name= "result.json"
path = 'C:\Projects\kev_cve_import'
# with name as day-month-year-hours-minutes-seconds
file = x.strftime('%d-%m-%Y-%H-%M-%S')
output_file = os.path.join(path, file_name)
with open("output_file", "w") as json_file:
    json_file.write(file)
