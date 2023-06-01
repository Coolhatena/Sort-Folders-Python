import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def moveFile(original_path, destination_path):
	shutil.move(original_path, destination_path)

def sort():

	path = path_txtvar.get() # Get value of the tkinter var 

	is_path = os.path.exists(path)
	if is_path:
		# Set value of the file categories with extensions
		file_categories = [
			["Images", ["jpg", "png", "jpeg", "vsg"]],
			["Docs", ["docx", "txt", "pdf", "epub"]],
			["Audio", ["mp3", "wav", "flac"]],
			["Video", ["mp4", "avi", "mov", "gif"]],
			["Compressed", ["rar", "zip"]],
			["Executables", ["exe", "msi", "jar"]],
			["Code", ["m"]],
			["Other", ["iso", "log"]],
		]

		# Create folders for file categories
		for file_category in file_categories:
			category_name = file_category[0]
			try:
				os.mkdir(os.path.join(path, category_name))
				print(f"Folder \"{category_name}\" created")
			except OSError as error:
				print(f"Folder \"{category_name}\" already exist")

		# Move the files from the original path to the the corresponding category folder
		files_on_path = os.listdir(path)
		#for file in files_on_path: print(file)
		for file in files_on_path:
			filename_split = file.split(".")
			file_extension = filename_split[-1].lower()

			for file_category in file_categories:
				if file_extension in file_category[1]:
					original_path = os.path.join(path, file)
					file_type_folder_path = os.path.join(path, file_category[0])
					destination_path = os.path.join(file_type_folder_path, file)
					moveFile(original_path, destination_path)

		messagebox.showinfo("Success", "Folder sorted successfully")
	else:
		messagebox.showerror("Error", "Cannot access the selected path")
        

# Window configurations
main_window = tk.Tk()
main_window.title("Sort folder")
main_window.geometry("500x100")

# Tk variables declaration
path_txtvar = tk.StringVar()

# Build window elements
ttk.Label(main_window, text="Path to folder: ", justify=tk.LEFT)\
    .pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

path_input = tk.Entry(main_window, textvariable=path_txtvar)
path_input.insert(0, "C:\\Users\\<user>\\Downloads")
path_input.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

ttk.Button(main_window, text="Sort", command=lambda: sort())\
    .pack(side=tk.LEFT, padx=10, pady=5)

# Start window Mainloop
main_window.mainloop()