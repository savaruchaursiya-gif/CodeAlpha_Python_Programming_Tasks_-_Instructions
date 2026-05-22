import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def select_folder():
    folder = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, folder)

def move_files():
    source_folder = entry_path.get()

    if source_folder == "":
        messagebox.showerror("Error", "Please select a folder")
        return

    if not os.path.exists(source_folder):
        messagebox.showerror("Error", "Folder not found")
        return

    destination_folder = os.path.join(source_folder, "jpg_files")
    os.makedirs(destination_folder, exist_ok=True)

    moved = 0

    try:
        for file in os.listdir(source_folder):
            if file.lower().endswith(".jpg"):
                src = os.path.join(source_folder, file)
                dst = os.path.join(destination_folder, file)

                shutil.move(src, dst)
                listbox.insert(tk.END, "Moved: " + file)
                moved += 1

        if moved == 0:
            messagebox.showinfo("Result", "No JPG files found")
        else:
            messagebox.showinfo("Result", f"{moved} files moved successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("JPG File Mover")
root.geometry("500x400")

tk.Label(root, text="Select Folder").pack(pady=5)

entry_path = tk.Entry(root, width=50)
entry_path.pack(pady=5)

tk.Button(root, text="Browse", command=select_folder).pack(pady=5)
tk.Button(root, text="Move JPG Files", command=move_files).pack(pady=5)

listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)

root.mainloop()