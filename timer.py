import time

seconds = float(0)
minutes = int(0)
hours = int(0)
TR = 'n'

#divider line.
def div():
    print('\n'+'  '+ 68*'-'+'\n')  

div()
    
while(True):
    try:
        minutes = int(input("\t\tSet Work Session Duration (minutes): "))
        break
    except ValueError:
        print("Invalid Value, try entering an integer.")

while (TR.lower()!="y"):
    TR = input("\t\t READY TO GET SOME WORK DONE (y/n): ")
    if (TR.lower() == 'n'):
        exit()

print ('\n\t\t\t    Timer started')

while(True):
    
    try:
        print ("\t\t\tWorking : {:02d}:{:02d}:{:05.2f}".format(hours, minutes, seconds), end = "\r")
        time.sleep(0.01)
        seconds -= 0.01
        
        if seconds < 0:
            seconds = 59.99
            minutes -= 1
        
        if minutes < 0:
            break
    
    except KeyboardInterrupt:
        decision = input("\t\t     FORFIET WORK SESSION(y/n): ")
        if decision.lower() == 'y':
            print ("\t\t    LAST WORK SESSION: {:02d}:{:02d}:{:05.2f}".format(hours, minutes, seconds))
            div()
            exit()
        else:
            continue

print ("\t\t       Work Session Completed!")
div()