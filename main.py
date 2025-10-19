
from tkinter import *
from tkinter import filedialog, messagebox
from file_scanner import FileScanner
from sync_manager import SyncManager

class SyncItApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sync-It : File Synchronization Tool")
        self.root.geometry("700x400")

        self.source_path = StringVar()
        self.dest_path = StringVar()
        self.scanner = FileScanner()
        self.manager = SyncManager()

        self.setup_ui()

    def setup_ui(self):
        Label(self.root, text="Source Directory:", font=('Arial', 12)).pack(pady=5)
        Entry(self.root, textvariable=self.source_path, width=60).pack()
        Button(self.root, text="Browse", command=self.browse_source).pack(pady=5)

        Label(self.root, text="Destination Directory:", font=('Arial', 12)).pack(pady=5)
        Entry(self.root, textvariable=self.dest_path, width=60).pack()
        Button(self.root, text="Browse", command=self.browse_dest).pack(pady=5)

        Button(self.root, text="Scan & Compare", command=self.scan_compare).pack(pady=10)
        Button(self.root, text="Sync Files", command=self.sync_files, bg='lightgreen').pack(pady=5)
        Button(self.root, text="Exit", command=self.root.quit, bg='lightcoral').pack(pady=5)

        self.log_box = Text(self.root, height=10, width=80)
        self.log_box.pack(pady=10)

    def browse_source(self):
        self.source_path.set(filedialog.askdirectory())

    def browse_dest(self):
        self.dest_path.set(filedialog.askdirectory())

    def scan_compare(self):
        src = self.source_path.get()
        dest = self.dest_path.get()
        if not src or not dest:
            messagebox.showerror("Error", "Select both directories!")
            return

        src_data = self.scanner.scan_folder(src)
        dest_data = self.scanner.scan_folder(dest)

        result = self.manager.compare_folders(src_data, dest_data)
        self.log_box.insert(END, f"\n✅ Scan complete!\n{result}\n")

    def sync_files(self):
        src = self.source_path.get()
        dest = self.dest_path.get()
        if not src or not dest:
            messagebox.showerror("Error", "Select both directories!")
            return

        log = self.manager.sync(src, dest)
        self.log_box.insert(END, f"\n🚀 Sync started...\n{log}\n")

if __name__ == "__main__":
    root = Tk()
    app = SyncItApp(root)
    root.mainloop()
