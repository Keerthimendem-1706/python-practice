import os
import shutil
folder = input("Enter the folder path: ")
if os.path.exists(folder):
    documents = os.path.join(folder, "Documents")
    images = os.path.join(folder, "Images")
    videos = os.path.join(folder, "Videos")
    os.makedirs(documents, exist_ok=True)
    os.makedirs(images, exist_ok=True)
    os.makedirs(videos, exist_ok=True)
    for file in os.listdir(folder):
        file_path= os.path.join(folder, file)
        if os.path.isfile(file_path):
            if file.lower().endswith(".pdf"):
                shutil.move(file_path, documents)
            elif file.lower().endswith((".jpg",".jpeg",".png")):
                shutil.move(file_path, images)
            elif file.lower().endswith((".mp4",".avi",".mkv")):
                shutil.move(file_path, videos)
    print("Files organized successfully!")
else:
    print("Folder not found.")