import os

def create_files_and_folders():
    # Create the 'build' folder if it doesn't exist
    build_folder = 'build'
    os.makedirs(build_folder, exist_ok=True)

    # List of folder names
    folder_names = ['folder1', 'folder2', 'folder3', 'folder4']

    # Create subfolders inside the 'build' folder
    for folder_name in folder_names:
        folder_path = os.path.join(build_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Write a file inside each subfolder
        file_content = f"This is a file inside {folder_name}."
        file_path = os.path.join(folder_path, f"{folder_name}_file.txt")
        with open(file_path, 'w') as file:
            file.write(file_content)

if __name__ == "__main__":
    create_files_and_folders()
