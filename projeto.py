from time import sleep

# Define color codes
c = ('\033[m',          # 0= reset
     "\033[01;30;41m",  # 1= red
     "\033[01;30;42m",  # 2= green
     "\033[01;30;43m",  # 3= yellow
     "\033[0;47m"       # 4= white
    )

def help_system(command):
    title(f'Accessing the manual of the command \'{command}\'', 4)
    try:
        print(c[4], end='')
        help(command)
    except Exception as e:
        print(c[1], end='')
        print(f"Error: {e}")
    finally:
        print(c[0], end='')
    sleep(0.5)

def title(msg, color=0):
    length = len(msg) + 4
    print(c[color], end='')
    print('~' * length)
    print(f"  {msg}")
    print('~' * length)
    print(c[0], end='')
    sleep(0.5)


# Main Content #
command = ''
while True:
    title("PyHELP HELP SYSTEM", 2)
    command = str(input("Function or library: "))
    if command.upper() == 'END':
        break
    else:
        help_system(command)
        
print(c[1] + "See you later!" + c[0])