import tkinter as tk
import math

#WORK TIME
WORK_TIME = 1 * 10      
BREAK_TIME = 1 * 10

remaining = WORK_TIME
phase = "idle"
after_id = None

#UI-
root = tk.Tk()
root.title("Study Flower 🌸 Pomodoro Timer")
root.configure(bg="pink")

#CANVAS
W, H = 360, 420
canvas = tk.Canvas(root, width=W, height=H, bg="white", highlightthickness=0)
canvas.pack(pady=10)

#TIMER LABEL 
label = tk.Label(root, text="00:00", font=("Arial", 40, "bold"), fg="black", bg="pink")
label.pack(pady=10)

motivation = tk.Label(root, text="", font=("Arial", 16), fg="black", bg="pink")
motivation.pack(pady=8)

# BUTTONS
btn_start = None
btn_water = None


# DRAWING THE FLOWER
def draw_bloom(canvas, cx, cy, r=28):
    canvas.delete("all")
    # ground
    canvas.create_oval(-40, H-70, W+40, H-20, fill="#c8e6c9", outline="")
    # stem
    stem_top_y = cy + r * 0.6
    canvas.create_line(cx, H-80, cx, stem_top_y, width=8, fill="#2e7d32", capstyle=tk.ROUND)
    # leaves
    canvas.create_oval(cx-70, H-130, cx-20, H-90, fill="#43a047", outline="")
    canvas.create_oval(cx+20, H-130, cx+70, H-90, fill="#43a047", outline="")
    # center
    canvas.create_oval(cx-r*0.6, cy-r*0.6, cx+r*0.6, cy+r*0.6, fill="#fdd733", outline="")
    # petals
    for i in range(6):
        ang = i * math.pi / 3
        px = cx + math.cos(ang) * (r * 1.2)
        py = cy + math.sin(ang) * (r * 1.2)
        canvas.create_oval(px-r, py-r*0.8, px+r, py+r*0.8, fill="#ec407a", outline="")


#TIMER
def format_mmss(seconds: int) -> str:
    m, s = divmod(max(0, seconds), 60)
    return f"{m:02d}:{s:02d}"


def update_timer():
    global remaining, phase

    label.config(text=format_mmss(remaining))

    if remaining > 0:
        remaining -= 1
        root.after(1000, update_timer)
    else:
        if phase == "work":
            motivation.config(text="Wonderful work! Time for a break 🌼")
            draw_bloom(canvas, W // 2, 150, r=15)
            start_break()
        else:
            label.config(text="Break over!")
            motivation.config(text="Revive the flower to restart 🌱")
            draw_bloom(canvas, W // 2, 150, r=40)
            start_water_button()


def start_work():
    """Start study session."""
    global remaining, phase
    phase = "work"
    remaining = WORK_TIME
    label.config(text=format_mmss(remaining), fg="black")
    motivation.config(text="You got this! Stay focused 💪")
    draw_bloom(canvas, W // 2, 150, r=40)
    update_timer()


def start_break():
    """Start break session."""
    global remaining, phase
    phase = "break"
    remaining = BREAK_TIME
    label.config(text=format_mmss(remaining), fg="purple")
    update_timer()


def on_start_clicked():
    btn_start.pack_forget()
    start_work()


def on_water_clicked():
    btn_water.pack_forget()
    start_work()


def start_water_button():
    """Button appears after break ends."""
    global btn_water
    btn_water = tk.Button(
        root, text="Water the Flower 🌸", font=("Arial", 16, "bold"),
        command=on_water_clicked, bg="hotpink", fg="white",
        activebackground="deeppink", bd=0, padx=14, pady=8
    )
    btn_water.pack(pady=10)


#START BUTTON
btn_start = tk.Button(
    root, text="Start Study Session", font=("Arial", 16, "bold"),
    command=on_start_clicked, bg="hotpink", fg="white",
    activebackground="deeppink", bd=0, padx=14, pady=8
)
btn_start.pack(pady=10)


root.mainloop()
