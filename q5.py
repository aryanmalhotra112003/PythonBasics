import os
import hashlib


def get_file_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            sha256.update(chunk)

    return sha256.hexdigest()


def find_duplicates(directory):

    hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(directory):
        for file in files:

            path = os.path.join(root, file)

            try:
                file_hash = get_file_hash(path)

                if file_hash in hashes:
                    duplicates.append(path)
                else:
                    hashes[file_hash] = path

            except Exception as e:
                print("Error reading file:", path)

    return duplicates


directory = input("Enter directory to scan: ")

dups = find_duplicates(directory)

if len(dups) == 0:
    print("No duplicate files found.")
else:
    print("\nDuplicate files found:")

    for file in dups:
        print(file)
