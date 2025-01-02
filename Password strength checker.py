import   customtkinter 
from tkinter import *
from tkinter import messagebox
import re

app=customtkinter.CTk()
app.title("Password Strength Checker")
app.geometry("400x300+480+200")
app.config(bg="#000")
app.resizable(False,False)


title_font = ("Arial",20,"bold")
subtitle_font = ("Arial",17,"bold")
button_font = ("Arial",18,"bold")

def is_strong_password(password):
    if len(password) < 8:
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[!@#$%^&*()_+]", password):
        return False

    return True

def display_password_result():
    password = password_text_box.get()
    if password:
        result_text_box.configure(state="normal")
        result_text_box.delete(0, END)
        
        if is_strong_password(password):
            result_text_box.insert(0, "Strong Password")
            result_text_box.configure(fg_color="#069602")
        else:
            result_text_box.insert(0, "Not Recmmended")
            result_text_box.configure(fg_color="#F00")

            result_text_box.configure(state="disabled")
    else:
            
            messagebox.showerror(title="Error",message= "Please enter a password.")   


title_label = customtkinter.CTkLabel(app,text="Password Strength Checker",font=title_font,text_color="#FFF",bg_color="#000")
title_label.place(x=70,y=20)

password_text_box = customtkinter.CTkEntry(app,font=subtitle_font,text_color="#FFF",fg_color="#000",bg_color="#000",border_color="#F53905",width=300,height=50)
password_text_box.place(x=50,y=60)

check_button = customtkinter.CTkButton(app,command=display_password_result,text="Check Password",font=button_font,text_color="#FFF",fg_color="#F53905",bg_color="#000",hover_color="#FFF",cursor="hand2",corner_radius=20,width=150,height=40,)
check_button.place(x=105,y=130)
 
password_strength_label = customtkinter.CTkLabel(app,text="Your Password Strenght",font=title_font,text_color="#FFF",bg_color="#000")
password_strength_label.place(x=100,y=200)


result_text_box = customtkinter.CTkEntry(app,state="disabled",font=subtitle_font,text_color="#FFF",fg_color="#000",bg_color="#000",border_color="#FFF",justify="center",width=200,height=30)
result_text_box.place(x=100,y=240)



app.mainloop()
