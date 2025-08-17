import pyautogui as pag
import tkinter as tk
import time as tspeed = 1.0 
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
            status_label.config(text="Status: Invalid speed (must be > 0)")
            click_active = False
            return
        speed = entered_speed
    except ValueError:
        status_label.config(text="Status: Invalid speed (enter a number)")
        click_active = False
        return

    status_label.config(text=f"Status: Clicking at {speed}s interval...")
    print(f"Starting clicking at {speed}s interval.")
    # Start the clicking process
    perform_click()

def stop_clicking():
    global click_active, click_job
    click_active = False
    if click_job:
        window.after_cancel(click_job) # Cancel any pending 'after' calls
        click_job = None
    status_label.config(text="Status: Stopped")
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
        status_label.config(text="Status: Stopped")


# --- Tkinter GUI Setup ---

window = tk.Tk()
window.title("Autoclicker")

# Speed input
speed_label = tk.Label(window, text="Click Speed (seconds):")
speed_label.pack(pady=5)
speed_entry = tk.Entry(window)
speed_entry.insert(0, "1.0") # Default value
speed_entry.pack(padx=25, pady=5)

# Buttons
beginClicking = tk.Button(window, text="Start clicking!", command=start_clicking)
beginClicking.pack(padx=25, pady=10)

stopClicking = tk.Button(window, text="Stop clicking!", command=stop_clicking)
stopClicking.pack(padx=25, pady=10)

# Status label
status_label = tk.Label(window, text="Status: Ready", fg="blue")
status_label.pack(pady=10)

# PyAutoGUI Failsafe warning
failsafe_info = tk.Label(window, text="To force stop, slam mouse to any corner.", fg="red")
failsafe_info.pack(pady=5)

# --- Run the GUI ---
window.mainloop()
