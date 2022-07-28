import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

x = None

def timer(count = 120):
    min = math.floor(count / 60)
    sec = count % 60
    if min <= 9:
        min = f"0{min}"
    if sec <= 9:
        sec = f"0{sec}"
    global x
    if count > 0:
        canvas.itemconfig(text, text=f"{min}:{sec}")
        x = window.after(1000, timer, count - 1)
def res():
    window.after_cancel(x)
    canvas.itemconfig(text, text = "00:00")

window = Tk()
window.config(padx= 100, pady= 100, bg= YELLOW)

image = PhotoImage(file= "tomato.png")
canvas = Canvas(width=200, height= 223)
canvas.create_image(100, 112, image = image)
text = canvas.create_text(100, 130, text= "00:00", fill= "white", font= (FONT_NAME, 24, "bold"))
canvas.config(bg= YELLOW, highlightthickness= 0)
canvas.grid(column= 2, row= 2)

label = Label(text= "Timer", fg= GREEN, bg= YELLOW, font= (FONT_NAME, 30))
label.grid(column= 2, row= 1)

reset_button = Button(text= "Reset", command= res)
reset_button.grid(column= 3, row= 3)

start_button = Button(text= "Start", command= timer)
start_button.grid(column= 1, row= 3)

window.mainloop()
