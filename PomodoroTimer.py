# Study Flower Pomodoro Timer
# This is my creative-coding project for the Code Prototype assignment.
# It combines time management (Pomodoro) with a visual feedback system -
# a flower that grows when I work and shrinks when I rest.
# I wanted it to feel calming and motivational, not just functional.


import tkinter as tk
import math

# Timer Settings
# I kept the times short for quick testing (10 sceonds = 1 Pomodoro round)
# Normally the duration should be 25 minutes per round
WORK_TIME = 10
BREAK_TIME = 10

remaining = WORK_TIME        # keeps track of remaining seconds
phase = "idle"               # can be 'work', 'break', or 'idle'
after_id = None              # used to control the repeating timer loop

# Main UI For The App
root = tk.Tk()
root.title("Study Flower 🌸 Pomodoro Timer")
root.configure(bg="pink")    # pink background to make it cheerful and calm


# Canvas Where The Flower Will Be Drawn
W, H = 360, 420
canvas = tk.Canvas(root, width=W, height=H, bg="white", highlightthickness=0)
canvas.pack(pady=10)


# Timer Label (for minutes and seconds)
label = tk.Label(root, text="00:00", font=("Arial", 40, "bold"), fg="black", bg="pink")
label.pack(pady=10)


# Motivation text changes based on progress
motivation = tk.Label(root, text="", font=("Arial", 16), fg="black", bg="pink")
motivation.pack(pady=8)

btn_start = None
btn_water = None

# --- This is where I draw the flower (Throguh canvas) ---
def draw_bloom(canvas, cx, cy, r=28):
    # I drew a simple flower using circles and ovals. 
    # I used math functions (cos/sin) to position the petals evenly
    canvas.delete("all")

    # Draw the ground
    canvas.create_oval(-40, H-70, W+40, H-20, fill="#c8e6c9", outline="")


    # Draw the stem
    stem_top_y = cy + r * 0.6
    canvas.create_line(cx, H-80, cx, stem_top_y, width=8, fill="#2e7d32", capstyle=tk.ROUND)


    # Draw the leaves on both sides
    canvas.create_oval(cx-70, H-130, cx-20, H-90, fill="#43a047", outline="")
    canvas.create_oval(cx+20, H-130, cx+70, H-90, fill="#43a047", outline="")


    # Draw the flower center
    canvas.create_oval(cx-r*0.6, cy-r*0.6, cx+r*0.6, cy+r*0.6, fill="#fdd733", outline="")


    # Draw the petals around the center (6 petals using trigonometry)
    for i in range(6):
        ang = i * math.pi / 3
        px = cx + math.cos(ang) * (r * 1.2)
        py = cy + math.sin(ang) * (r * 1.2)
        canvas.create_oval(px-r, py-r*0.8, px+r, py+r*0.8, fill="#ec407a", outline="")


# Flower sizes
BIG_R = 40
SMALL_R = 15

# Timer Helper Functions
def format_mmss(seconds: int) -> str:
    # Turns seconds into a mm:ss string (e.g. 23:30)
    m, s = divmod(max(0, seconds), 60)
    return f"{m:02d}:{s:02d}"

def cancel_after():
    #Stops any running timer loop to avoid overlap.
    global after_id
    if after_id is not None:
        try:
            root.after_cancel(after_id)
        except Exception:
            pass
        after_id = None

def schedule_next():
    #Schedules the timer to update every second. 
    global after_id
    cancel_after()
    after_id = root.after(1000, update_timer)

# The Main Timer Loop
def update_timer():
    # This function runs every second to update the countdown.
    global remaining, phase
    label.config(text=format_mmss(remaining))

    if remaining > 0:
        remaining -= 1
        schedule_next()
        return

    # When time runs out
    if phase == "work":
        # After work, start break - flower stays blooming
        motivation.config(text="Wonderful work! Time for a break 🌼")
        draw_bloom(canvas, W // 2, 150, r=BIG_R)  # stays big
        start_break()
    elif phase == "break":
        # After break, the flower wilt (shrink)
        label.config(text="Break over!")
        motivation.config(text="Revive the flower to restart 🌱")
        draw_bloom(canvas, W // 2, 150, r=SMALL_R)
        show_water_button()
        cancel_after()


# Phase Controls
def start_work():
    # Starts the work phase and makes the flower bloom. 
    global remaining, phase
    cancel_after()
    phase = "work"
    remaining = WORK_TIME
    label.config(text=format_mmss(remaining), fg="black")
    motivation.config(text="You got this! Stay focused 💪")

    # When work starts, flower grows
    draw_bloom(canvas, W // 2, 150, r=BIG_R)

    # Hide extra buttons
    hide_start_button()  # hides start button once click for the first time
    hide_water_button()
    schedule_next()

def start_break():
    # Swithces to break time and keeps flower big.
    global remaining, phase
    cancel_after()
    phase = "break"
    remaining = BREAK_TIME
    label.config(text=format_mmss(remaining), fg="purple")
    draw_bloom(canvas, W // 2, 150, r=BIG_R)
    schedule_next()

# Button Callbakcs
def on_start_clicked():
    # Triggered when the 'Start Study Session' button is clicked.
    start_work()

def on_water_clicked():
    # Triggered after a break — restarts the work timer.
    hide_water_button()
    start_work()


# Button Helpers
def show_water_button():
    # Displays the 'Water the Flower' button after break ends.
    global btn_water
    if btn_water is None:
        btn_water = tk.Button(
            root, text="Water the Flower 🌸", font=("Arial", 16, "bold"),
            command=on_water_clicked, bg="hotpink", fg="white",
            activebackground="deeppink", bd=0, padx=14, pady=8
        )
    btn_water.pack(pady=10)

def hide_water_button():
    # Hides the 'Water' button when the timer starts again
    if btn_water is not None:
        btn_water.pack_forget()

def hide_start_button():  # Hide Start button after first click
    btn_start.pack_forget()

# Start Button
btn_start = tk.Button(
    root, text="Start Study Session", font=("Arial", 16, "bold"),
    command=on_start_clicked, bg="hotpink", fg="white",
    activebackground="deeppink", bd=0, padx=14, pady=8
)
btn_start.pack(pady=10)

# Initial State
# When the app opens, the flower starts small until the session begins
draw_bloom(canvas, W // 2, 150, r=SMALL_R)
label.config(text=format_mmss(remaining))

# Run The Appp
root.mainloop()
