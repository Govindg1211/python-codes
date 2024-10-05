import os
import tkinter as tk
from tkinter import messagebox

# Function to organize files in the specified directory
def organize_files(directory):
    # Detect the operating system using os.name
    is_windows = os.name == 'nt'
    
    # Define file categories and corresponding file extensions
    file_types = {
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audios': ['.mp3', '.wav', '.aac', '.flac'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
        'Misc': []
    }
    
    # Create folders for each file category if they don't already exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Iterate over the files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Determine the file extension
        file_extension = os.path.splitext(file_name)[1].lower()
        
        # Find the appropriate category for the file
        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                # Move the file to the corresponding folder
                destination = os.path.join(directory, folder, file_name)
                
                # Check if file already exists at the destination
                if not os.path.exists(destination):
                    if is_windows:
                        os.system(f'move "{file_path}" "{destination}"')
                    else:
                        os.system(f'mv "{file_path}" "{destination}"')
                moved = True
                break
        
        # If no matching category is found, move to the 'Misc' folder
        if not moved:
            misc_destination = os.path.join(directory, 'Misc', file_name)
            if not os.path.exists(misc_destination):
                if is_windows:
                    os.system(f'move "{file_path}" "{misc_destination}"')
                else:
                    os.system(f'mv "{file_path}" "{misc_destination}"')
    
    messagebox.showinfo("Success", "Files have been organized!")

# Function to handle button click event
def show_input():
    user_input = entry.get()  # Get text from the entry box
    if os.path.exists(user_input):
        organize_files(user_input)
    else:
        messagebox.showerror("Error", "Invalid directory path!")

# Create main application window
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")  # Set the window size

# Create label and entry for user input
label = tk.Label(root, text="Enter directory path to organize:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Create submit button
button = tk.Button(root, text="Organize Files", command=show_input)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()