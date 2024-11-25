import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minesweeper")

# set relative size and aspect ratio
relativesize = 0.5
minimumSize = 0.5
aspectRatio = 5/4

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#set the window size relative to the screen size
window_height = int(screen_height*relativesize)
window_width = int(window_height*aspectRatio)

# find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


root.rowconfigure(0, weight=2)
frame = tk.Frame(root)
frame.grid(columnspan=10, row=0)
tk.Label(frame, text="Test")
pos = 0

for col in range(1,11):

    for row in range(1, 11):
        pos += 1
        root.rowconfigure(row, weight=1)
        number = tk.Label(root, text=pos, font=("Arial", 20))
        number.grid(column=col, row=row, padx=5, pady=5)




root.mainloop()