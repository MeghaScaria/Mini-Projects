from tkinter import *
import pyspeedtest

# Function to check download speed and display in a custom window
def one():
    # Get download speed
    speed = pyspeedtest.SpeedTest("www.google.com")
    download_speed = speed.download()  # Speed in bits per second
    download_speed_in_MB = download_speed / 1_000_000  # Convert to MBps for better readability
    a1 = f"{download_speed_in_MB:.2f} MB per second"
    
    # Create a custom Toplevel window to show download speed
    result_window = Toplevel(root)
    result_window.title("Speed Test Result")
    result_window.geometry("400x200")
    result_window.config(bg="#ffccf0")  # Soft pink background
    
    # Label to show speed result
    label = Label(result_window, text="💖 Your Download Speed 💖", font=("Comic Sans MS", 16, "bold"), bg="#ffccf0", fg="#d5008f")
    label.pack(pady=15)
    
    # Label to display actual download speed
    speed_label = Label(result_window, text=a1, font=("Comic Sans MS", 14), bg="#ffccf0", fg="#e91e63")
    speed_label.pack(pady=10)
    
    # Button to close the result window
    close_button = Button(result_window, text="Close 💖", font=("Comic Sans MS", 12), command=result_window.destroy, bg="#d5008f", fg="white", relief="raised", width=10)
    close_button.pack(pady=15)

# Main Tkinter window setup
root = Tk()
root.title("✨ Cute Internet Speed Checker ✨")
root.config(bg="#ffccf0")  # Soft pink background
root.geometry("500x250")

# Header Label with a cute theme and font
label1 = Label(root, text="✨ Speed Test Time! ✨", font=("Comic Sans MS", 30, "bold"), bg="#ffccf0", fg="#d5008f")
label1.pack(pady=30)

# Button to check internet speed, with a cute pink theme
button1 = Button(root, text="Click to Check 🌸", font=("Comic Sans MS", 18, "bold"), bg="#ff80bf", fg="white", height=1, width=18, command=one, relief="raised")
button1.pack(pady=20)

# Mainloop
root.mainloop()
