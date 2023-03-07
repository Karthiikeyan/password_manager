from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generatepassword():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_synbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_synbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="The File dosn't Exist")

    else:
        if website in data:
            mail = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title="Information", message=f"Email : {mail}\nPassword : {password}")
        else:
            messagebox.showinfo(title="Oops", message="The Website doesn't Exist")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    with open(file="data.txt",mode="a") as data_file:
        website = website_entry.get()
        email = mail_entry.get()
        password = password_entry.get()
        newdata = {website : {"Email" : email, "Password" : password}}

        if len(website)==0 or len(email)==0 or len(password)==0:
            messagebox.showerror(title="Error", message="Don't Leave any box Empty")
        elif ".com" not in website:
            messagebox.showerror(title="Website Error", message="Invalid Website")
        elif '@' not in email:
            messagebox.showerror(title="Email Error", message="Invalid Email address")
        elif len(password)<=8:
            messagebox.showerror(title="Password Error", message="Password should be atleast 8 characters")
        else:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(newdata)
                with open("data.json", "w") as data_file:
                    json.dump(data ,data_file, indent=4)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(newdata,data_file, indent=4)
            finally:
                website_entry.delete(0,END)
                mail_entry.delete(0,END)
                password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
image = canvas.create_image(100,100,image=photo)
canvas.grid(row=0,column=1)

website_label = Label(text="Website :")
website_label.grid(row=1, column=0)
website_label.focus()

mail_label = Label(text="Email :")
mail_label.grid(row=2, column=0)

password_label = Label(text="Password :")
password_label.grid(row=3, column=0)



website_entry = Entry(width=31)
website_entry.grid(row=1, column=1)
website_entry.focus()


mail_entry = Entry(width=50)
mail_entry.grid(row= 2, column=1, columnspan=2)

password_entry = Entry(width=31)
password_entry.grid(row=3, column=1)

generate = Button(text="Generate Password", width=14, command=generatepassword)
generate.grid(row=3, column=2)

search = Button(text="Search", width=14, command=find_password)
search.grid(row=1, column=2)

button = Button(text="Add", width=35, command=save)
button.grid(row=4, column=1, columnspan=2)


window.mainloop()