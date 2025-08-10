# ----- Image File Mover -----
# Developed by: <shreyansh pandey>
# Internship Project: CodeAlpha
# This script moves all .jpg files from one folder to another.

import os
import shutil

def show_intro():
    print("\n🖼 Image File Mover Tool")
    print("Move all JPG images from a source folder to a target folder.\n")

def move_images(src_folder, dest_folder):
    # Ensure source folder exists
    if not os.path.exists(src_folder):
        print(f"⚠ Source folder '{src_folder}' does not exist.")
        return
    
    # Create destination folder if not exists
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"📂 Created destination folder: {dest_folder}")

    moved_count = 0

    # Loop through all files in source folder
    for file_name in os.listdir(src_folder):
        if file_name.lower().endswith(".jpg"):
            source_path = os.path.join(src_folder, file_name)
            dest_path = os.path.join(dest_folder, file_name)
            
            shutil.move(source_path, dest_path)
            moved_count += 1
            print(f"✅ Moved: {file_name}")

    if moved_count == 0:
        print("⚠ No JPG files found in the source folder.")
    else:
        print(f"\n🎯 Total {moved_count} JPG files moved successfully!")

if __name__ == "__main__":
    show_intro()
    source = input("🔹 Enter source folder path: ").strip()
    destination = input("🔹 Enter destination folder path: ").strip()
    move_images(source, destination)
