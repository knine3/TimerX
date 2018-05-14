import time

seconds = float(0)
minutes = int(0)
hours = int(0)
TR = 'n'

while (TR.lower()=="n"):
    TR = input("Start Timer: (y/n)")

while TR.lower() == 'y':
    if seconds > 59:
        seconds = 0
        minutes += 1
    
    if minutes > 59:
        mintues = 0
        hours += 1
    
    print ("timer: {:02d}:{:02d}:{:05.2f}".format(hours, minutes, seconds), end = "\r")
    time.sleep(0.01)
    seconds += 0.01
    
    if minutes == 1:
        break
    