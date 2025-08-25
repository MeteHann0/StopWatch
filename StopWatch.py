import time
import threading
from tkinter import*

second = 0
minute = 0
hour = 0
running = False

def Start():
    global hour,minute,second,running
    running = True
    while running:
        time.sleep(1)
        second+=1
        if second == 60:
            second = 0
            minute += 1
            if minute == 60:
                minute = 0           
                hour += 1
        lbl1.config(text = f"Time: {hour:02}:{minute:02}:{second:02} ")

def Stop():
    global running
    running = False
    lbl2.config(text = f"Total time: {hour} hour {minute} minute and {second} second.")

root = Tk()
root.title("StopWatch")
root.geometry("500x400")
frame = Frame(root, bg="lightgray", padx=20, pady=20)
frame.pack(pady=50)
lbl1 = Label(frame, text=f"Time: {hour:02}:{minute:02}:{second:02}", font=(20), bg="lightgray")
lbl1.pack(pady=30)
lbl2 = Label(frame, text = "", font=(14), bg="lightgray")
lbl2.pack(side=BOTTOM, pady= 40)
btnStart = Button(text="Start", command=lambda: threading.Thread(target=Start).start(), width=12, height=6)
btnStart.pack(side=LEFT, padx=50, pady=10)
btnStop = Button(text="Stop", command=Stop, width=12, height=6)
btnStop.pack(side=RIGHT, padx=50, pady=10)

root.mainloop()