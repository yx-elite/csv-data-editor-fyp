import os

def count_files_in_directory(directory):
    count = 0
    for _, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.png'):
                count += 1
    return count

directory_path = 'comparison_data'
files_count = count_files_in_directory(directory_path)
print("Number of files in directory:", files_count)
