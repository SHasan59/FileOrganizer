import os
import shutil
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x300")

desktop_path = "C:\\Users\\test\\Desktop"


def move_files(source_dir, target_dir, extension):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    # Move files with specified extension to target directory
    for file in os.listdir(source_dir):
        if file.endswith(extension):
            shutil.move(os.path.join(source_dir, file), target_dir)


def organize_files():
    source_dir = dir_entry.get()  # Retrieve the directory from the entry field
    move_files(source_dir, os.path.join(source_dir, "TXT FILES"), ".txt")
    move_files(source_dir, os.path.join(source_dir, "PDF FILES"), ".pdf")
    move_files(source_dir, os.path.join(source_dir, "JPG FILES"), ".jpg")
    move_files(source_dir, os.path.join(source_dir, "ZIP FILES"), ".zip")
    move_files(source_dir, os.path.join(source_dir, "PNG FILES"), ".png")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="File Organizer")
label.pack(padx=10, pady=30)

dir_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Desktop Directory", width=200)
dir_entry.insert(0, desktop_path)  # Insert desktop path into the entry field
dir_entry.pack(padx=10, pady=30)

organize_button = customtkinter.CTkButton(frame, text="Organize Files", command=organize_files)
organize_button.pack(padx=10, pady=10)

root.mainloop()
