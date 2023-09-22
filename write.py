from datetime import datetime
import os
# get current date and time
x = datetime.now()

# with name as day-month-year-hours-minutes-seconds

file_name= "result.json"
path = 'C:\Projects\kev_cve_import'

file = x.strftime('%d-%m-%Y-%H-%M-%S')
output_file = os.path.join(path, file_name)
with open("output_file", "w") as json_file:
    json_file.write(file)
