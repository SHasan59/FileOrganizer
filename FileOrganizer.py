import os
import shutil

desktop_path = "C:\\Users\\Hasan\\Desktop"


def move_files(source_dir, target_dir, extension):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    # Move files with specified extension to target directory
    for file in os.listdir(source_dir):
        if file.endswith(extension):
            shutil.move(os.path.join(source_dir, file), target_dir)


# Move .txt files to 'TXT FILES' directory
move_files(desktop_path, os.path.join(desktop_path, "TXT FILES"), ".txt")

# Move .pdf files to 'PDF FILES' directory
move_files(desktop_path, os.path.join(desktop_path, "PDF FILES"), ".pdf")

# Move .jpg files to 'JPG FILES' directory
move_files(desktop_path, os.path.join(desktop_path, "JPG FILES"), ".jpg")

# Move .zip files to 'ZIP FILES' directory
move_files(desktop_path, os.path.join(desktop_path, "ZIP FILES"), ".zip")
