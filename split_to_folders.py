import os
import shutil

# Set the folder where your .wav files are located
source_folder = "<root>/translated"
output_folder = "<root>/split"

# Define the number of files per folder
files_per_folder = 8488

# Function to move files into folders
def split_files():
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all .wav files in the source folder
    wav_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.wav')]
    total_files = len(wav_files)
    print(f"Total .wav files: {total_files}")

    # Split the files into numbered folders
    folder_number = 1
    for i in range(0, total_files, files_per_folder):
        # Create a new folder for each batch
        folder_name = os.path.join(output_folder, f"folder_{folder_number}")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Get the subset of files for this folder
        files_to_move = wav_files[i:i + files_per_folder]
        
        # Move the files into the folder
        for file_name in files_to_move:
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(folder_name, file_name)
            shutil.move(source_path, destination_path)

        print(f"Moved {len(files_to_move)} files to {folder_name}")
        folder_number += 1

    print("All files have been moved into folders.")

if __name__ == "__main__":
    split_files()
