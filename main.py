from pygame import mixer
from tkinter import Tk, PhotoImage, Button, Scale, HORIZONTAL, Menu, messagebox, filedialog, Label, SUNKEN, BOTTOM
from tkinter import X, W
import os


def play_music():
    try:
        mixer.music.load(dir_name)
        mixer.music.play()
        status["text"] = "Playing "+os.path.basename(dir_name)
    except NameError:
        messagebox.showerror("ERROR", "No file has been added!")


def pause_music():
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


root = Tk()
mixer.init()

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

root.geometry("400x400")
root.title("MegaAmp")
root.iconbitmap(r"icon.ico")

play_btn = Button(root, image=playPhoto, command=play_music)
play_btn.pack()

pause_btn = Button(root, image=pausePhoto, command=pause_music)
pause_btn.pack()

stop_btn = Button(root, image=stopPhoto, command=stop_music)
stop_btn.pack()

scale = Scale(root, from_=0, to_=100, orient=HORIZONTAL, command=set_vol)
scale.set(80)
mixer.music.set_volume(0.8)
scale.pack()

status = Label(root, text="Welcome to MegaAmp", relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
