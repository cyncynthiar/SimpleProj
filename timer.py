#python timer 
import time
import os
import sys
import osascript

"""
print("", divmod(10, 60) )
time.sleep(1) 
print("waiting")
os.system('afplay /System/Library/Sounds/Sosumi.aiff')
time_ = sys.argv[1]
print(time_)

"""
def count_down(t):
    #print("inside count_down", t)
    
    while t:
        """
        if input().strip() != "":
            break
        """
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

    #turn on systems sound

    target_volume = 50
    vol = "set volume output volume " + str(50)
    osascript.osascript(vol)

    for i in range(5):  #15
        os.system('afplay /System/Library/Sounds/Sosumi.aiff')

    
def input_timer():
    """
    """
    c = "1"
    while(c!="0"):
        time_  = input("seconds:  ")
        if not time_.isnumeric():
            print("please enter an integer for minutes")
        else:
            count_down(int(time_))
        c = input("wanna exit? type 0:   ")

def main():
    lis_t = sys.argv
    if len(lis_t) > 1:
        count_down(int(lis_t[1]))
    else: #time_ is empty
        print("enter time for the timer, 5 min = 300, 20 = 1200, 25=1500")
        input_timer()

if __name__ == '__main__':
    main()
