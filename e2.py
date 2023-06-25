import pandas as pd
from datetime import datetime
import os
import tkinter as tk
from tkinter import messagebox
from download import download

web_file_url = 'https://frozecrate.000webhostapp.com/app_version/check_test/check1.xlsx'
save_folder = 'sysverinfo/check'
existing_file_path = os.path.join(save_folder, 'check01.xlsx')

# Function to download the web file and save it
def download_web_file(url, save_path):
    downloaded_file_path, _ = download(url, save_path, replace=True)
    return downloaded_file_path

# Function to check if the web file matches the existing file
def is_file_matching(web_file, existing_file):
    try:
        web_df = pd.read_excel(web_file, engine='openpyxl')
        existing_df = pd.read_excel(existing_file, engine='openpyxl')
        return web_df.equals(existing_df)
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError):
        return False

# Function to perform the monthly update check
def perform_monthly_update():
    current_date = datetime.now()
    current_month = current_date.strftime("%B")
    current_year = current_date.strftime("%Y")
    new_file_path = os.path.join(save_folder, f"{current_month}_{current_year}.xlsx")

    # Check if the web file matches the existing file
    if is_file_matching(web_file_url, existing_file_path):
        messagebox.showinfo("Update Check", "No update required.")
    else:
        try:
            download_web_file(web_file_url, existing_file_path)
            messagebox.showinfo("Update Check", "New update downloaded and saved.")
        except Exception as e:
            messagebox.showerror("Update Check", f"Error downloading the file: {str(e)}")

    # Perform any necessary operations on the data
    # For example, you can read the existing file using pandas and modify the data

    # Create a new Excel file with the modified data
    try:
        df = pd.read_excel(existing_file_path)
        df.to_excel(new_file_path, index=False)
        messagebox.showinfo("Update Check", "New update created.")
    except pd.errors.EmptyDataError:
        messagebox.showerror("Update Check", "Empty data file.")
    except pd.errors.ParserError:
        messagebox.showerror("Update Check", "Invalid file format.")

# Create the main GUI window
window = tk.Tk()
window.title("Update Check")
window.geometry("500x300+200+100")

# Function to handle the button click event
def on_button_click():
    perform_monthly_update()

# Create the button
button = tk.Button(window, text="Check for Updates", command=on_button_click)
button.pack(pady=10)

# Run the main GUI loop
window.mainloop()
