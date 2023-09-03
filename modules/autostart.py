from tkinter import messagebox
# import pythoncom
# import win32com.client

import subprocess

def create_shortcut(target_path, shortcut_path, description="", icon_path="", working_directory=""):
    try:
        code = subprocess.call(["ln", "-s", target_path, shortcut_path])
        # shortcut = win32com.client.Dispatch("WScript.Shell").CreateShortcut(shortcut_path)
        # shortcut.TargetPath = target_path
        # shortcut.Description = description
        # shortcut.IconLocation = icon_path
        # shortcut.WorkingDirectory = working_directory
        # shortcut.Save()
        if code == 0:
            messagebox.showinfo("Success", f"Added '{target_path}' to Autostart")
        else:
            messagebox.showinfo("Error", f"Can not add to Autostart Error Code: {code}")    
    except Exception as e:
        messagebox.showinfo("Error", f"Can not add to Autostart: {str(e)}")
