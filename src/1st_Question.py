import os
import hashlib

def find_duplicate_files(directory):
    # Dictionary to store file hashes and their paths
    file_hashes = {}  
    # List to store duplicate files
    duplicates = []   

    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            with open(filepath, 'rb') as file:
                file_hash = hashlib.md5(file.read()).hexdigest()

            if file_hash in file_hashes:
                duplicates.append((filepath, file_hashes[file_hash]))
            else:
                file_hashes[file_hash] = filepath

    return duplicates
