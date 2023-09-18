import platform as os

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
