from pygame import mixer
from tkinter import Tk, PhotoImage, Button, Scale, HORIZONTAL, Menu, messagebox, filedialog, Label, SUNKEN, BOTTOM
from tkinter import X, W, Frame, LEFT
import os

muted = False
paused = False


def play_music():
    global paused
    try:
        paused
    except NameError:
        try:
            mixer.music.load(dir_name)
            mixer.music.play()
            status["text"] = "Playing "+os.path.basename(dir_name)
        except NameError:
            messagebox.showerror("ERROR", "No file has been added!")
    else:
        mixer.music.unpause()
        status["text"] = "Playing " + os.path.basename(dir_name)
        paused = False


def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    status["text"] = "Paused"


def stop_music():
    mixer.music.stop()
    status["text"] = "Stopped"


def set_vol(val):
    vol = int(val)/100
    mixer.music.set_volume(vol)


def about():
    messagebox.showinfo('About MegaAmp', 'Made by Funky_M0nk as a means to pass time.')


def browse():
    global dir_name
    dir_name = filedialog.askopenfilename()
    print(dir_name)


def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(0.8)
        scale.set(80)
        mute_btn.configure(image=mutePhoto)
        muted = False
    else:
        mixer.music.set_volume(0)
        scale.set(0)
        mute_btn.configure(image=unmutePhoto)
        muted = True


root = Tk()
mixer.init()

middle_frame = Frame(root)
middle_frame.pack(pady=10)

bottom_frame = Frame(root)
bottom_frame.pack(pady=10)

menu_bar = Menu(root)
root.config(menu=menu_bar)

sub_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="Open Folder", command=browse)
sub_menu.add_command(label="Exit", command=root.destroy)

sub_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=sub_menu)
sub_menu.add_command(label="About", command=about)

playPhoto = PhotoImage(file="play.png")
pausePhoto = PhotoImage(file="pause.png")
stopPhoto = PhotoImage(file="stop.png")
backPhoto = PhotoImage(file="back.png")
nextPhoto = PhotoImage(file="next.png")
mutePhoto = PhotoImage(file="mute.png")
unmutePhoto = PhotoImage(file="unmute.png")

root.title("MegaAmp")
root.iconbitmap(r"icon.ico")

rewind_btn = Button(middle_frame, image=backPhoto, command=play_music, borderwidth=0)
rewind_btn.grid(row=0, column=0, padx=10)

pause_btn = Button(middle_frame, image=pausePhoto, command=pause_music, borderwidth=0)
pause_btn.grid(row=0, column=1, padx=10)

play_btn = Button(middle_frame, image=playPhoto, command=play_music, borderwidth=0)
play_btn.grid(row=0, column=2, padx=10)

stop_btn = Button(middle_frame, image=stopPhoto, command=stop_music, borderwidth=0)
stop_btn.grid(row=0, column=3, padx=10)

next_btn = Button(middle_frame, image=nextPhoto, borderwidth=0)
next_btn.grid(row=0, column=4, padx=10)

mute_btn = Button(bottom_frame, image=mutePhoto, command=mute_music, borderwidth=0)
mute_btn.grid(row=0, column=0, padx=10)

scale = Scale(root, from_=0, to_=100, orient=HORIZONTAL, command=set_vol)
scale.set(80)
mixer.music.set_volume(0.8)
scale.pack()

status = Label(root, text="Welcome to MegaAmp", relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
