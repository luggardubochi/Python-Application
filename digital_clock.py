from tkinter import *
from tkinter import messagebox
import time
import threading

# ------------------- MAIN WINDOW -------------------
app_window = Tk()
app_window.title("Sophisticated Digital Clock")
app_window.geometry("500x300")
app_window.resizable(False, False)
app_window.config(bg="#f2e750")

# ------------------- FONTS & COLORS -------------------
time_font = ("Boulder", 60, "bold")
date_font = ("Helvetica", 16)
day_font = ("Helvetica", 16, "bold")

light_theme = {"bg": "#f2e750", "fg": "#363529"}
dark_theme = {"bg": "#222", "fg": "#00FFDD"}

current_theme = light_theme

# ------------------- LABELS -------------------
time_label = Label(app_window, font=time_font, bg=current_theme["bg"], fg=current_theme["fg"])
time_label.pack(pady=10)

date_label = Label(app_window, font=date_font, bg=current_theme["bg"], fg=current_theme["fg"])
date_label.pack()

day_label = Label(app_window, font=day_font, bg=current_theme["bg"], fg=current_theme["fg"])
day_label.pack(pady=5)

# ------------------- ALARM FEATURE -------------------
alarm_time = None

def set_alarm():
    global alarm_time
    alarm_time = alarm_entry.get()
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    alarm_entry.delete(0, END)

def check_alarm():
    while True:
        if alarm_time:
            current_time = time.strftime("%H:%M")
            if current_time == alarm_time:
                messagebox.showwarning("Alarm", "⏰ Time's up!")
                break
        time.sleep(30)  # check every 30 seconds

# Run alarm checking in a separate thread
threading.Thread(target=check_alarm, daemon=True).start()

# ------------------- CLOCK FUNCTION -------------------
use_24_hour = True

def update_clock():
    current_time = time.strftime("%H:%M:%S") if use_24_hour else time.strftime("%I:%M:%S %p")
    current_date = time.strftime("%d %B %Y")
    current_day = time.strftime("%A")

    time_label.config(text=current_time)
    date_label.config(text=current_date)
    day_label.config(text=current_day)

    app_window.after(1000, update_clock)

# ------------------- THEME TOGGLE -------------------
def toggle_theme():
    global current_theme
    current_theme = dark_theme if current_theme == light_theme else light_theme

    app_window.config(bg=current_theme["bg"])
    for lbl in [time_label, date_label, day_label]:
        lbl.config(bg=current_theme["bg"], fg=current_theme["fg"])

# ------------------- 12/24 HOUR TOGGLE -------------------
def toggle_format():
    global use_24_hour
    use_24_hour = not use_24_hour

# ------------------- BUTTONS -------------------
button_frame = Frame(app_window, bg=current_theme["bg"])
button_frame.pack(pady=10)

Button(button_frame, text="Toggle 12/24H", command=toggle_format, bg="#fff", fg="#000", padx=10).grid(row=0, column=0, padx=5)
Button(button_frame, text="Theme", command=toggle_theme, bg="#fff", fg="#000", padx=10).grid(row=0, column=1, padx=5)

# ------------------- ALARM SETTER -------------------
alarm_frame = Frame(app_window, bg=current_theme["bg"])
alarm_frame.pack(pady=10)

Label(alarm_frame, text="Set Alarm (HH:MM):", bg=current_theme["bg"], fg=current_theme["fg"]).grid(row=0, column=0)
alarm_entry = Entry(alarm_frame, width=10)
alarm_entry.grid(row=0, column=1, padx=5)
Button(alarm_frame, text="Set", command=set_alarm, bg="#fff", fg="#000").grid(row=0, column=2)

# ------------------- START -------------------
update_clock()
app_window.mainloop()
