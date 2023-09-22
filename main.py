
import os
from datetime import datetime
#import requests

# get current date & time
x = datetime.now()


# with name as day-month-year-hours-minutes-seconds
var = x.strftime('%d-%m-%Y-%H-%M-%S')
with open("output.json", 'w') as fp:
    fp.write(var)


