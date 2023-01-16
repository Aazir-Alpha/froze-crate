

import tkinter as tk
from tkinter import filedialog
import urllib.request
from tqdm import tqdm


def download_file():
    url = entry_url.get()
    local_filename = filedialog.asksaveasfilename(
        initialdir="/", title="Select file", filetypes=(("all files", "*.*"), ("jpeg files", "*.jpg")))
    try:
        with urllib.request.urlopen(url) as url:
            total_size = int(url.headers.get("Content-Length", 0))
            block_size = 1024
            progress = tqdm(total=total_size, unit='B',
                            unit_scale=True, desc=local_filename, leave=False)
            with open(local_filename, "wb") as f:
                while True:
                    buffer = url.read(block_size)
                    if not buffer:
                        break
                    progress.update(len(buffer))
                    f.write(buffer)
            progress.close()
        label_status.config(text="Download complete")
    except Exception as e:
        label_status.config(text=str(e))


def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))


root = tk.Tk()
root.title("File Downloader")
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", toggle_fullscreen)

# Create sections
frame_url = tk.Frame(root)
frame_url.pack(fill=tk.X, padx=5, pady=5)

frame_download = tk.Frame(root)
frame_download.pack(fill=tk.X, padx=5, pady=5)

frame_status = tk.Frame(root)
frame_status.pack(fill=tk.X, padx=5, pady=5)

# Create widgets for the "URL" section
label_url = tk.Label(frame_url, text="Enter URL:")
label_url.grid(row=0, column=0, padx=5, pady=5)

entry_url = tk.Entry(frame_url)
entry_url.grid(row=0, column=1, padx=5, pady=5)

# Create widgets for the "Download" section
button_download = tk.Button(
    frame_download, text="Download", command=download_file)
button_download.grid(row=0, column=0, padx=5, pady=5)

# Create widgets for the "Status" section
label_status = tk.Label(frame_status, text="")
label_status.grid(row=0, column=0, padx=5, pady=5)

# Center the GUI on the screen
#root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
root.mainloop()
