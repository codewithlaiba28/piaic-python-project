import time

def countdown(minutes, seconds):
    t = minutes * 60 + seconds
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    print("Timer Completed!")  
mins = int(input("Enter minutes: "))
secs = int(input("Enter seconds: "))
countdown(mins, secs)
