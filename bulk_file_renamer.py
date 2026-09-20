from pathlib import Path
folder = input("Enter the folder path: ")
folder_path = Path(folder)
if folder_path.exists():
    number = 1
    for file in folder_path.iterdir():
        if file.is_file():
            new_name = f"file_{number}{file.suffix}"
            new_path = folder_path / new_name
            file.rename(new_path)
            print(f"Renamed: {file.name} -> {new_name}")
            number += 1
        print("\nAll files renamed successfully!")
else:
    print("Folder not found.")