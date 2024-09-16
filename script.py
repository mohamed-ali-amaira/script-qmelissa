import os
from collections import defaultdict


def rename_files_in_current_directory():
    # Get the directory where this script is located
    directory = os.path.dirname(os.path.abspath(__file__))

    # Get the list of all files in the directory
    files = os.listdir(directory)

    # Filter out directories and sort files by name (excluding extensions) in ascending order
    files = sorted(
        [f for f in files if os.path.isfile(os.path.join(directory, f))])

    # Dictionary to group files by name without extension
    name_groups = defaultdict(list)

    # Group files by their name without extension
    for filename in files:
        # Get the name without the extension
        name_without_ext = os.path.splitext(filename)[0]
        name_groups[name_without_ext].append(filename)

    # Rename the groups of files, giving the same number to files with the same name (different extensions)
    for index, (name_without_ext, file_group) in enumerate(name_groups.items(), start=1):
        for filename in file_group:
            # Get the file extension
            file_extension = os.path.splitext(filename)[1]
            # Create the new filename
            new_name = f"{index}{file_extension}"
            # Get the full path for the old and new file names
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_name}")


# Run the function
rename_files_in_current_directory()
