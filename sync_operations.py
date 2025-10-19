# sync_operations.py
import os
import shutil
from concurrent.futures import ThreadPoolExecutor

class SyncOperation:
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=5)

    def perform_sync(self, src_folder, dest_folder):
        tasks = []
        for root, _, files in os.walk(src_folder):
            for file in files:
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, src_folder)
                dest_path = os.path.join(dest_folder, rel_path)

                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                tasks.append(self.executor.submit(shutil.copy2, src_path, dest_path))

        return f"Started {len(tasks)} file sync operations..."
