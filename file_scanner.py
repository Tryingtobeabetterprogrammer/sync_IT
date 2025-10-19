# file_scanner.py
import os
import hashlib

class FileScanner:
    def __init__(self):
        pass

    def get_file_hash(self, filepath):
        """Compute SHA-256 hash for a given file"""
        sha256 = hashlib.sha256()
        try:
            with open(filepath, "rb") as f:
                while chunk := f.read(8192):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception as e:
            return None

    def scan_folder(self, folder_path):
        """Returns dictionary: {relative_path: file_hash}"""
        files_dict = {}
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, folder_path)
                file_hash = self.get_file_hash(full_path)
                if file_hash:
                    files_dict[rel_path] = file_hash
        return files_dict
