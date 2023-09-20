import platform as os
import os
from datetime import datetime

# get current date and time
x = datetime.now()


# with name as day-month-year-hours-minutes-seconds
file_name_2 = x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open("output.json", 'w') as fp:
    fp.write(file_name_2)

print('Operating system name: ',os.system())
print('Host name: ',os.node())
print('Machine name: ',os.machine())
print('Processor name: ',os.processor())
print('Release: ',os.release())
print('Version: ',os.version())

#second method

info=os.uname()     #uname returns tuple of string
print('using tuple')
print('Operating system name: ',info.system)
print('Host name: ',info.node)
print('Machine name: ',info.machine)
print('Processor name: ',info.processor)
print('OS Release: ',info.release)
print('OS Version: ',info.version)
