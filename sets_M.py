#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import csv

# A script to create a directory structure for the M_variables files as stated in KUENM R package
def get_files_to_copy(filenames, subdir):
    """Returns a list of the files to be copied for the given filenames and subdirectory."""
    files_to_copy = []
    for filename in os.listdir(subdir):
        # Check if the file is in the list of filenames to copy
        for f in filenames:
            if f in filename:
                files_to_copy.append(filename)
    return files_to_copy

# Create the M_variables directory
m_variables_dir = 'M_variables'
if not os.path.exists(m_variables_dir):
    os.makedirs(m_variables_dir)

# Open the CSV file
with open('sets.csv', 'r') as f:
    reader = csv.reader(f)
    # Create a dictionary with the values from the CSV file, skipping empty fields
    thresholds = {row[0]: [x for x in row[1:] if x] for row in reader}

# Loop through the threshold values
for threshold, filenames in thresholds.items():
    # Create a new directory with the threshold value (without the '.')
    new_dir = threshold.replace('.', '')
    new_dir_path = os.path.join(m_variables_dir, new_dir)
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)
    # Get the list of files to be copied for the current threshold value
    files_to_copy = get_files_to_copy(filenames, '.')
    # Loop through the files to be copied
    for filename in files_to_copy:
        # Build the source and destination paths
        src_path = os.path.join('.', filename)
        dst_path = os.path.join(new_dir_path, filename)
        # Copy the file
        shutil.copy(src_path, dst_path)
