import os
import shutil
import csv

# A script to create a directory structure for the G_variables files as stated in KUENM R package
def get_files_to_copy(filenames, subdir):
    """Returns a list of the files to be copied for the given filenames and subdirectory."""
    files_to_copy = []
    for filename in os.listdir(subdir):
        # Check if the file is in the list of filenames to copy
        base, _ = os.path.splitext(filename)
        base = base.split('.')[0]  # consider only the first part of the base name in case of multiple extensions like 'bio1.asc.aux'
        if base in filenames:
            files_to_copy.append(filename)
    return files_to_copy

# Create the G_variables directory
g_variables_dir = 'G_variables'
if not os.path.exists(g_variables_dir):
    os.makedirs(g_variables_dir)

# Open the CSV file
with open('sets.csv', 'r') as f:
    reader = csv.reader(f)
    # Create a dictionary with the values from the CSV file, skipping empty fields
    thresholds = {row[0]: [x for x in row[1:] if x] for row in reader}

# Loop through the threshold values
for threshold, filenames in thresholds.items():
    # Create a new directory with the threshold value (without the '.')
    new_dir = threshold.replace('.', '')
    new_dir_path = os.path.join(g_variables_dir, new_dir)
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)
    # Loop through the subdirectories
    for subdir in os.listdir():
        # Skip non-directories and the G_variables directory
        if not os.path.isdir(subdir) or subdir == g_variables_dir:
            continue
        # Create a new subdirectory in the new directory
        new_subdir = os.path.join(new_dir_path, subdir)
        if not os.path.exists(new_subdir):
            os.makedirs(new_subdir)
        # Get the list of files to be copied for the current subdirectory and threshold value
        files_to_copy = get_files_to_copy(filenames, subdir)
        # Loop through the files to be copied
        for filename in files_to_copy:
            # Build the source and destination paths
            src_path = os.path.join(subdir, filename)
            dst_path = os.path.join(new_subdir, filename)
            # Copy the file
            shutil.copy(src_path, dst_path)
