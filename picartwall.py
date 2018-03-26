
from tkinter import Tk, Label, Button, E, W
import os, time, subprocess
time1 = ''
# get a list of all WAV files in Music directory
dirList= os.listdir("/home/pi/Music/")
dirList = [item for item in dirList if '.wav' in item or '.WAV' in item]
dirList.sort()

# make sure list is at least 14 records long
if len(dirList) < 14:
    for z in range (14-len(dirList)):
        dirList.append('')

print(dirList) # for debugging

# create list of filenames and titles that is 14 records long
audioList = []
for x in range(14):
    title = dirList[x][:-4]
    audioList.append([dirList[x],title[:15]])
print(audioList) # for debugging

# find RaspPi's IP address
IP = subprocess.check_output(["hostname", "-I"]).split()[0]


class cartGUI:
    def __init__(self, master):

        self.master = master
        master.title("PiCartWall")

        def play(track):
            fullPath = os.path.normpath("/home/pi/Music/"+dirList[track].replace(' ','\ '))
            os.system("aplay " + fullPath)

        self.label = Label(master, text="PiCartWall by @blogmywiki", font=('Lato Heavy',25), fg = 'blue')
        self.label.grid(columnspan=7, pady=10)

        self.button1 = Button(master, text="1", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(0))
        self.button1.grid(row=1, pady=10)

        self.button2 = Button(master, text="2", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(1))
        self.button2.grid(row=1, column=1)

        self.button3 = Button(master, text="3", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(2))
        self.button3.grid(row=1, column=2)

        self.button4 = Button(master, text="4", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(3))
        self.button4.grid(row=1, column=3)

        self.button5 = Button(master, text="5", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(4))
        self.button5.grid(row=1, column=4)

        self.button6 = Button(master, text="6", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(5))
        self.button6.grid(row=1, column=5)

        self.button7 = Button(master, text="7", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(6))
        self.button7.grid(row=1, column=6)

        self.label1 = Label(master, text=audioList[0][1])
        self.label1.grid(row=2)

        self.label2 = Label(master, text=audioList[1][1])
        self.label2.grid(row=2, column=1)

        self.label3 = Label(master, text=audioList[2][1])
        self.label3.grid(row=2, column=2)

        self.label4 = Label(master, text=audioList[3][1])
        self.label4.grid(row=2, column=3)

        self.label5 = Label(master, text=audioList[4][1])
        self.label5.grid(row=2, column=4)

        self.label6 = Label(master, text=audioList[5][1])
        self.label6.grid(row=2, column=5)

        self.label7 = Label(master, text=audioList[6][1])
        self.label7.grid(row=2, column=6)

        self.button8 = Button(master, text="8", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(7))
        self.button8.grid(row=3, pady=10)

        self.button9 = Button(master, text="9", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(8))
        self.button9.grid(row=3, column=1)

        self.button10 = Button(master, text="10", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(9))
        self.button10.grid(row=3, column=2)

        self.button11 = Button(master, text="11", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(10))
        self.button11.grid(row=3, column=3)

        self.button12 = Button(master, text="12", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(11))
        self.button12.grid(row=3, column=4)

        self.button13 = Button(master, text="13", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(12))
        self.button13.grid(row=3, column=5)

        self.button14 = Button(master, text="14", font=('Lato Heavy',55), fg = 'blue', height=1, width=2, command=lambda: play(13))
        self.button14.grid(row=3, column=6)

        self.label8 = Label(master, text=audioList[7][1])
        self.label8.grid(row=4)

        self.label9 = Label(master, text=audioList[8][1])
        self.label9.grid(row=4, column=1)

        self.label10 = Label(master, text=audioList[9][1])
        self.label10.grid(row=4, column=2)

        self.label11 = Label(master, text=audioList[10][1])
        self.label11.grid(row=4, column=3)

        self.label12 = Label(master, text=audioList[11][1])
        self.label12.grid(row=4, column=4)

        self.label13 = Label(master, text=audioList[12][1])
        self.label13.grid(row=4, column=5)

        self.label14 = Label(master, text=audioList[13][1])
        self.label14.grid(row=4, column=6)

        self.ip_button = Button(master, text="IP addr", command=self.ipaddr)
        self.ip_button.grid(row=5, pady=10)
    
        self.stop_button = Button(master, text="shut down", command=self.shutdown)
        self.stop_button.grid(row=5, column=2)

        self.close_button = Button(master, text="close app", command=self.close)
        self.close_button.grid(row=5, column=4)

        self.foo_button = Button(master, text="--", command=self.foo)
        self.foo_button.grid(row=5, column=6)

    def shutdown(self):
        print("shutting down system")
        self.label.config(text='shutting down system')
        os.system("sudo shutdown now")

    def close(self):
        root.destroy()

    def ipaddr(self):
        self.label.config(text=IP)

    def foo(self):
        os.system("")


root = Tk()

root.configure(cursor='none')
root.attributes('-fullscreen', True)
my_gui = cartGUI(root)

clock = Label(root, font=('Lato Light', 42, 'bold'), fg='gray42')
clock.grid(row=6, columnspan=7, pady=10)
def tick():
    global time1
    # get the current local time
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()

root.mainloop()
