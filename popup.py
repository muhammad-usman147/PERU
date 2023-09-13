import customtkinter
import pandas as pd

df = pd.read_excel("dataemployees.xlsx")

def SearchFilter():
    pass 


def popup_window():
    popup_window = customtkinter.CTk()
    popup_window.geometry("1080x550")
    frame2 = customtkinter.CTkFrame(master=popup_window,width=2000)
    frame2.pack(pady=20, padx=20 ,fill='both', expand=True)
    inner_frame = customtkinter.CTkFrame(master=frame2)
    inner_frame.pack()


    # HU-21 : search by Name 
    age_search= customtkinter.CTkLabel(master=inner_frame, text="Search By Age", text_color='Green', font=("Arial",8),)
    age_search.grid(row=1, column=0, columnspan=3, pady=20, padx=10)
    theme = customtkinter.CTkComboBox(master=inner_frame, values = [str(i) for i in df['Age'].unique()],#command=SearchFilter,
                                    fg_color='Green',bg_color='Green',text_color='White')
    theme.grid(row=1,column=1,columnspan=1,padx=5,sticky='ew',)
    # Add content to the popup window
    customtkinter.CTkLabel(popup_window, text="This is a popup window").pack(pady=20, padx=20 )
    customtkinter.CTkButton(popup_window, text="Close Popup", command=popup_window.destroy).pack()

