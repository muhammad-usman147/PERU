import customtkinter
from tkinter import messagebox,filedialog
import subprocess
import tkinter.font as tkfont
import requests 
from tkinter import DISABLED



customtkinter.set_appearance_mode('white')
root = customtkinter.CTk()
root.geometry("1080x550")



def browse_file():
    file_path = filedialog.askopenfilename()
    if not file_path.lower().endswith(('.xls','.xlsx')):
        messagebox.showerror("File Error","Only Excel File is Accepted")
    else:
        entry3.insert(0, file_path)
    



def execute():
    file_path = entry3.get()
    username = entry1.get()
    password = entry2.get()
    
    entry3.delete(0, 'end')
    print("Reading From:", file_path)
    # Call the sample function from the dynamic module
    ret = Automate(file_path, username, password)
    if ret == False:
        messagebox.showerror("Error","Something went wrong")


def Ammend_data():
    file_path = entry3.get()
    username = entry1.get()
    password = entry2.get()
    
    entry3.delete(0, 'end')
    print("Reading From:", file_path)
    # Call the sample function from the dynamic module
    ret = Ammend_Fields(file_path, username, password)
    if ret == False:
        messagebox.showerror("Error","Something went wrong")



frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)
frame.configure(width=500)
button_font = customtkinter.CTkFont(size=20)

inner_frame = customtkinter.CTkFrame(master=frame)
inner_frame.pack()

label = customtkinter.CTkLabel(master=inner_frame, text="Peru Work", text_color='Green', font=("Arial", 60),)
label.grid(row=0, column=0, columnspan=3, pady=20, padx=10)

entry3_variable = customtkinter.StringVar()
entry3 = customtkinter.CTkEntry(master=inner_frame, placeholder_text="File Path", textvariable=entry3_variable)
entry3.grid(row=1, column=0, pady=12, padx=10, sticky="ew")
entry3.configure(width=500)  # Set desired width of the entry widget

browse_button = customtkinter.CTkButton(master=inner_frame, text="Browse", command=browse_file,
                                        bg_color='Green', fg_color='Green', font=button_font)
browse_button.grid(row=1, column=1, pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=inner_frame, placeholder_text="Textbox1")
entry1.grid(row=2, column=0, pady=12, padx=10, sticky="ew")

entry2 = customtkinter.CTkEntry(master=inner_frame, placeholder_text="Textbox2")
entry2.grid(row=3, column=0, pady=12, padx=10, sticky="ew")
try:
    cond = requests.get("http://usman4485.pythonanywhere.com/damco-activation")
    cond.raise_for_status()
    cond = cond.text
except requests.exceptions.RequestException as e:
    cond = False
    messagebox.showerror("Connection Error","Please Check your internet Connection")
except:
    cond = False
    messagebox.showerror("Something Went Wrong","Unexpected Error")

button = customtkinter.CTkButton(master=inner_frame, text="Button", command=execute,
                                    bg_color='Green', fg_color='Green', font=button_font)
button.grid(row=4, column=0, columnspan=2, pady=12, padx=10, sticky="ew")

print("-->",cond)
if not cond == "True":
    button.configure(state=DISABLED)

root.mainloop()
