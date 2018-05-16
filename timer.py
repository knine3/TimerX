import time

seconds = float(0)
minutes = int(0)
hours = int(0)
TR = 'n'

#divider line.
def div():
    print('\n'+'  '+ 68*'-'+'\n')  

def formatter(message, delim='\n'):
    print ('{:^72}'.format(message), end = delim)

def deform (message):
    spaces = int((72-len(message))/2) 
    return (spaces*' ' + message)

div()
    
while(True):
    try:
        minutes = int(input(deform("Set Work Session Duration (minutes): ")))
        break
    except ValueError:
        formatter("Invalid Value, try entering an integer.")

while (TR.lower()!="y"):
    TR = input(deform("READY TO GET SOME WORK DONE (y/n): "))
    if (TR.lower() == 'n'):
        exit()

print()
formatter('Timer started')

while(True):
    
    try:
        formatter("Working : {:02d}:{:02d}:{:05.2f}".format(hours, minutes, seconds), '\r')
        time.sleep(0.01)
        seconds -= 0.01
        
        if seconds < 0:
            seconds = 59.99
            minutes -= 1
        
        if minutes < 0:
            break
    
    except KeyboardInterrupt:
        decision = input(deform("FORFIET WORK SESSION(y/n): "))
        if decision.lower() == 'y':
            formatter('Work Session Forfeited!')
            div()
            exit()
        else:
            continue

formatter ("Work Session Completed!")
div()