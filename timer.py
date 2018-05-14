import time

seconds = float(0)
minutes = int(0)
hours = int(0)
TR = 'n'

while(True):
    try:
        overflow = int(input("Set Work Session Duration (minutes): "))
        break
    except ValueError:
        print("Invalid Value, try entering an integer.")

while (TR.lower()!="y"):
    print ("\nEnter 'y' for Yes, 'n' for No or 'e' to exit.")
    TR = input("READY TO GET SOME WORK DONE (y/n/e): ")
    if (TR.lower() == 'e'):
        exit()

print ('Timer started', end='\t\t')
print ("\t\tWork Session duration: {:02d}:{:02d}:{:05.2f}".format(hours, overflow, seconds), end = "\r" )

while(True):
    try:
        while TR.lower() == 'y':
            if seconds > 59:
                seconds = 0
                minutes += 1
            
            if minutes > 59:
                mintues = 0
                hours += 1
            
            print ("\t\tWorking: {:02d}:{:02d}:{:05.2f}".format(hours, minutes, seconds), end = "\r")
            time.sleep(0.01)
            seconds += 0.01
            
            if minutes == overflow:
                break
    
    except KeyboardInterrupt:
        decision = input("\nFORFIET WORK SESSION(y/n): ")
        if decision.lower() == 'y':
            print ("LAST WORK SESSION: {:02d}:{:02d}:{:05.2f}".format(hours, minutes, seconds))
            exit()
        else:
            continue

print ("\nWork Session Completed")    