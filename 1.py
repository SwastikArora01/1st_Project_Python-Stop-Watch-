import tkinter as tk
import tkinter.messagebox

def update_time():
    global time, running

    if running:
        time += 1
        clock.config(text=calculate_time())

    window.after(1000, update_time)  # Update time every 1 second

def calculate_time():
    hours = time // 3606
    mins = (time // 60) % 60
    secs = time % 60
    return "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)

def start():
    global running
    running = True
    update_time()

def reset():
    global time, running
    time = 0
    running = False
    clock.config(text="00:00:00")

def quit_app():
    window.destroy()

def handle_entry(event):
    # Functionality for handling user input in the entry field can be added here.
    # For example, validate the input as a time format.
    pass

def pause():
    global running
    running = not running  # Toggle running state on each pause click

def resume():
    global running
    if not running:  # Only resume if currently paused
        running = True

running = False
time = 0

window = tk.Tk()
window.title("Stopwatch")

clock = tk.Label(window, text="00:00:00", font=("Courier", 20))
clock.grid(row=1, column=1, stick="S")

time_label = tk.Label(window, text="hour min sec", font=("Courier", 10), width=15)
time_label.grid(row=2, column=1, sticky="N")

start_button = tk.Button(window, text="Start", command=start)
start_button.grid(row=3, column=0, sticky="NE")

reset_button = tk.Button(window, text="Reset", command=reset)
reset_button.grid(row=3, column=1, sticky="NW")

pause_button = tk.Button(window, text="Pause", command=pause)
pause_button.grid(row=3, column=2, sticky="NW")  # Adjust position if necessary

resume_button = tk.Button(window, text="Resume", command=resume)
resume_button.grid(row=3, column=3, sticky="NE")  # Adjust position if necessary

time_entry = tk.Entry(window)
time_entry.grid(row=0, column=1)
time_entry.bind("<Key>", handle_entry)

window.bind("<Return>", start)  # Start on Enter key press

window.mainloop()