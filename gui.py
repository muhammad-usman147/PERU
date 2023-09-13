import customtkinter
from tkinter import messagebox,filedialog
import subprocess
import tkinter.font as tkfont
import requests 
from tkinter import DISABLED
from resignationprediction import ResignationPrediction
import cv2
from popup import popup_window

#customtkinter.set_appearance_mode('dark')
root = customtkinter.CTk()
root.geometry("1080x550")

rp_obj = ResignationPrediction()
def open_popup():
    popup_window()
popup_button = customtkinter.CTkButton(root, text="Open Popup", command=open_popup)
popup_button.pack()
def browse_file():
    file_path = filedialog.askopenfilename()
    if not file_path.lower().endswith(('.xls','.xlsx')):
        messagebox.showerror("File Error","Only Excel File is Accepted")
    else:
        entry3.insert(0, file_path)
    



def execute():
    file_path = entry3.get()
    #username = entry1.get()
    #password = entry2.get()
    
    entry3.delete(0, 'end')
    print("Reading From:", file_path)
    # Call the sample function from the dynamic module
    rp_obj.preprocess(file_path)
    rp_obj.train()

def Predictions():
    rp_obj.predict()




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


def on_hover(event):
    vis_resig_emp.configure(text_color='LightBlue',fg_color='Green',bg_color='Green')
def on_leave(event):
    vis_resig_emp.configure(text_color='Green',fg_color='Orange',bg_color='Orange')





frame = customtkinter.CTkFrame(master=root,width=2000)
frame.pack(pady=20, padx=20 ,fill='both', expand=True)
button_font = customtkinter.CTkFont(size=20)
button_font2 = customtkinter.CTkFont(size=18,weight='bold')


inner_frame = customtkinter.CTkFrame(master=frame)
inner_frame.pack()

label = customtkinter.CTkLabel(master=inner_frame, text="Peru Work", text_color='Green', font=("Arial", 60),)
label.grid(row=0, column=0, columnspan=3, pady=20, padx=10)

entry3_variable = customtkinter.StringVar()
entry3 = customtkinter.CTkEntry(master=inner_frame, placeholder_text="File Path", textvariable=entry3_variable)
entry3.grid(row=1, column=0, pady=12, padx=10, sticky="ew")
entry3.configure(width=500)  # Set desired width of the entry widget


#HU-02 : Importing the database into the system
browse_button = customtkinter.CTkButton(master=inner_frame, text="Browse", command=browse_file,
                                        bg_color='Green', fg_color='Green', font=button_font)
browse_button.grid(row=1, column=1, pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=inner_frame, placeholder_text="Textbox1")
entry1.grid(row=2, column=0, pady=12, padx=10, sticky="ew")

entry2 = customtkinter.CTkEntry(master=inner_frame, placeholder_text="Textbox2")
entry2.grid(row=3, column=0, pady=12, padx=10, sticky="ew")

#HU-04 : System to learn from the imported database
train_button = customtkinter.CTkButton(master=inner_frame, text="HU-04: Start Training", command=execute,
                                    bg_color='Green', fg_color='Green', font=button_font)
train_button.grid(row=4, column=0, columnspan=2, pady=12, padx=10, sticky="ew")


#HU-05 : System Predictions
predict_button = customtkinter.CTkButton(master=inner_frame, text='HU-05: Predict', command = Predictions,
                                        bg_color='#3d3db8',fg_color='#3d3db8', font=button_font)
predict_button.grid(row=5,column=0,columnspan=2,pady=12,padx=10,sticky='ew')

#HU-06: Visualize possible regisnation of employees from there table
vis_resig_emp = customtkinter.CTkButton(master=inner_frame,text='HU-06: Show Possible \n Resignations',command='#',
                                        fg_color='Orange',font=button_font2,text_color='Green')
vis_resig_emp.grid(row=1,column=2,columnspan=1,pady=12,padx=5,sticky='ew',)
vis_resig_emp.bind("<Enter>",on_hover)
vis_resig_emp.bind("<Leave>",on_leave)


#HU-07: Visualize possible regisnation of employees from there table

def on_hover1(event):
    vis_resig_emp2.configure(text_color='LightBlue',fg_color='Green',bg_color='Green')
def on_leave1(event):
    vis_resig_emp2.configure(text_color='Green',fg_color='Orange',bg_color='Orange')

vis_resig_emp2 = customtkinter.CTkButton(master=inner_frame,text='HU-07: Show Voluntary \n Resignations',command='#',
                                        fg_color='Orange',font=button_font2,text_color='Green')
vis_resig_emp2.grid(row=2,column=2,columnspan=1,pady=5,padx=5,sticky='ew',)


vis_resig_emp2.bind("<Enter>",on_hover1)
vis_resig_emp2.bind("<Leave>",on_leave1)
#HU-08: Display Predictibility Meter

def on_hover3(event):
    vis_resig_emp3.configure(text_color='LightBlue',fg_color='Green',bg_color='Green')
def on_leave3(event):
    vis_resig_emp3.configure(text_color='Green',fg_color='Orange',bg_color='Orange')

vis_resig_emp3 = customtkinter.CTkButton(master=inner_frame,text='HU-08: Display Predictibility \n Meter',command='#',
                                        fg_color='Orange',font=button_font2,text_color='Green')
vis_resig_emp3.grid(row=1,column=3,columnspan=1,pady=5,padx=5,sticky='ew',)


vis_resig_emp3.bind("<Enter>",on_hover3)
vis_resig_emp3.bind("<Leave>",on_leave3)

#HU-09: Download Table

def on_hover4(event):
    vis_resig_emp4.configure(text_color='LightBlue',fg_color='Green',bg_color='Green')
def on_leave4(event):
    vis_resig_emp4.configure(text_color='Green',fg_color='Orange',bg_color='Orange')

vis_resig_emp4 = customtkinter.CTkButton(master=inner_frame,text='HU-09: Download \n Predictions(PDF)',command='#',
                                        fg_color='Orange',font=button_font2,text_color='Green')
vis_resig_emp4.grid(row=2,column=3,columnspan=1,pady=5,padx=5,sticky='ew',)


vis_resig_emp4.bind("<Enter>",on_hover4)
vis_resig_emp4.bind("<Leave>",on_leave4)

#HU-10 - HU - 13 Display Charts
def on_hover5(event):
    vis_resig_emp5.configure(text_color='LightBlue',fg_color='Green',bg_color='Green')
def on_leave5(event):
    vis_resig_emp5.configure(text_color='Green',fg_color='Orange',bg_color='Orange')

vis_resig_emp5 = customtkinter.CTkButton(master=inner_frame,text='HU-1013: Show Charts',command='#',
                                        fg_color='Orange',font=button_font2,text_color='Green')
vis_resig_emp5.grid(row=3,column=2,columnspan=1,pady=5,padx=5,sticky='ew',)
vis_resig_emp5.bind("<Enter>",on_hover5)
vis_resig_emp5.bind("<Leave>",on_leave5)
#HU-14 Display Variables
def on_hover6(event):
    vis_resig_emp6.configure(text_color='LightBlue',fg_color='Green',bg_color='Green')
def on_leave6(event):
    vis_resig_emp6.configure(text_color='Green',fg_color='Orange',bg_color='Orange')

vis_resig_emp6 = customtkinter.CTkButton(master=inner_frame,text='HU-14: Display Variables',command='#',
                                        fg_color='Orange',font=button_font2,text_color='Green')
vis_resig_emp6.grid(row=4,column=2,columnspan=1,pady=5,padx=5,sticky='ew',)
vis_resig_emp6.bind("<Enter>",on_hover6)
vis_resig_emp6.bind("<Leave>",on_leave6)

#HU-15 Download All Charts
def on_hover7(event):
    vis_resig_emp7.configure(text_color='LightBlue',fg_color='Green',bg_color='Green')
def on_leave7(event):
    vis_resig_emp7.configure(text_color='Green',fg_color='Orange',bg_color='Orange')

vis_resig_emp7 = customtkinter.CTkButton(master=inner_frame,text='HU-15: Download Graphs',command='#',
                                        fg_color='Orange',font=button_font2,text_color='Green')
vis_resig_emp7.grid(row=3,column=3,columnspan=1,pady=5,padx=5,sticky='ew',)
vis_resig_emp7.bind("<Enter>",on_hover7)
vis_resig_emp7.bind("<Leave>",on_leave7)



#HU-16 Download Table
def on_hover8(event):
    vis_resig_emp8.configure(text_color='LightBlue',fg_color='Green',bg_color='Green')
def on_leave8(event):
    vis_resig_emp8.configure(text_color='Green',fg_color='Orange',bg_color='Orange')

vis_resig_emp8 = customtkinter.CTkButton(master=inner_frame,text='HU-15: Download Prediction \n Table (excel)',command='#',
                                        fg_color='Orange',font=button_font2,text_color='Green')
vis_resig_emp8.grid(row=5,column=2,columnspan=1,pady=5,padx=5,sticky='ew',)
vis_resig_emp8.bind("<Enter>",on_hover8)
vis_resig_emp8.bind("<Leave>",on_leave8)




#HU-17 Download Table

vis_resig_emp9 = customtkinter.CTkButton(master=inner_frame,text='HU-17: Exit',command='#',
                                        fg_color='#ed1f37',bg_color='#ed1f37',font=button_font2,text_color='White')
vis_resig_emp9.grid(row=6,column=3,columnspan=1,padx=5,sticky='ew',)

#HU-18 Change Theme
def change_theme(event):
    selected_theme = theme.get()

    if selected_theme == "Light Theme":
        #root.tk_setPalette(background='#FFFFFF', foreground='#000000')
        customtkinter.set_appearance_mode('light')

    elif selected_theme == "Dark Theme":
        #root.tk_setPalette(background='#000000', foreground='#FFFFFF')
        customtkinter.set_appearance_mode('dark')

theme = customtkinter.CTkComboBox(master=inner_frame, values = ['Light Theme','Dark Theme'],command=change_theme,
                                    fg_color='Green',bg_color='Green',text_color='White')
theme.grid(row=2,column=1,columnspan=1,padx=5,sticky='ew',)

theme.set("Light")

#HU-20 Help Button
def displayGuide():
    img = cv2.imread("guide.png")
    cv2.imshow("System Guide",img)
    cv2.waitKey()
    cv2.destroyAllWindows()


help = customtkinter.CTkButton(master=inner_frame,text='HU-20: System Guide',command=displayGuide,
                                        fg_color='#ed1f37',bg_color='#ed1f37',font=button_font2,text_color='White')
help.grid(row=3,column=1,columnspan=1,padx=5,sticky='ew',)

root.mainloop()
