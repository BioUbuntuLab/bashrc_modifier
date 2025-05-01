import subprocess
import tkinter as tk
from tkinter import messagebox

def run_pipeline():
       
    try:
        # Open .bashrc with Sublime Text
        command = f"subl ~/.bashrc"
        subprocess.run(["bash", "-c", command], check=True)

    # Error hadling
    except subprocess.CalledProcessError as e:
        app.after(0, lambda: messagebox.showerror("Error", str(e)))

# Set up tkinter app
app = tk.Tk()
app.title("bashrc modifier")

# Set the window size (width x height)
app.geometry("270x50")

# Configure the grid to center the button
app.grid_rowconfigure(0, weight=1)  # Allow the row to expand
app.grid_columnconfigure(0, weight=1)  # Allow the column to expand

# Start button, using sticky to center it
tk.Button(app, text="Run program", command=run_pipeline).grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

app.mainloop()
