import tkinter as tk
root = tk.Tk()
root.title("Simple Input and Button GUI")
root.geometry("300x150")  # Set the window sizeFunction to be called when the button is clicked


def show_input():
    user_input = entry.get()  # Get text from the entry box
    print("User input:", user_input)


label = tk.Label(root, text="Enter something:")
label.pack(pady=10)  # Add padding around the labelEntry (input block) where user can type text


entry = tk.Entry(root, width=30)
entry.pack(pady=5)


button = tk.Button(root, text="Submit", command=show_input)
button.pack(pady=10)
root.mainloop()