import sys
import os

# Add the parent directory to the path so we can import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_FILES
from src.file_scanner import FileScanner
from src.content_analyzer import ContentAnalyzer

class LabelAutomationApp:
    def __init__(self, root):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = root
        self.root.title("Label Automation v2.0")
        self.root.geometry("700x500")
        self.root.configure(bg="#0a1931")

        self.select_btn = ctk.CTkButton(root, text="Select Folder", command=self.select_folder, corner_radius=20, fg_color="#185adb", hover_color="#1e3a8a", text_color="#fff")
        self.select_btn.pack(pady=10)

        self.dnd_label = ctk.CTkLabel(root, text="Drag and drop a folder here", width=400, height=40, corner_radius=20, fg_color="#185adb", text_color="#fff", font=("Segoe UI", 13, "bold"))
        self.dnd_label.pack(pady=10)
        self.dnd_label.drop_target_register(DND_FILES)  # type: ignore
        self.dnd_label.dnd_bind('<<Drop>>', self.drop_folder)  # type: ignore
        self.dnd_label.dnd_bind('<<DragEnter>>', self.on_drag_enter)  # type: ignore
        self.dnd_label.dnd_bind('<<DragLeave>>', self.on_drag_leave)  # type: ignore

        self.result_box = ctk.CTkTextbox(root, width=650, height=300, corner_radius=15, fg_color="#11204d", text_color="#fff", font=("Segoe UI", 11))
        self.result_box.pack(padx=10, pady=10)

        self.progress = ctk.CTkProgressBar(root, width=600, height=15, corner_radius=7)
        self.progress.pack(pady=5)
        self.progress.set(0)

    def select_folder(self):
        from tkinter import filedialog
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.result_box.delete("1.0", "end")
            self.result_box.insert("end", f"Scanning folder: {folder_selected}\n\n")
            self.analyze_folder(folder_selected)

    def drop_folder(self, event):
        data = event.data.strip()
        if data.startswith('{') and data.endswith('}'):
            folder_path = data[1:-1]
        else:
            folder_path = data
        if os.path.isdir(folder_path):
            self.result_box.delete("1.0", "end")
            self.result_box.insert("end", f"Scanning folder: {folder_path}\n\n")
            self.analyze_folder(folder_path)
        else:
            from tkinter import messagebox
            messagebox.showerror("Invalid Drop", f"Please drop a folder, not a file.\nDropped: {folder_path}")

    def on_drag_enter(self, event):
        self.dnd_label.configure(fg_color="#15306b")  # Slightly darker blue

    def on_drag_leave(self, event):
        self.dnd_label.configure(fg_color="#185adb")  # Restore original color

    def analyze_folder(self, folder_path):
        scanner = FileScanner()
        analyzer = ContentAnalyzer()
        all_files = []
        for root, _, files in os.walk(folder_path):
            for file in files:
                all_files.append(os.path.join(root, file))
        total_files = len(all_files)
        self.progress.set(0)

        for idx, file_path in enumerate(all_files, 1):
            content = scanner.read_file(file_path)
            if content:
                sensitivity = analyzer.analyze_file(content)
                file_name = os.path.basename(file_path)
                self.result_box.insert("end", f"{file_name} : {sensitivity}\n")
            # Set progress as a float between 0 and 1
            self.progress.set(idx / total_files if total_files else 1)
            self.root.update_idletasks()

        self.result_box.insert("end", "\nScan complete.")

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = LabelAutomationApp(root)
    root.mainloop()