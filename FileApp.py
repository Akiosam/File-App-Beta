from tkinter import *
from tkinter import messagebox, ttk, filedialog
import shutil
import os

def move_file():
    src_file = os.path.abspath(T.get("1.0", "end-1c"))
    dst_file = os.path.abspath(T1.get("1.0", "end-1c"))
    try:
        shutil.move(src_file, dst_file)
        messagebox.showinfo("Success", "File moved successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

window = Tk()


label = ttk.Label(window, text="Source File:")
label.pack()

T = Text(window, height=5, width=52)
T.pack()

label1 = ttk.Label(window, text="Destination File:")
label1.pack()

T1 = Text(window, height=5, width=52)
T1.pack()


btn = ttk.Button(window, text="Move File", width=20, command=move_file)
btn.pack(pady=20)


style = ttk.Style()
style.configure("TButton", foreground="blue")


src_browse = ttk.Button(window, text='Browse', command=lambda: T.insert(END, filedialog.askopenfilename()))
src_browse.pack()


dst_browse = ttk.Button(window, text='Browse', command=lambda: T1.insert(END, filedialog.askdirectory()))
dst_browse.pack()

window.title("File Mover")
window.geometry("320x250")
window.configure(background='blue')
window.mainloop()