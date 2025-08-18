import pyautogui as pag
import tkinter as tk
import time as t
speed = 1.0 
click_active = False 
click_job = None 
version="1.0.2"
# --- Functions for button actions ---

def start_clicking():
    global click_active, speed, click_job
    click_active = True

    try:
        entered_speed = float(speed_entry.get())
        if entered_speed <= 0.0:
            status_label.config(text="Invalid speed (must be > 0)")
            click_active = False
            return
        speed = entered_speed
    except ValueError:
        status_label.config(text="Invalid speed (enter a number)")
        click_active = False
        return

    status_label.config(text=f"Clicking at {speed}s interval...")
    print(f"Starting clicking at {speed}s interval.")
    # Start the clicking process
    perform_click()

def stop_clicking():
    global click_active, click_job
    click_active = False
    if click_job:
        window.after_cancel(click_job) # Cancel any pending 'after' calls
        click_job = None
    status_label.config(text="Stopped")
    print("Stopped Clicking.")

def perform_click():
    """Performs a single click and schedules the next one."""
    global click_active, click_job
    if click_active:
        pag.click()
        # window.after expects milliseconds, so multiply speed by 1000
        click_job = window.after(int(speed * 1000), perform_click)
    else:
        status_label.config(text="Stopped")

def sendMouseto(event):
    """Send the mouse to x, y and start clicking."""
    x=int(coordsx_input.get())
    y=int(coordsy_input.get())
    pag.moveto(x, y)
    print("Sent mouse to ({x}, {y})")
    start_clicking()

# --- Tkinter GUI Setup ---

window = tk.Tk()
window.title(f"TG Autoclicker v{version}")
window.attributes("-topmost", True)
window.configure(bg="#2C2C2C")
label_ = tk.Label(window, text=f"TG Autoclicker v{version}\nhttps://github.com/BridgesPrivateDectectivesInc/tg-autoclicker")
label_.pack(pady=30, padx=10)
label_.configure(bg="#2C2C2C", fg="white", font="Arial")

# Speed input
speed_label = tk.Label(window, text="Click Speed (seconds):")
speed_label.pack(pady=5)
speed_label.configure(bg="#2C2C2C", fg="white", font="Arial")
speed_entry = tk.Entry(window)
speed_entry.insert(0, "0.5") # Default value
speed_entry.pack(padx=25, pady=5)
speed_entry.configure(bg="#4C4B4B", fg="white", font="Arial")

# Coords inputs
coordsx_label = tk.Label(window, text="X Coordinate:")
coordsx_label.pack(pady=5)
coordsx_label.configure(bg="#2C2C2C", fg="white", font="Arial")

coordsx_input = tk.Entry(window)
coordsx_input.insert(0, "100")
coordsx_input.pack(padx=25, pady=6)
coordsx_input.configure(bg="#4C4B4B", fg="white", font="Arial")

coordsy_label = tk.Label(window, text="Y Coordinate:")
coordsy_label.pack(pady=5)
coordsy_label.configure(bg="#2C2C2C", fg="white", font="Arial")

coordsy_input = tk.Entry(window)
coordsy_input.insert(0, "100")
coordsy_input.pack(padx=25, pady=6)
coordsy_input.configure(bg="#4C4B4B", fg="white", font="Arial")
# Buttons
beginClicking = tk.Button(window, text="Start clicking!", command=start_clicking)
beginClicking.pack(padx=25, pady=10)
beginClicking.configure(bg="#2C2C2C", fg="white", font="Arial")

stopClicking = tk.Button(window, text="Stop clicking!", command=stop_clicking)
stopClicking.pack(padx=25, pady=10)
stopClicking.configure(bg="#2C2C2C", fg="white", font="Arial")

clickAtCoords = tk.Button(window, text="Click at Coordinates!", command=sendMouseto)
clickAtCoords.pack(padx=25, pady=10)
clickAtCoords.configure(bg="#2C2C2C", fg="white", font="Arial")

# Status label
status_label = tk.Label(window, text="Status: Ready", fg="lime")
status_label.pack(pady=10)
status_label.configure(bg="#2C2C2C", font="Arial")

# PyAutoGUI Failsafe warning
failsafe_info = tk.Label(window, text="To force stop, slam mouse to any corner.", fg="red")
failsafe_info.pack(pady=5)
failsafe_info.configure(bg="#2C2C2C",font="Arial")

window.mainloop()
