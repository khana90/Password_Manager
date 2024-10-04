from tkinter import *
from tkinter import messagebox
import random
from random import choice, randint,shuffle
import pyperclip
import json
# -----------------password generator--------------------------------------
#Password Generator Project
def Generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters= [choice(letters) for _ in range(randint (8, 10))]
    password_symbols= [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers= [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password= "".join(password_list)
    # copy the generated password automatically
    pyperclip.copy(password)
# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")
    password_entry.insert(0, password)
#------------------ save password -------------------------------------------
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data= {
        website: {
            "email" : email,
            "password" :password,
        }
    }

    if len(website) == 0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="You left one or more fields empty!")
    else:
        try:
        # is_ok = messagebox.askokcancel(title=website, message=f"These details are entered: \nEmail:{email}"
        #                                               f"\nPassword: {password} \nIs it OK to Save?")
        # if is_ok:
            with open("data.json", "r") as data_file:
                   # reading data
                 data= json.load(data_file)
        except FileNotFoundError:
             with open("data.json", "w") as data_file:
                  json.dump(new_data,data_file,indent=4)

        else:
              #updating data
             data.update(new_data)
            # saving old data
             with open("data.json", "w") as data_file:
              json.dump(data,data_file,indent=4)
        finally:
            # data_file.write(f"{website} | {email} | {password}\n")
             website_entry.delete(0,END)
             password_entry.delete(0,END)
# --------------------Find Password-----------------------------------------
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data= json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title= "Error", message="Data not found error")
    else:
        if website in data:
            email=data[website]["email"]
            password =data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword :{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")


#--------------------UI setup------------------------------------------------

window=Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)

canvas=Canvas(height=200, width=200)
logo_img= PhotoImage(file="logo.png")
# asking to add tupple to image width and height ,which is half of the actual canvas
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

# labels
website_labl = Label (text="Website:")
website_labl.grid(row=1,column=0)
email_labl= Label(text="Email/Username:")
email_labl.grid(row=2,column=0)
password_labl=Label(text="Password:")
password_labl.grid(row=3,column=0)

# Entries
website_entry= Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2)
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=3)
email_entry.insert(0,"zaheer_kan@lve.co.uk")
password_entry=Entry(width=20)
password_entry.grid(row=3,column=1)

# Buttons
generate_pass_btn=Button(text="Generate Password",width=11, command=Generate_pass)
generate_pass_btn.grid(row=3, column=2)
add_btn=Button(text="Add", width=33,command=save)
add_btn.grid(row=4,column=1,columnspan=2)
search_btn= Button(text="Search",width=10,command=find_password)
search_btn.grid(row=1,column=2)

window.mainloop()
