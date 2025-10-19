# sync_manager.py
from sync_operations import SyncOperation

class SyncManager:
    def __init__(self):
        self.operation = SyncOperation()

    def compare_folders(self, src_data, dest_data):
        added = [f for f in src_data if f not in dest_data]
        deleted = [f for f in dest_data if f not in src_data]
        modified = [f for f in src_data if f in dest_data and src_data[f] != dest_data[f]]

        return f"Added: {len(added)}, Deleted: {len(deleted)}, Modified: {len(modified)}"

    def sync(self, src_folder, dest_folder):
        log = self.operation.perform_sync(src_folder, dest_folder)
        return log
