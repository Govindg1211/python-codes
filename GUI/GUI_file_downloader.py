from file_downloder import download_file  # Ensure this module has the download_file function
import tkinter as tk

def take_input():
    url = entry.get()  # Get text from the entry box
    file_name = entry2.get()  # Get filename from the second entry box
    download_file(url, file_name)  # Call download_file with user inputs

# Create the main window
root = tk.Tk()
root.title("Simple Input and Button GUI")
root.geometry("300x250")  # Set the window size

# Create and pack label
label = tk.Label(root, text="Enter URL:")
label.pack(pady=10)

# Create and pack entry for URL
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Create and pack label for filename
label2 = tk.Label(root, text="Enter filename:")
label2.pack(pady=10)

# Create and pack entry for filename
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

# Create and pack button with command to call take_input
button = tk.Button(root, text="Submit", command=take_input)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()