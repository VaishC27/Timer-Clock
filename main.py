from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
tim = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global tim
    window.after_cancel(tim)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    tick.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_Sec = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long)
        timer.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short)
        timer.config(text="BREAK", fg=PINK)
    else:
        count_down(work_Sec)
        timer.config(text="WORK", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(c):
    count_min=math.floor(c/60)
    count_sec=c%60
    if count_sec <10:
        count_sec= f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if c > 0:
        global tim
        tim = window.after(1000, count_down, c-1)
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(reps/2)):
            mark+="✔"
        tick.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Timer Clock")
window.config(padx=100, pady=50, bg=YELLOW)


timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="Untitled.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 125, text="00:00", fill="black", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

tick = Label(fg=GREEN, bg=YELLOW)
tick.grid(column=1, row=3)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()