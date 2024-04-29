# More like text area

#Bug settings fore isnt working find a fix def fore

from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser

# App icon


def fore():
    # global a
    a = colorchooser.askcolor()
    print(a)
    textarea.config(fg=a[1])

def back():
    # global a
    
    a = colorchooser.askcolor()
    print(a)
    textarea.config(bg=a[1])

def erase():
    textarea.delete("1.0",END)

def filesave():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                     filetypes=[("Txt file",".txt"),
                                                ("word",".docx")])
    filetxt = textarea.get(1.0,END)
    file.write(filetxt)
    file.close()

# Setings

def set():
    window1 = Toplevel()
    window1.geometry("200x110")

    

    label1 = Label(window1,text="Change your font color:")
    label1.pack()

    button1 = Button(window1,text="FOREGROUND", command=fore)
    button1.pack()

    label2 = Label(window1,text="Change your page color:")
    label2.pack()

    button2 = Button(window1,text="BACKGROUND", command=back)
    
    button2.pack()

    window1.mainloop()

# Main wframe
window = Tk()

frame = Frame(window)
frame.pack()

# window.geometry("300x380")
window.config(bg="white")

icon = PhotoImage(file='icon.png')
window.iconphoto(True,icon)

window.title("Notto")

textarea = Text(frame, font=("arial",18),
                width=20, height=10,
                padx=8,pady=8, bg="#ffffbc" )
textarea.pack()

settings = Button(frame,text="Settings",command=set)
settings.pack(side=RIGHT)

save = Button(frame,text="Save",command=filesave,)
save.pack(side=RIGHT)

erase = Button(frame,text="Erase",command=erase,)
erase.pack(side=RIGHT)
# erase.place(x=100, y=200)


#settings








window.mainloop()
