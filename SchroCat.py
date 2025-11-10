from tkinter import *
from PIL import Image,ImageTk
from qiskit.quantum_info import Statevector
from numpy import sqrt

click_enabled = True

def load_and_resize_image(filename,size):
    img = Image.open(filename)
    img = img.resize(size)
    return ImageTk.PhotoImage(img)

def measure(event):
    global click_enabled
    v = Statevector([1/sqrt(2), 1/sqrt(2)])
    outcome = v.measure()[0]
    if click_enabled == True:
        if outcome == '1':
            state.config(text="ALIVE!")
            box.config(image=alive_img)
            click_enabled = False
            window.after(2500, reset_box)
        else:
            state.config(text="DEAD!")
            box.config(image=dead_img)
            click_enabled = False
            window.after(2500, reset_box)

def reset_box():
    global click_enabled
    click_enabled = True
    state.config(text='SUPERPOSITION!')
    box.config(image=box_img)

window = Tk()
window.config(bg='black')
window.bind('<Button-1>', measure)
window.bind('<space>', measure)
window.title("SchröCat")
window.iconphoto=(True, PhotoImage(file='psi.png'))
window.geometry('350x400')
window.minsize(350,400)
window.maxsize(350,400)

box_img = load_and_resize_image('box.png', (220,220))
alive_img = load_and_resize_image('alive.png', (250,250))
dead_img = load_and_resize_image('dead.png', (250,250))

label = Label(text = "SchröCat",
                bg='black',
                fg='white',
                font=('',35,'bold'))
label.pack()

state = Label(text='SUPERPOSITION!',
                bg='black',
                fg='white',
                font=('',15,'bold'))
state.pack()

box = Label(image=box_img,
            borderwidth=0,
            highlightthickness=0,
            bg='black',
            activebackground='black')
box.pack()

window.mainloop()

