import pyautogui as pag
import tkinter as tk
import time as t
speed = 1.0 
click_active = False 
click_job = None 

# --- Functions for button actions ---

def start_clicking():
    global click_active, speed, click_job
    click_active = True

    try:
        # Get speed from the entry widget
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
        # Schedule the next click after 'speed' seconds
        # window.after expects milliseconds, so multiply speed by 1000
        click_job = window.after(int(speed * 1000), perform_click)
    else:
        status_label.config(text="Stopped")


# --- Tkinter GUI Setup ---

window = tk.Tk()
window.title("TG Autoclicker")
window.attributes("-topmost", True)
window.configure(bg="#2C2C2C")
label_ = tk.Label(window, text="TG Autoclicker\nhttps://github.com/BridgesPrivateDectectivesInc/tg-autoclicker")
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

# Buttons
beginClicking = tk.Button(window, text="Start clicking!", command=start_clicking)
beginClicking.pack(padx=25, pady=10)
beginClicking.configure(bg="#2C2C2C", fg="white", font="Arial")

stopClicking = tk.Button(window, text="Stop clicking!", command=stop_clicking)
stopClicking.pack(padx=25, pady=10)
stopClicking.configure(bg="#2C2C2C", fg="white", font="Arial")

# Status label
status_label = tk.Label(window, text="Status: Ready", fg="lime")
status_label.pack(pady=10)
status_label.configure(bg="#2C2C2C", font="Arial")
# PyAutoGUI Failsafe warning
failsafe_info = tk.Label(window, text="To force stop, slam mouse to any corner.", fg="red")
failsafe_info.pack(pady=5)
failsafe_info.configure(bg="#2C2C2C",font="Arial")
# --- Run the GUI ---
window.mainloop()
